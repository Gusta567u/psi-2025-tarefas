from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("nome", "status", "prazo")
    exclude = ('atraso',)
    search_fields = ("nome",)
