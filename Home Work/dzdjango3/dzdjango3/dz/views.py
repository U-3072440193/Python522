from django.shortcuts import render
from .models import Dz


def index(request):
    albums = Dz.objects.all()
    return render(request, 'dz/index.html', {'albums': albums})
