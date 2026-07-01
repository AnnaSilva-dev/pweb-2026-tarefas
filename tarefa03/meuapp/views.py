from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    usuarios = [
        {"nome": "Maria Matilde", "matricula": "2021001", "idade": 20, "cidade": "Natal"},
        {"nome": "João Silva", "matricula": "2021002", "idade": 22, "cidade": "Natal"},
        {"nome": "Ana Souza", "matricula": "2021003", "idade": 19, "cidade": "São Paulo do Potengi"},
        {"nome": "Pedro Oliveira", "matricula": "2021004", "idade": 21, "cidade": "São Paulo do Potengi"},
        {"nome": "Carla Santos", "matricula": "2021005", "idade": 23, "cidade": "São Paulo do Potengi"},
    ]
    lista_usuarios = {"usuarios": usuarios}
    return render(request, "usuarios.html", lista_usuarios)
