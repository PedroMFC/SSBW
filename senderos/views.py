from django.shortcuts import render, HttpResponse
from .models import Excursión

# Create your views here.
#def index(request):
#    return HttpResponse('Hola, desde index')

def index(request):
    context = {
        'saludo': 'Buenas tardes',
        'excursiones': Excursión.objects.all()
    }
    return render(request, 'senderos/index.html', context)

def buscar(request):
    busqueda = request.POST.get('busqueda','')
    print(busqueda)
    context = {
        'buscado': busqueda,
        'excursiones': Excursión.objects.all()
    }
    return render(request, 'senderos/index.html', context)
