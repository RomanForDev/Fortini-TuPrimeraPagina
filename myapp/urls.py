from django.urls import path
from myapp.views import inicio, crear_piedra, listar_piedras, contacto, detalle_piedra, borrar_piedra

urlpatterns= [
    path('', inicio, name= 'inicio'),
    path('crear-piedra/', crear_piedra, name="crear_piedra"),
    path('listar-piedra/', listar_piedras, name="listar_piedras"),
    path('contacto/', contacto, name='contacto',),
    path('detalle/<int:id>/', detalle_piedra, name='detalle_piedra'),
    path('borrar/<int:id>/', borrar_piedra, name='borrar_piedra'),
    path('editar-piedra/<int:id>/', acavalaclase, name='editar_piedra')
]