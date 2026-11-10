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
    hoje = localdate()
    cardapio_hoje = Cardapio.objects.filter(data=hoje).first()

    # Avaliações do Cardápio do dia de hoje (tipo '1')
    avaliacoes_hoje = Avaliacao.objects.filter(tipo='1', data_criacao__date=hoje)
    total_avaliacoes_hoje = avaliacoes_hoje.count()

    media_dict_hoje = avaliacoes_hoje.aggregate(Avg('nota'))
    media_hoje = round(media_dict_hoje['nota__avg'], 1) if media_dict_hoje['nota__avg'] else 0.0

    # Média Geral Histórica
    avaliacoes_geral = Avaliacao.objects.filter(tipo='1')
    media_dict_geral = avaliacoes_geral.aggregate(Avg('nota'))
    media_avaliacoes = round(media_dict_geral['nota__avg'], 1) if media_dict_geral['nota__avg'] else 0.0

    total_comentarios = Avaliacao.objects.count()
    ultimos_comentarios = list(Avaliacao.objects.order_by('-data_criacao')[:5])

    # Vincula o cardápio correspondente a cada um dos últimos comentários
    for c in ultimos_comentarios:
        c.cardapio_vinculado = Cardapio.objects.filter(data=c.data_criacao.date()).first()

    cardapio_atual = Cardapio.objects.order_by('-data').first()

    context = {
        'hoje': hoje,
        'cardapio_hoje': cardapio_hoje,
        'media_hoje': media_hoje,
        'total_avaliacoes_hoje': total_avaliacoes_hoje,
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

    cardapio_hoje = Cardapio.objects.filter(data=hoje).first()

    # Trata o salvamento da edição rápida na mesma página
    if request.method == 'POST' and 'salvar_inline' in request.POST:
        if cardapio_hoje:
            form_inline = CardapioForm(request.POST, instance=cardapio_hoje)
        else:
            form_inline = CardapioForm(request.POST)

        if form_inline.is_valid():
            cardapio_salvo = form_inline.save(commit=False)
            cardapio_salvo.data = hoje
            cardapio_salvo.save()
            return redirect('administracao:cardapio')
    else:
        form_inline = CardapioForm(instance=cardapio_hoje, initial={'data': hoje}) if cardapio_hoje else CardapioForm(
            initial={'data': hoje})

    # Filtros por Intervalo de Datas
    inicio = request.GET.get('inicio', '').strip()
    fim = request.GET.get('fim', '').strip()

    if inicio:
        cardapios = cardapios.filter(data__gte=inicio)
    if fim:
        cardapios = cardapios.filter(data__lte=fim)

    # VÍNCULO COM AS AVALIAÇÕES:
    # Para cada cardápio, calcula a média de notas e a quantidade de avaliações do tipo '1' do mesmo dia
    for c in cardapios:
        avaliacoes_do_dia = Avaliacao.objects.filter(
            tipo='1',
            data_criacao__date=c.data
        )
        agregado = avaliacoes_do_dia.aggregate(Avg('nota'), Count('id'))
        media = agregado['nota__avg']

        c.media_avaliacao = round(media, 1) if media is not None else None
        c.qtd_avaliacoes = agregado['id__count'] or 0

    context = {
        'hoje': hoje,
        'cardapio_hoje': cardapio_hoje,
        'cardapios': cardapios,
        'form_inline': form_inline,
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
    # 1. Filtros recebidos via GET
    inicio = request.GET.get('inicio', '').strip()
    fim = request.GET.get('fim', '').strip()
    nota = request.GET.get('nota', '').strip()

    # 2. Avaliações do Cardápio (tipo '1')
    avaliacoes = Avaliacao.objects.filter(tipo='1')

    if inicio:
        avaliacoes = avaliacoes.filter(data_criacao__date__gte=inicio)
    if fim:
        avaliacoes = avaliacoes.filter(data_criacao__date__lte=fim)
    if nota:
        avaliacoes = avaliacoes.filter(nota=nota)

    avaliacoes = avaliacoes.order_by('-data_criacao')
    total_avaliacoes = avaliacoes.count()

    # Média Geral (baseada no filtro atual)
    media_dict = avaliacoes.aggregate(Avg('nota'))
    media_avaliacao = round(media_dict['nota__avg'] or 0, 1) if total_avaliacoes > 0 else 0.0

    # Distribuição de Estrelas (5 a 1)
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

    # Vincula o Cardápio do dia para cada Avaliação da lista
    for a in avaliacoes:
        data_av = a.data_criacao.date()
        a.cardapio_vinculado = Cardapio.objects.filter(data=data_av).first()

    # 3. Mensagens de Carinho (tipo '2')
    mensagens_carinho = Avaliacao.objects.filter(tipo='2')
    if inicio:
        mensagens_carinho = mensagens_carinho.filter(data_criacao__date__gte=inicio)
    if fim:
        mensagens_carinho = mensagens_carinho.filter(data_criacao__date__lte=fim)

    mensagens_carinho = mensagens_carinho.order_by('-data_criacao')
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