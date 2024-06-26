## wind-pioneers-case-study

# Introduction
This is a file/document-based AI assistant chat app. Users can select files from their drive and ask the assistant queries, which takes the selected file into context to answer.

# Project Demo
[Watch the video](https://www.loom.com/embed/d2068de6a1d74753bf86ba663e321d98?sid=b348e960-a948-4a7b-a0d5-44f7e088aeb4)

# Project Setup 
1. Create and activate a virtual environment named env (you can use any virtual environment manager, such as virtualenv or conda):
    virtualenv env
    source env/bin/activate
2. Install the required packages:
   - pip install -r requirements.txt
3. Add environment variable:
   1. Create a .env file in the root directory of the project.
   2. Add the OPENAI_API_KEY to the .env file.
4. Add Google credentials:
   - Save the Google credentials with the name client_secret.json in the app directory of the project.
5. Run the application
   - python manage.py runserver
6. Access the application at http://localhost:8000/app/files/.


# Main URL
Users can access the file selection feature of the application by visiting http://localhost:8000/app/files/. This page allows users to select files from their drive and interact with the AI assistant using the selected file as context.
