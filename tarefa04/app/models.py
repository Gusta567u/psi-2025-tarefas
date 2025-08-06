from django.db import models

class Status(models.TextChoices):
    concluido = "Concluído"
    n_concluido = "Não Concluído"


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(
        choices=Status.choices,
        default=Status.n_concluido,
    )
    prazo = models.DateField()
    atraso = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

