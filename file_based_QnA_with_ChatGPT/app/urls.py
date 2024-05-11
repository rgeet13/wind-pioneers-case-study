from django.urls import path
from .views import chat_view, file_view, view_file

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('files/', file_view, name='files'),
    path('view-file/', view_file, name='view-file')
]
