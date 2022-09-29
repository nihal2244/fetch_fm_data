from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from app.services import FilterAlbumData, GetFMAlbumData


class GetAlbumDetails(APIView):
    def get(self, request, *args, **kwargs):
        """APi to get first record from last.fm api"""
        data = GetFMAlbumData.fetch_data_album(self.kwargs["album"])
        filtered_data = FilterAlbumData.get_first_values(data)
        return Response(data=filtered_data)
