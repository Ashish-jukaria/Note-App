from django.urls import path
from rest_framework import permissions
from .views import NoteCreateAPIView, NoteRetrieveUpdateAPIView, NoteListAPIView


urlpatterns = [
    path('notes/create/', NoteCreateAPIView.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateAPIView.as_view(), name='note-detail'),
    path('notes/', NoteListAPIView.as_view(), name='note-list'),
]
