from django.shortcuts import render
from django.http import HttpResponse

#transfora html em arquivo para ser executado

def home(request):
    return render(request, 'home.html') 

def escrever(request):
    return render(request, 'escrever.html') 