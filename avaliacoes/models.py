from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Avaliacao(models.Model):
    TIPO_CHOICES = [
        ('1', 'Cardápio do Dia'),
        ('2', 'Mensagem de Carinho'),
    ]

    nome_autor = models.CharField(max_length=100, default='Anônimo', verbose_name="Nome do Autor")
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, verbose_name="Tipo de Avaliação")
    mensagem = models.TextField(verbose_name="Mensagem")
    nota = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Nota (Estrelas)"
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['-data_criacao'] # Traz as mais recentes primeiro

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nome_autor} ({self.data_criacao.strftime('%d/%m/%Y')})"