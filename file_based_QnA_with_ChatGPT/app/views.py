from django.shortcuts import render

def chat_view(request):
    # Define the WebSocket connection URL
    ws_url = 'ws://localhost:8000/ws/chat/'

    # Render the template with the WebSocket URL
    return render(request, 'chat_app.html', {'ws_url': ws_url})