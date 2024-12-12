from django import forms
from .models import Libro, Revista, Periodico

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'autor', 'isbn']

class RevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ['titulo', 'fecha_publicacion', 'numero', 'editorial']

class PeriodicoForm(forms.ModelForm):
    class Meta:
        model = Periodico
        fields = ['titulo', 'fecha_publicacion', 'seccion', 'editor']

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)