from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display=('titulo','data_evento','data_criacao', 'usuario',)#definir o que eu quero que apareça ao lado de cada item na tabela
    list_filter = ( 'data_evento', 'usuario',)


# Register your models here.
admin.site.register(Evento, EventoAdmin)