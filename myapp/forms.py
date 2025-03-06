from django import forms
from myapp.models import piedra

class CrearPiedra(forms.Form):
    clase= forms.CharField(max_length=20)
    material= forms.CharField(max_length=20)
    descripcion= forms.CharField(required=False, widget=forms.Textarea)

class BuscarPiedra(forms.Form):
    clase= forms.CharField(max_length=20, required=False) #required False para que no exija poner algo si o si en la solicitud
    material= forms.CharField(max_length=20, required=False)
    
class EditarPiedraFormulario(forms.ModelForm):
    class Meta:
        model= piedra
        fields= '__all__' #est opuede ser una lista con cada elemento
        widgets= {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }