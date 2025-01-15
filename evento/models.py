from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    tags_choices = (
        ('V', 'Viagem'),
        ('T', 'Trabalho')
    )

    titulo = models.CharField(max_length=100)
    tags = models.TextField()
    pessoas = models.ManyToManyField(Pessoa)
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
