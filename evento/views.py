from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa


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

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome'),
        foto = request.POST.get('foto')

    pessoa = Pessoa(
        nome=nome,
        foto=foto
    )
    
    pessoa.save()
    return redirect('escrever')