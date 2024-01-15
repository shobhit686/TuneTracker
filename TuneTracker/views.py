from django.shortcuts import render, redirect
from .models import Artist, Song


def Tuner(request):
    songs = Song.objects.order_by('?')
    context = {"songs": songs}
    return render(request, 'TuneTracker/base.html', context)


def Contribute(request):
    return render(request, 'TuneTracker/contribute.html')


def dataSubmission(request):
    if request.method == "POST":
        artist_name = request.POST.get('artist_name')
        data = Artist(artist_name=artist_name)
        data.save()
    return redirect('Home')
