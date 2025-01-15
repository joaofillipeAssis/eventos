from django.urls import path
from . import views

urlpatterns = [
    # suburl vazia 
    path('', views.home),
    path('escrever/', views.escrever, name='escrever'),
    path('pessoa/cadastro/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
]