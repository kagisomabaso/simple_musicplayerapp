from django.shortcuts import render, get_object_or_404
from .models import Song, Playlist

def home(request):
    songs = Song.objects.all()
    return render(request, 'player/home.html', {'songs': songs})

def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/play.html', {'song': song})

from django.shortcuts import render, redirect
from .forms import SongUploadForm


def upload_song(request):
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user  # Assign the logged-in user
            song.save()
            return redirect('home')  # Redirect to the homepage
    else:
        form = SongUploadForm()
    return render(request, 'player/upload_song.html', {'form': form})
