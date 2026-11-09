from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils.timezone import localdate
from django.contrib.auth.decorators import login_required

from avaliacoes.models import Avaliacao
from cardapio.models import Cardapio
from .forms import CardapioForm


@login_required
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


@login_required
def lista_cardapios(request):
    hoje = localdate()
    cardapios = Cardapio.objects.order_by('-data')

    # Busca o cardápio de hoje (ou o mais recente) para o destaque no topo
    cardapio_hoje = Cardapio.objects.filter(data=hoje).first()
    if not cardapio_hoje:
        cardapio_hoje = Cardapio.objects.order_by('-data').first()

    # Processamento dos filtros GET
    inicio = request.GET.get('inicio', '').strip()
    fim = request.GET.get('fim', '').strip()
    refeicao = request.GET.get('refeicao', '').strip()

    if inicio:
        cardapios = cardapios.filter(data__gte=inicio)
    if fim:
        cardapios = cardapios.filter(data__lte=fim)

    if refeicao:
        if refeicao == 'lanche_manha':
            cardapios = cardapios.exclude(refeicao_manha__exact='').exclude(refeicao_manha__isnull=True)
        elif refeicao == 'almoco':
            cardapios = cardapios.exclude(refeicao_almoco__exact='').exclude(refeicao_almoco__isnull=True)
        elif refeicao == 'lanche_tarde':
            cardapios = cardapios.exclude(refeicao_tarde__exact='').exclude(refeicao_tarde__isnull=True)

    context = {
        'hoje': hoje,
        'cardapio_hoje': cardapio_hoje,
        'cardapios': cardapios,
    }
    return render(request, 'adm/cardapio.html', context)


@login_required
def novo_cardapio(request):
    if request.method == 'POST':
        data_input = request.POST.get('data')
        instancia_existente = Cardapio.objects.filter(data=data_input).first() if data_input else None

        if instancia_existente:
            form = CardapioForm(request.POST, instance=instancia_existente)
        else:
            form = CardapioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('administracao:cardapio')
    else:
        form = CardapioForm()

    return render(request, 'adm/novo_cardapio.html', {'form': form})


@login_required
def editar_cardapio(request, pk):
    cardapio = get_object_or_404(Cardapio, pk=pk)
    if request.method == 'POST':
        form = CardapioForm(request.POST, instance=cardapio)
        if form.is_valid():
            form.save()
            return redirect('administracao:cardapio')
    else:
        form = CardapioForm(instance=cardapio)

    return render(request, 'adm/editar_cardapio.html', {'form': form, 'cardapio': cardapio})


@login_required
@require_POST
def excluir_cardapio(request, pk):
    cardapio = get_object_or_404(Cardapio, pk=pk)
    cardapio.delete()
    return redirect('administracao:cardapio')


@login_required
def importar_cardapio(request):
    ultimos_3_cardapios = Cardapio.objects.order_by('-data')[:3]
    todos_cardapios = Cardapio.objects.order_by('-data')

    context = {
        'ultimos_3_cardapios': ultimos_3_cardapios,
        'todos_cardapios': todos_cardapios,
        'hoje': localdate(),
    }
    return render(request, 'adm/importar_cardapio.html', context)


@login_required
def resumo_comentarios(request):
    # 1. Avaliações do Cardápio (tipo '1' com notas de 1 a 5 estrelas)
    avaliacoes = Avaliacao.objects.filter(tipo='1').order_by('-data_criacao')
    total_avaliacoes = avaliacoes.count()

    # Média Geral das Notas
    media_dict = avaliacoes.aggregate(Avg('nota'))
    media_avaliacao = round(media_dict['nota__avg'] or 0, 1) if total_avaliacoes > 0 else 0.0

    # Distribuição por estrela (5 a 1)
    contagem_raw = avaliacoes.values('nota').annotate(total=Count('nota'))
    contagem_notas = {}
    for item in contagem_raw:
        if item['nota'] is not None:
            nota_int = int(item['nota'])
            contagem_notas[nota_int] = contagem_notas.get(nota_int, 0) + item['total']

    distribuicao = []
    for estrela in range(5, 0, -1):
        qtd = contagem_notas.get(estrela, 0)
        porcentagem = (qtd / total_avaliacoes * 100) if total_avaliacoes > 0 else 0
        distribuicao.append({
            'estrela': estrela,
            'quantidade': qtd,
            'porcentagem_css': str(round(porcentagem, 1)).replace(',', '.')
        })

    # 2. Mensagens de Carinho (tipo '2')
    mensagens_carinho = Avaliacao.objects.filter(tipo='2').order_by('-data_criacao')
    total_mensagens_carinho = mensagens_carinho.count()

    context = {
        'avaliacoes': avaliacoes,
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacao': media_avaliacao,
        'distribuicao': distribuicao,
        'mensagens_carinho': mensagens_carinho,
        'total_mensagens_carinho': total_mensagens_carinho,
    }

    return render(request, 'adm/resumo_comentarios.html', context)


@login_required
@require_POST
def excluir_comentario(request, pk):
    comentario = get_object_or_404(Avaliacao, pk=pk)
    comentario.delete()
    return redirect('administracao:resumo_comentarios')