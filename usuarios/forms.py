from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class NuestroUserCreationForm(UserCreationForm):
    username= forms.CharField(label='Nombre de usuario', max_length=150)
    email= forms.EmailField(required=False)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre', max_length=30)
    last_name= forms.CharField(label='Apellido', max_length=30)

    class Model:
        model= User
        fields= ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts= {llave: '' for llave in fields}