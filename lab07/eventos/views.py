from django.shortcuts import render, redirect
from .models import Evento


def crear_evento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        descripcion = request.POST.get('descripcion')
        
        Evento.objects.create(nombre=nombre, fecha=fecha, hora=hora, lugar=lugar, descripcion=descripcion)
        return redirect('lista_eventos')

    return render(request, 'crea_evento.html')

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def actualizar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':
        evento.nombre = request.POST.get('nombre')
        evento.fecha = request.POST.get('fecha')
        evento.hora = request.POST.get('hora')
        evento.lugar = request.POST.get('lugar')
        evento.descripcion = request.POST.get('descripcion')
        evento.save()
        return redirect('lista_eventos')

    return render(request, 'actualiza_evento.html', {'evento': evento})

def eliminar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')

    return render(request, 'elimina_evento.html', {'evento': evento})