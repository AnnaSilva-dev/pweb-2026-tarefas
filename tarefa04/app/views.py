from django.shortcuts import render
from .models import Tarefa
from datetime import date

def index(request):
    return render(request, "index.html")

def tarefas(request):
    tarefas = Tarefa.objects.all()

    context = {
        "tarefas": tarefas,
        "hoje": date.today()
    }
    return render(request, "tarefas.html", context)