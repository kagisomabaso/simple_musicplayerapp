from django.shortcuts import render, get_object_or_404
from .models import Song, Playlist

def home(request):
    songs = Song.objects.all()
    return render(request, 'player/home.html', {'songs': songs})

def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/play.html', {'song': song})
