from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer


class NoteCreateAPIView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

class NoteListAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        title_filter = self.request.query_params.get('title')
        if title_filter:
            queryset = queryset.filter(title__icontains=title_filter)
        return queryset
