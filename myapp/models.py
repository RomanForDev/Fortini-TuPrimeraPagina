from django.db import models

class piedra(models.Model):
    clase= models.CharField(max_length=20)
    material= models.CharField(max_length=20)
    descripcion= models.TextField(null=True, blank=True)
    imagen= models.ImageField(upload_to='Imagen', null=True, blank=True)
    
    def __str__(self):
        return f'{self.clase} {self.material}'