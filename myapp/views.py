from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import CrearPiedra
from myapp.models import piedra

def inicio(request):
    return render(request, 'inicio.html')

def crear_piedra(request):
    formulario= CrearPiedra()
    if request.method== "POST":
        formulario= CrearPiedra(request.POST)
        if formulario.is_valid():
            formulario.cleaned_data
            Piedra= piedra(
                clase=formulario.cleaned_data.get('clase'),
                material=formulario.cleaned_data.get('material'),
                descripcion=formulario.cleaned_data.get('descripcion')
                )
            Piedra.save()
    return render(request, 'crear_piedra.html', {'formulario': formulario})


def listar_piedras(request):
    existencias= piedra.objects.all()
    return render(request, 'listar_piedras.html', {'existencias': existencias})

def contacto(request):
    return render(request, 'contacto.html')
            

