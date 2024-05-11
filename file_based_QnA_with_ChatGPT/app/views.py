from django.shortcuts import render
from .drive_utils import get_all_files_from_folder, download_file
from django.http import JsonResponse
import json

def chat_view(request):
    # Define the WebSocket connection URL
    ws_url = 'ws://localhost:8000/ws/chat/'

    # Render the template with the WebSocket URL
    return render(request, 'chat_app.html', {'ws_url': ws_url})

def file_view(request):
    try:
        folder_id = '13KSB55spACO_PyBswteQgiIZGm2ZRq2Q'
        files = get_all_files_from_folder(folder_id)
        context = {'files': files}
        return render(request, 'file_list.html', context)
    except Exception as e:
        print('Error:', e)
        return render(request, 'error.html', {'error_message': str(e)})

def view_file(request):
    try:
        if request.method == 'POST':
            data = request.body.decode('utf-8')
            print("Data -- ", data)
            try:
                json_data = json.loads(data)
            except json.JSONDecodeError as e:
                print('Error decoding JSON:', e)
                return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)

            file_name = json_data.get('file_name', None)
            file_id = json_data.get('file_id', None)
            print("File id -- ", file_id, "Filename -- ", file_name)
            download_file(file_id, file_name)
            return JsonResponse({'status': 'success', 'message': 'File downloaded'}, statu=201)
    except Exception as e:
        print('Error:', e)
        return render(request, 'error.html', {'error_message': str(e)})
