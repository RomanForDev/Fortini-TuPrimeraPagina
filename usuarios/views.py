from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from usuarios.forms import NuestroUserCreationForm, NuestroUserChangeForm
from django.contrib.auth import login as do_login

def login(request):
    if request.method == 'POST':
        formulario= AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario= formulario.get_user()
            do_login(request, usuario)
            return redirect('inicio')
    else:
        formulario= AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario}) 

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def registro(request):
    if request.method == 'POST':
        formulario= NuestroUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario= NuestroUserCreationForm()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def editar_perfil(request):
    if request.method == 'POST':
        formulario= NuestroUserChangeForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios/perfil.html') #no es editar_perfil, chequear!
    else:
        formulario= NuestroUserChangeForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'formulario': formulario})