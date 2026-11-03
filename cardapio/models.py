from django.db import models

class Cardapio(models.Model):
    data = models.DateField(verbose_name="Data do Cardápio")

    class Meta:
        verbose_name = "Cardápio"
        verbose_name_plural = "Cardápios"
        ordering = ['-data']

    def __str__(self):
        return f"Cardápio - {self.data.strftime('%d/%m/%Y')}"


class ItemCardapio(models.Model):
    TURNO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('ALMOCO', 'Almoço'),
        ('TARDE', 'Tarde'),
    ]

    cardapio = models.ForeignKey(
        Cardapio,
        on_delete=models.CASCADE,
        related_name='itens',
        verbose_name="Cardápio"
    )
    turno = models.CharField(
        max_length=10,
        choices=TURNO_CHOICES,
        verbose_name="Turno"
    )
    nome_alimento = models.CharField(
        max_length=150,
        verbose_name="Nome do Alimento"
    )
    ingredientes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Ingredientes Principais"
    )
    alergenicos = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Alergénicos"
    )

    # Informações Nutricionais
    calorias = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Calorias (kcal)"
    )
    carboidratos = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Carboidratos (g)"
    )
    proteinas = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Proteínas (g)"
    )
    gorduras = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Gorduras (g)"
    )
    fibras = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Fibras (g)"
    )
    sodio = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Sódio (mg)"
    )
    observacao_nutricional = models.TextField(
        blank=True, null=True, verbose_name="Observações Nutricionais"
    )

    class Meta:
        verbose_name = "Item do Cardápio"
        verbose_name_plural = "Itens do Cardápio"

    def __str__(self):
        return f"{self.get_turno_display()} - {self.nome_alimento}"