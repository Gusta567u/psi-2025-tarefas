from django.shortcuts import render, get_list_or_404
from datetime import date
from .models import Tarefa, Status


def index(request):
    
    data = date.today()
    tarefas = get_list_or_404(Tarefa)
    context = {
        'tarefas':tarefas
    }

    for i in tarefas:
        if i.status == Status.concluido:
            i.atraso = "Já foi realizado"
        else:
            if data > i.prazo:
                i.atraso = "Tarefa atrasada"
            else:
                i.atraso = "Dentro do prazo"


    return render(request, "app/index.html", context)