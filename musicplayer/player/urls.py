from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('song/<int:song_id>/', views.play_song, name='play_song'),
    path('upload/', views.upload_song, name='upload_song'),
]
