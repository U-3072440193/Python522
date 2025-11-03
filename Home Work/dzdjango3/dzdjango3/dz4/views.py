from django.shortcuts import render, get_object_or_404
from .models import Dz4


def dz4(request):
    dz = Dz4.objects.all()
    return render(request, 'dz4/dz4.html', {"dz": dz})


def detail(request, dz_id):
    dz = get_object_or_404(Dz4, pk=dz_id)
    return render(request, 'dz4/detail.html', {'dz': dz})
