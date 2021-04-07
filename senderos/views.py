import os
from django.shortcuts import render, HttpResponse, redirect
from .models import Excursión, Fotos
from .forms import ExcursiónForm
from django.contrib import messages
from django.conf import settings
from django import forms

from mongoengine.queryset.visitor import Q 

# Create your views here.
#def index(request):
#    return HttpResponse('Hola, desde index')

IMAGE_DIR = os.path.join('static', 'imgs', 'senderos')

def index(request):
    context = {
        'saludo': 'Buenas tardes',
        'excursiones': Excursión.objects.all(),
        'form': ExcursiónForm(),
    }
    return render(request, 'senderos/index.html', context)

def buscar(request):
    busqueda = request.POST.get('busqueda','')
    print(busqueda)
    context = {
        'buscado': busqueda,
        'excursiones': Excursión.objects(Q(nombre__icontains=busqueda) | Q(descripción__icontains=busqueda))
    }
    return render(request, 'senderos/index.html', context)

def info(request, id):
    e = Excursión.objects.get(id=id)
    form = ExcursiónForm({'nombre': e.nombre, 'descripción':e.descripción})
    context = {
        'buscado': id,
        'e': e,
        'form': form
    }

    return render(request, 'senderos/info.html', context)

def borrar(request, id):
    Excursión.objects.get(id=id).delete()

    messages.add_message(request, messages.ERROR, 'Excursión borrada')

    return redirect('index')


def SaveFiles(id, files, e, input_d):
    dire = os.path.join(IMAGE_DIR, id)

    try:
        print("HACIENDO TRY")
        if not os.path.isdir(dire):
            os.mkdir(dire)
        file_n = os.path.join(dire, str(files['foto']))
        print('Direccion: ', file_n)
        with open(file_n, 'wb+') as dest:
            for chunk in files['foto'].chunks():
                dest.write(chunk)
        e.fotos=[Fotos(pie=input_d.get('pie'), file="/imgs/senderos/"+id+"/"+input_d.get('foto').name)]
        e.save()

    except OSError as error:
        print('************ ALGO SALIÓ MAL', error)


def editar(request, id):

    if request.method == 'POST':
        form = ExcursiónForm(request.POST, request.FILES)

        if form.is_valid():
            e = Excursión.objects.get(id=id)
            input_d = form.cleaned_data
            files = request.FILES
            e. nombre = input_d['nombre']
            e.descripción = input_d['descripción']
            e.save()

            if len(files) > 0:
                SaveFiles(id, files, e, input_d)

            messages.add_message(request, messages.INFO, 'Excursión editada')
        else:
            messages.add_message(request, messages.WARNING, 'Problemas')

    return redirect('index')


def añadir(request):
    if request.method == 'POST':
        form = ExcursiónForm(request.POST, request.FILES)

        if form.is_valid():
            input_d = form.cleaned_data
            files = request.FILES
            
            reg = Excursión(nombre=input_d['nombre'], descripción=input_d['descripción']).save()
            print('Files:\n', files, '\n')

            if len(files) > 0:
                print('Input:\n', input_d, '\n', input_d.get('foto').name)
                SaveFiles(str(reg.id), files, reg, input_d)

            messages.add_message(request, messages.INFO, 'Excursión añadida')
        else:
            print('n', form.errors, '\n')
            messages.add_message(request, messages.ERROR, form.errors)

    #return render(request, 'senderos/añadir.html', context)
    return redirect('index')