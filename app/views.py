from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import LibroForm, RevistaForm, PeriodicoForm, BuscarForm
from .models import Libro, Revista, Periodico
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def insertar(request):
    if request.method == 'POST':
        libro_form = LibroForm(request.POST, prefix='libro')
        revista_form = RevistaForm(request.POST, prefix='revista')
        periodico_form = PeriodicoForm(request.POST, prefix='periodico')
        if libro_form.is_valid() and revista_form.is_valid() and periodico_form.is_valid():
            libro_form.save()
            revista_form.save()
            periodico_form.save()
            return redirect('home')
    else:
        libro_form = LibroForm(prefix='libro')
        revista_form = RevistaForm(prefix='revista')
        periodico_form = PeriodicoForm(prefix='periodico')
    return render(request, 'insertar.html', {
        'libro_form': libro_form,
        'revista_form': revista_form,
        'periodico_form': periodico_form
    })

def buscar(request):
    resultados = []
    if request.method == 'GET':
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            libros = Libro.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
            revistas = Revista.objects.filter(Q(titulo__icontains=query) | Q(editorial__icontains=query))
            periodicos = Periodico.objects.filter(Q(titulo__icontains=query) | Q(editor__icontains=query))
            resultados = {
                'Libros': libros,
                'Revistas': revistas,
                'Periodicos': periodicos
            }
    else:
        form = BuscarForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})