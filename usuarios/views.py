from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from usuarios.forms import NuestroUserCreationForm
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

def registro(request):
    if request.method == 'POST':
        formulario= NuestroUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario= NuestroUserCreationForm()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})