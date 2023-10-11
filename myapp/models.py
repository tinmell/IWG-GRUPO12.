from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto = models.TextField(verbose_name='Texto de la pregunta')
    def __str__(self):
        return self.texto
    
#preguntya correcta
class ElegirRespuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='correcta?', default=False, null = False)
    texto = models.TextField(verbose_name='texto respuesta')
    def __str__(self):
        return self.texto

