from django.shortcuts import render
from django.utils.timezone import localdate
from .models import Cardapio

def index(request):
    hoje = localdate()
    # Busca estritamente o cardápio cadastrado para o dia de hoje
    cardapio = Cardapio.objects.filter(data=hoje).first()

    itens_manha = [item.strip() for item in cardapio.refeicao_manha.split('\n') if item.strip()] if cardapio and cardapio.refeicao_manha else []
    itens_almoco = [item.strip() for item in cardapio.refeicao_almoco.split('\n') if item.strip()] if cardapio and cardapio.refeicao_almoco else []
    itens_tarde = [item.strip() for item in cardapio.refeicao_tarde.split('\n') if item.strip()] if cardapio and cardapio.refeicao_tarde else []

    context = {
        'cardapio': cardapio,
        'hoje': hoje,
        'itens_manha': itens_manha,
        'itens_almoco': itens_almoco,
        'itens_tarde': itens_tarde,
    }
    return render(request, 'index.html', context)
