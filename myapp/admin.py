from django.contrib import admin
from .models import ElegirRespuesta, Pregunta



# Register your models here.
class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto', ]
    search_fields = ['texto', "preguntas__texto"]


admin.site.register(ElegirRespuesta)
admin.site.register(Pregunta, PreguntaAdmin)
