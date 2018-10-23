from django.shortcuts import render, get_object_or_404
from suporte.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'suporte/entradas.html', {'entradas': entradas})


def list_entradas(request, pk):
    get_entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'suporte/entrada.html', {'get_entrada': get_entrada})


def atendimentos(request):
    atendimentos = Atendimento.objects.all()
    return

def novo_atendimento(request, pk):
    atendimento = get_object_or_404(Atendimento, pk=pk)
    return render(request, 'suporte/novo_atendimento.html', {'atendimento': atendimento})


def equipamentos(request):
    equips = Equipamento.objects.all()
    return render(request, 'suporte/equipamentos.html', {'equipamentos': equips})


def list_equipamentos(request, pk):
    get_equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'suporte/equipamento.html', {'get_equipamento': get_equipamento})


def novo_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'suporte/novo_equipamento.html', {'equipamento': equipamento})


def departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'suporte/departamentos.html', {'departamentos': departamentos})


def list_departamentos(request, pk):
    get_departamento = get_object_or_404(Departamento, pk=pk)
    return render(request, 'suporte/departamento.html', {'get_departamentos': get_departamento})
