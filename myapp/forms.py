from django import forms

class CrearPiedra(forms.Form):
    clase= forms.CharField(max_length=20),
    material= forms.CharField(max_length=20),
    descripcion= forms.CharField(required=False, widget=forms.Textarea)
    