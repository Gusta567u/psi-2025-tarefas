from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
        {"nome": "João Pedro", "matricula": "0000", "idade": 17, "cidade": "Riachuelo"},
        {"nome": "Gustavo", "matricula": "1111", "idade": 16, "cidade": "São Paulo do Potengi"},
        {"nome": "Pierre", "matricula": "2222", "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "João", "matricula": "3333", "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Danilo", "matricula": "4444", "idade": 18, "cidade": "Boa Saúde"},
    ]

    context = {
        "usuarios": user_list,
    }
    return render(request, "usuarios.html", context)