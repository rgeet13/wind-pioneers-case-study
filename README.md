## wind-pioneers-case-study

# Introduction
This is a file/document-based AI assistant chat app. Users can select files from their drive and ask the assistant queries, which takes the selected file into context to answer.

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
6. Access the application at http://localhost:8000/app/.



