from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .models import Avaliacao

def pagina_avaliacoes(request):
    # Obtém a data local de hoje
    hoje = timezone.localdate()
    inicio_dia = timezone.make_aware(datetime.datetime.combine(hoje, datetime.time.min))
    fim_dia = timezone.make_aware(datetime.datetime.combine(hoje, datetime.time.max))

    # 1. Mensagens de Carinho (tipo '2')
    mensagens_carinho = Avaliacao.objects.filter(tipo='2').order_by('-data_criacao')[:10]

    # 2. Avaliações do Cardápio do Dia (tipo '1') enviadas HOJE
    avaliacoes_hoje = Avaliacao.objects.filter(
        tipo='1',
        data_criacao__range=(inicio_dia, fim_dia)
    ).order_by('-data_criacao')

    # Mantemos 'avaliacoes_hoje' e 'avaliacoes_cardapio' para garantir compatibilidade total no template
    context = {
        'mensagens_carinho': mensagens_carinho,
        'avaliacoes_hoje': avaliacoes_hoje,
        'avaliacoes_cardapio': avaliacoes_hoje,
    }
    return render(request, 'avaliacoes/avaliacoes.html', context)


def cadastrar_avaliacao(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        mensagem = request.POST.get('mensagem', '').strip()
        nota = request.POST.get('nota')

        # Verifica se o tipo é válido
        if tipo not in ['1', '2']:
            return render(
                request,
                'avaliacoes/cadastroAvaliacoes.html',
                {'erro': 'Tipo de avaliação inválido.'}
            )

        # Verifica se a mensagem foi preenchida
        if not mensagem:
            return render(
                request,
                'avaliacoes/cadastroAvaliacoes.html',
                {'erro': 'Escreva uma mensagem antes de publicar.'}
            )

        # Valida a nota
        try:
            nota = int(nota)
            if nota < 1 or nota > 5:
                raise ValueError
        except (ValueError, TypeError):
            return render(
                request,
                'avaliacoes/cadastroAvaliacoes.html',
                {'erro': 'Selecione uma nota de 1 a 5 estrelas.'}
            )

        # Identifica o autor
        if request.user.is_authenticated:
            autor = request.user.first_name or request.user.username
        else:
            autor = 'Anônimo'

        # Salva a avaliação
        Avaliacao.objects.create(
            nome_autor=autor,
            tipo=tipo,
            mensagem=mensagem,
            nota=nota
        )

        return redirect('pagina_avaliacoes')

    return render(request, 'avaliacoes/cadastroAvaliacoes.html')


def mensagens_carinho(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem', '').strip()

        if mensagem:
            if request.user.is_authenticated:
                autor = request.user.first_name or request.user.username
            else:
                autor = 'Anônimo'

            Avaliacao.objects.create(
                nome_autor=autor,
                tipo='2',
                mensagem=mensagem,
                nota=1
            )

            return redirect('pagina_avaliacoes')

        return render(
            request,
            'avaliacoes/mensagemCarinho.html',
            {'erro': 'Escreva uma mensagem antes de publicar.'}
        )

    return render(
        request,
        'avaliacoes/mensagemCarinho.html'
    )