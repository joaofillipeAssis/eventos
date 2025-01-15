from django.shortcuts import render
from django.http import HttpResponse

#transfora html em arquivo para ser executado

def home(request):
    return render(request, 'home.html') 

def escrever(request):
    if request.method == 'GET':
        return render(request, 'escrever.html')
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo'),
        tags = request.POST.getlist('tags'),
        pessoas = request.POST.getlist('pessoas'),
        texto = request.POST.get('texto')

        return HttpResponse(f'{titulo} + {tags} + {pessoas} + {texto}')