from django.contrib import admin
from django.urls import path
from app.views import GetAlbumDetails

urlpatterns = [
    path("album/<str:album>", GetAlbumDetails.as_view()),
]
