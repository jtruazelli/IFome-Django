from django.shortcuts import render
from django.utils.timezone import localdate
from .models import Cardapio, Alimento

def index(request):
    # Busca o cardápio da data atual ou o mais recente cadastrado
    hoje = localdate()
    cardapio = Cardapio.objects.filter(data=hoje).first()
    if not cardapio:
        cardapio = Cardapio.objects.order_by('-data').first()

    context = {
        'cardapio': cardapio,
        'alimentos_manha': cardapio.alimentos.filter(turno='MANHA') if cardapio else [],
        'alimentos_almoco': cardapio.alimentos.filter(turno='ALMOCO') if cardapio else [],
        'alimentos_tarde': cardapio.alimentos.filter(turno='TARDE') if cardapio else [],
    }
    return render(request, 'index.html', context)

def tabela(request):
    # Lista alimentos organizados por turno
    alimentos_manha = Alimento.objects.filter(turno='MANHA').prefetch_related('ingredientes', 'alergenicos', 'tabela_nutricional')
    alimentos_almoco = Alimento.objects.filter(turno='ALMOCO').prefetch_related('ingredientes', 'alergenicos', 'tabela_nutricional')
    alimentos_tarde = Alimento.objects.filter(turno='TARDE').prefetch_related('ingredientes', 'alergenicos', 'tabela_nutricional')

    context = {
        'alimentos_manha': alimentos_manha,
        'alimentos_almoco': alimentos_almoco,
        'alimentos_tarde': alimentos_tarde,
    }
    return render(request, 'tabela.html', context)