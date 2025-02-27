from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import CrearPiedra, BuscarPiedra
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
            return redirect("listar_piedras")
        
    return render(request, 'crear_piedra.html', {'formulario': formulario})


def listar_piedras(request):
    formulario= BuscarPiedra(request.GET)
    if formulario.is_valid():
        clase= formulario.cleaned_data.get('clase')
        material= formulario.cleaned_data.get('material')
        existencias= piedra.objects.filter(material__icontains=material, clase__icontains=clase)
    return render(request, 'listar_piedras.html', {'existencias': existencias, 'formulario': formulario})

def contacto(request):
    return render(request, 'contacto.html')
            

