from django.db import models


class Cardapio(models.Model):
    data = models.DateField(unique=True)

    refeicao_manha = models.TextField(
        verbose_name="Manhã",
        blank=True,
        null=True
    )

    refeicao_almoco = models.TextField(
        verbose_name="Almoço",
        blank=True,
        null=True
    )

    refeicao_tarde = models.TextField(
        verbose_name="Tarde",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Cardápio de {self.data.strftime('%d/%m/%Y')}"