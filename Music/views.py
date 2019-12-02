from django.shortcuts import render
from .models import Music


def embed_music(request):
    music_content = Music.objects.all().order_by('-id')
    return render(request, 'pages/music.html', {'music_content': music_content})

