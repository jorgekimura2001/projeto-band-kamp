from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics
import ipdb


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        return self.queryset.filter(album_id=self.kwargs.get('album_id'))

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get('album_id'))
