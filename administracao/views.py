from django.shortcuts import render
from django.db.models import Count, Avg
from avaliacoes.models import Avaliacao


# Create your views here.
def dashboard(request):
    return render(request, 'adm/dashboard.html')

def cardapio(request):
    return render(request, 'adm/cardapio.html')

def editar_cardapio(request):
    return render(request, 'adm/editar_cardapio.html')

def novo_cardapio(request):
    return render(request, 'adm/novo_cardapio.html')

def importar_cardapio(request):
    return render(request, 'adm/importar_cardapio.html')


def resumo_comentarios(request):
    avaliacoes = Avaliacao.objects.all()

    # Aplica os filtros recebidos via GET
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

    # Média Geral
    media_dict = avaliacoes.aggregate(Avg('nota'))
    media_avaliacao = round(media_dict['nota__avg'] or 0, 1)

    # Distribuição por Estrelas (1 a 5)
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

    context = {
        'avaliacoes': avaliacoes.order_by('-id'),  # Mais recentes primeiro
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacao': media_avaliacao,
        'distribuicao': distribuicao,
    }

    return render(request, 'adm/resumo_comentarios.html', context)