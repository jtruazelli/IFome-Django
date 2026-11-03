from django.shortcuts import render
from django.db.models import Avg, Count
from avaliacoes.models import Avaliacao


# Create your views here.
def dashboard(request):
    # 1. Avaliações do Cardápio (tipo '1')
    avaliacoes_cardapio = Avaliacao.objects.filter(tipo='1')

    # 2. Média Geral das notas do cardápio
    media_dict = avaliacoes_cardapio.aggregate(Avg('nota'))
    media_avaliacoes = round(media_dict['nota__avg'], 1) if media_dict['nota__avg'] else 0.0

    # 3. Total Geral de registros (Avaliações + Mensagens de Carinho)
    total_comentarios = Avaliacao.objects.count()

    # 4. Busca os 5 registros mais recentes
    ultimos_comentarios = list(Avaliacao.objects.order_by('-data_criacao')[:5])

    # Passa EXATAMENTE as variáveis esperadas pelo dashboard.html
    context = {
        'media_avaliacoes': media_avaliacoes,
        'total_comentarios': total_comentarios,
        'ultimos_comentarios': ultimos_comentarios,
    }
    return render(request, 'adm/dashboard.html', context)


def cardapio(request):
    return render(request, 'adm/cardapio.html')


def editar_cardapio(request):
    return render(request, 'adm/editar_cardapio.html')


def novo_cardapio(request):
    return render(request, 'adm/novo_cardapio.html')


def importar_cardapio(request):
    return render(request, 'adm/importar_cardapio.html')


def resumo_comentarios(request):
    avaliacoes = Avaliacao.objects.filter(tipo='1')

    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    nota = request.GET.get('nota')

    if inicio:
        avaliacoes = avaliacoes.filter(data_criacao__date__gte=inicio)
    if fim:
        avaliacoes = avaliacoes.filter(data_criacao__date__lte=fim)
    if nota:
        avaliacoes = avaliacoes.filter(nota=nota)

    total_avaliacoes = avaliacoes.count()

    media_dict = avaliacoes.aggregate(Avg('nota'))
    media_avaliacao = round(media_dict['nota__avg'] or 0, 1)

    contagem_raw = avaliacoes.values('nota').annotate(total=Count('nota'))
    contagem_notas = {item['nota']: item['total'] for item in contagem_raw}

    distribuicao = []
    for estrela in range(5, 0, -1):
        qtd = contagem_notas.get(estrela, 0)
        porcentagem = (qtd / total_avaliacoes * 100) if total_avaliacoes > 0 else 0
        distribuicao.append({
            'estrela': estrela,
            'quantidade': qtd,
            'porcentagem': round(porcentagem, 1)
        })

    mensagens_carinho = Avaliacao.objects.filter(tipo='2').order_by('-data_criacao')

    context = {
        'avaliacoes': avaliacoes.order_by('-data_criacao'),
        'mensagens_carinho': mensagens_carinho,
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacao': media_avaliacao,
        'distribuicao': distribuicao,
    }
    return render(request, 'adm/resumo_comentarios.html', context)