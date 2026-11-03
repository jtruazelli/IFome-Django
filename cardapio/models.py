from django.db import models

# Create your models here.
from django.db import models

class Alergenico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class TabelaNutricional(models.Model):
    calorias = models.FloatField(help_text="Valor em kcal", default=0)
    carboidratos = models.FloatField(help_text="Valor em gramas (g)", default=0)
    proteinas = models.FloatField(help_text="Valor em gramas (g)", default=0)
    gorduras = models.FloatField(help_text="Valor em gramas (g)", default=0)
    fibras = models.FloatField(help_text="Valor em gramas (g)", default=0)
    sodio = models.FloatField(help_text="Valor em miligramas (mg)", default=0)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Nutrientes ({self.calorias} kcal)"

class Alimento(models.Model):
    TURNO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('ALMOCO', 'Almoço'),
        ('TARDE', 'Tarde'),
    ]

    nome = models.CharField(max_length=150)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, default='ALMOCO')
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)
    alergenicos = models.ManyToManyField(Alergenico, blank=True)
    tabela_nutricional = models.OneToOneField(
        TabelaNutricional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nome} ({self.get_turno_display()})"

class Cardapio(models.Model):
    data = models.DateField(unique=True)
    alimentos = models.ManyToManyField(Alimento, related_name='cardapios')

    def __str__(self):
        return f"Cardápio do dia {self.data.strftime('%d/%m/%Y')}"
