from django.conf import settings
import openai
import traceback
from openai import OpenAI

# openai.api_key = settings.OPENAI_API_KEY
client = OpenAI(api_key=settings.OPENAI_API_KEY)
def upload_file(path):
    # Upload a file with an "assistants" purpose
    file = client.files.create(file=open(path, "rb"), purpose="assistants")
    return file

def create_vector_store_and_upload_files(file):
    """
    Create a vector store and upload the files to it.
    """
    # Create a vector store caled "FileBasedQnA"
    vector_store = client.beta.vector_stores.create(name="FileBasedQnA")
    
    # Ready the files for upload to OpenAI
    file_paths = [file]
    file_streams = [open(path, "rb") for path in file_paths]
    
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
    )
    
    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)
    return vector_store.id

def create_assistant():
    """
    You currently cannot set the temperature for Assistant via the API.
    """
    try:
        assistant = client.beta.assistants.create(
            name="FileBased QnA with ChatGPT",
            instructions="You might want to go through the following document to get a better understanding of the document.",
            tools=[{"type": "file_search"}],
            model="gpt-4-turbo",
        )
        return assistant
    except Exception as e:
        print("Error in creating assistant "+ str(e))
        return None

def update_assistant(assistant_id, vector_store_id):
    """
    Update the assistant with the vector store.
    """
    try:
        assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
        )
        return assistant
    except Exception as e:
        print("Error in updating assistant "+ str(e))
        return False
# --------------------------------------------------------------
# Thread management
# --------------------------------------------------------------
def create_thread(file_path, query):
    """
    Create a thread with the assistant.
    """
    try:
        # Upload the user provided file to OpenAI
        message_file = client.files.create(
        file=open(file_path, "rb"), purpose="assistants"
        )
        
        # Create a thread and attach the file to the message
        thread = client.beta.threads.create(
        messages=[
            {
            "role": "user",
            "content": query,
            # Attach the new file to the message.
            "attachments": [
                { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
            ],
            }
        ]
        )
        
        # The thread now has a vector store with that file in its tool resources.
        print(thread.tool_resources.file_search)
        return thread
    except Exception as e:
        print("Error in creating thread "+ str(e))
        return False

def get_response(assistant_id,thread_id):
    """
    Get the response from the assistant.
    """
    try:
        # Use the create and poll SDK helper to create a run and poll the status of
        # the run until it's in a terminal state.

        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread_id, assistant_id=assistant_id
        )
        messages = list(client.beta.threads.messages.list(thread_id=thread_id, run_id=run.id))
        message_content = messages[0].content[0].text
        return message_content.value
    except Exception as e:
        print("Error in getting response "+ str(e))
        return False

