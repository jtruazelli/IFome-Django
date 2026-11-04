from django.db import models

class Avaliacao(models.Model):
    TIPO_CHOICES = [
        ('1', 'Cardápio do Dia'),
        ('2', 'Mensagem de Carinho'),
    ]

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='1')
    nota = models.IntegerField(default=5)
    mensagem = models.TextField(blank=True, null=True)
    nome_autor = models.CharField(max_length=100, default='Anônimo')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nome_autor}"