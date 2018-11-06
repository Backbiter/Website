from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.shortcuts import render
from django.template import loader


def index(request):
    album_all = Album.objects.all()
    template = loader.get_template("home/music.html")
    con = {
        'album_all': album_all,
    }
    return HttpResponse(template.render(con, request))


def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Not found")
    return render(request, 'home/details.html',{'album': album})