from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import CrearPiedra
from myapp.models import piedra

def inicio(request):
    return render(request, 'inicio.html')

def crear_piedra(request):
    if request.method== "POST":
        formulario= CrearPiedra(request.POST)
        if formulario.is_valid():
            formulario.cleaned_data
            nueva_piedra= piedra(
                clase= formulario.cleaned_data.get('clase'),
                material= formulario.cleaned_data.get('material'),
                descripcion= formulario.cleaned_data.get('descripcion')
            )
            nueva_piedra.save()
        return render(request, 'inicio/crear_piedra.html', {'formulario': formulario})


def listar_piedras(request):
    existencias= piedra.objects.all()
    return render(request, 'inicio/listar_piedras.html', {'existencias': existencias})
            

