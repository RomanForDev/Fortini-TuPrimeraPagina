from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login, registro

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name= 'usuarios/logout.html'), name='logout'), #cvb
    path('register/', registro, name='registro'),
]
