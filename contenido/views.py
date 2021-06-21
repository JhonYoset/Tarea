import contenido
from django.shortcuts import render

from .models import Contenido

def index(request):
    contenidos = Contenido.objects.all()
    return render(request, 'blog/index.html', {'contenidos': contenidos})

def detail(request, pk):
    contenido = Contenido.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'contenido': contenido})