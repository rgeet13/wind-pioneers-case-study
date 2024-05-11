from googleapiclient.http import MediaIoBaseDownload
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os, io

API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.metadata.readonly']
file_path = os.path.join(settings.BASE_DIR, 'app', 'client_secret.json')

def create_service():
    CLIENT_SECRET_FILE = file_path
    try:
        credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=SCOPES)
        service = build(API_NAME, API_VERSION, credentials=credentials)
        print(API_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def get_all_files_from_folder(folder_id):
    service = create_service()
    results = service.files().list(q=f"'{folder_id}' in parents", pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:
            print(f"{item['name']} ({item['id']})")
        return items

def download_file(file_id, file_name):
    service = create_service()
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%")
    
    with open(file_name, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
