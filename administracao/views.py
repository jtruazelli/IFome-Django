from django.db.models import Avg, Count
from avaliacoes.models import Avaliacao
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils.timezone import localdate
from cardapio.models import Cardapio
from .forms import CardapioForm


def dashboard(request):
    avaliacoes_cardapio = Avaliacao.objects.filter(tipo='1')
    media_dict = avaliacoes_cardapio.aggregate(Avg('nota'))
    media_avaliacoes = round(media_dict['nota__avg'], 1) if media_dict['nota__avg'] else 0.0

    total_comentarios = Avaliacao.objects.count()
    ultimos_comentarios = list(Avaliacao.objects.order_by('-data_criacao')[:5])
    cardapio_atual = Cardapio.objects.order_by('-data').first()

    context = {
        'media_avaliacoes': media_avaliacoes,
        'total_comentarios': total_comentarios,
        'ultimos_comentarios': ultimos_comentarios,
        'cardapio_atual': cardapio_atual,
    }
    return render(request, 'adm/dashboard.html', context)


def lista_cardapios(request):
    hoje = localdate()
    # Busca estritamente o cardápio cadastrado para a data de hoje
    cardapio_hoje = Cardapio.objects.filter(data=hoje).first()

    itens_manha = [item.strip() for item in cardapio_hoje.refeicao_manha.split('\n') if item.strip()] if cardapio_hoje and cardapio_hoje.refeicao_manha else []
    itens_almoco = [item.strip() for item in cardapio_hoje.refeicao_almoco.split('\n') if item.strip()] if cardapio_hoje and cardapio_hoje.refeicao_almoco else []
    itens_tarde = [item.strip() for item in cardapio_hoje.refeicao_tarde.split('\n') if item.strip()] if cardapio_hoje and cardapio_hoje.refeicao_tarde else []

    # Lista completa de históricos para o modal/tabela
    todos_cardapios = Cardapio.objects.order_by('-data')

    context = {
        'hoje': hoje,
        'cardapio': cardapio_hoje,
        'itens_manha': itens_manha,
        'itens_almoco': itens_almoco,
        'itens_tarde': itens_tarde,
        'todos_cardapios': todos_cardapios,
    }
    return render(request, 'adm/cardapio.html', context)


def novo_cardapio(request):
    if request.method == 'POST':
        data_input = request.POST.get('data')
        # Verifica se já existe um cardápio para essa data
        instancia_existente = Cardapio.objects.filter(data=data_input).first() if data_input else None

        if instancia_existente:
            form = CardapioForm(request.POST, instance=instancia_existente)
        else:
            form = CardapioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cardapio')
    else:
        form = CardapioForm()

    return render(request, 'adm/novo_cardapio.html', {'form': form})


def editar_cardapio(request, pk):
    cardapio = get_object_or_404(Cardapio, pk=pk)
    if request.method == 'POST':
        form = CardapioForm(request.POST, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('cardapio')
    else:
        form = CardapioForm(instance=cardapio)

    return render(request, 'adm/editar_cardapio.html', {'form': form, 'cardapio': cardapio})


@require_POST
def excluir_cardapio(request, pk):
    cardapio = get_object_or_404(Cardapio, pk=pk)
    cardapio.delete()
    return redirect('cardapio')


def importar_cardapio(request):
    # Pega os 3 dias mais recentes que possuem cardápio cadastrado
    ultimos_3_cardapios = Cardapio.objects.order_by('-data')[:3]
    todos_cardapios = Cardapio.objects.order_by('-data')

    context = {
        'ultimos_3_cardapios': ultimos_3_cardapios,
        'todos_cardapios': todos_cardapios,
        'hoje': localdate(),
    }
    return render(request, 'adm/importar_cardapio.html', context)


def resumo_comentarios(request):
    # Avaliações do tipo '1' (Cardápio)
    avaliacoes = Avaliacao.objects.filter(tipo='1').order_by('-data_criacao')
    total_avaliacoes = avaliacoes.count()

    # Média Geral
    media_dict = avaliacoes.aggregate(Avg('nota'))
    media_avaliacao = round(media_dict['nota__avg'] or 0, 1) if total_avaliacoes > 0 else 0.0

    # Agrupamento e contagem por nota
    contagem_raw = avaliacoes.values('nota').annotate(total=Count('nota'))

    # O SEGREDO ESTÁ AQUI: int(item['nota']) garante que a chave do dicionário seja sempre um inteiro
    contagem_notas = {}
    for item in contagem_raw:
        if item['nota'] is not None:
            nota_int = int(item['nota'])
            contagem_notas[nota_int] = contagem_notas.get(nota_int, 0) + item['total']

    # Monta a distribuição exata de 5 a 1 estrelas
    distribuicao = []
    for estrela in range(5, 0, -1):
        qtd = contagem_notas.get(estrela, 0)
        porcentagem = (qtd / total_avaliacoes * 100) if total_avaliacoes > 0 else 0
        distribuicao.append({
            'estrela': estrela,
            'quantidade': qtd,
            'porcentagem_css': str(round(porcentagem, 1)).replace(',', '.')
        })

    context = {
        'avaliacoes': avaliacoes,
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacao': media_avaliacao,
        'distribuicao': distribuicao,
    }

    return render(request, 'adm/resumo_comentarios.html', context)