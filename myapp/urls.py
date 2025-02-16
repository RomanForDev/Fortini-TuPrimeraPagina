from django.urls import path
from myapp.views import inicio, crear_piedra, listar_piedras, contacto

urlpatterns= [
    path('', inicio, name= 'inicio'),
    path('crear-piedra/', crear_piedra, name="crear_piedra"),
    path('listar-piedra/', listar_piedras, name="listar_piedras"),
    path('contacto/', contacto, name='contacto')
]