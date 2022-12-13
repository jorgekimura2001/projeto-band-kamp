from rest_framework import serializers

from .models import Album

import ipdb


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "user_id",
            "name",
            "year",
        ]
