from django.db import models
class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=255,default='')
    email = models.EmailField(default='')
    eventos = models.ManyToManyField(Evento, through='RegistroEvento')
    def __str__(self):
        return self.nombre


class RegistroEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.evento.nombre + " - " + self.usuario.nombre
