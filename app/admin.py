from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Libro, Revista, Periodico

admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Periodico)
