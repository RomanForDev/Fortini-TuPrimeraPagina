from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import CrearPiedra, BuscarPiedra, EditarPiedraFormulario
from myapp.models import piedra
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio.html')

def crear_piedra(request):
    formulario= CrearPiedra()
    if request.method== "POST":
        formulario= CrearPiedra(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.cleaned_data
            Piedra= piedra(
                clase=formulario.cleaned_data.get('clase'),
                material=formulario.cleaned_data.get('material'),
                descripcion=formulario.cleaned_data.get('descripcion'),
                imagen=formulario.cleaned_data.get('imagen')
                )
            Piedra.save()
            return redirect("listar_piedras")
        
    return render(request, 'crear_piedra.html', {'formulario': formulario})


def listar_piedras(request):
    formulario= BuscarPiedra(request.GET)
    if formulario.is_valid():
        clase= formulario.cleaned_data.get('clase')
        material= formulario.cleaned_data.get('material')
        imagen= formulario.cleaned_data.get('imagen')
        existencias= piedra.objects.filter(material__icontains=material, clase__icontains=clase) #, imagen__icontains=imagen)
    return render(request, 'listar_piedras.html', {'existencias': existencias, 'formulario': formulario})

def detalle_piedra(request, id):
    piedras= piedra.objects.get(id=id)
    return render(request, 'detalle_piedra.html', {'piedra': piedras})

def borrar_piedra(request, id):
    piedras= piedra.objects.get(id=id)
    piedras.delete()
    return redirect("listar_piedras")

def contacto(request):
    return render(request, 'contacto.html')
            
class EditarPiedra(LoginRequiredMixin, UpdateView):
    model = piedra
    template_name = "editar_piedra.html"
    success_url = reverse_lazy("listar_piedras")
    form_class=  EditarPiedraFormulario #sirve para crear un formulario personalizado, se debe importar el formulario. Sirve para hacerlo mas personalizado.
    #fields= '__all__' #esto es para que se muestren todos los campos del
    #formulario, si no se pone, se debe especificar los campos que se quieren mostrar 
    #(ej: "clase", "material", "descripcion") si se pone mas de una se hace en una lista

class BorrarPiedra(LoginRequiredMixin, DeleteView):
    model = piedra
    template_name = "borrar_piedra.html"
    success_url = reverse_lazy("listar_piedras")
