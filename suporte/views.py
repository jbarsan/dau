from django.shortcuts import render, get_object_or_404
from suporte.models import *


# Create your views here.
def home(request):
    entradas = Entrada.objects.all()

    return render(request, 'home.html', {'entradas': entradas})


def entradas(request, pk):
    # entradas = Entrada.objects.get(pk=pk)
    entradas = get_object_or_404(Entrada, pk=pk)
    return render(request, 'suporte/entrada.html', {'entradas': entradas})
