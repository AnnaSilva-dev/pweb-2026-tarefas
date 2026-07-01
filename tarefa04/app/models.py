from django.db import models

class Tarefa(models.Model):
    STATUS = [
        ('P', 'Pendente'),
        ('A', 'Em andamento'),
        ('C', 'Concluída'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS, default='P')
    prazo = models.DateTimeField()


    def __str__(self):
        return self.nome