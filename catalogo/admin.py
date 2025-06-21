from django.contrib import admin

from catalogo.models import Autor, EjemplarLibro, Genero, Libro

# Register your models here.
admin.site.site_header = "Sistema de Biblioteca"
admin.site.index_title = "Administración del Sistema de Biblioteca"
admin.site.site_title = "Biblioteca Admin"
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(EjemplarLibro)