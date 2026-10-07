from django.shortcuts import render, redirect
from .models import Avaliacao

def pagina_avaliacoes(request):
    mensagens_carinho = Avaliacao.objects.filter(tipo='2')
    avaliacoes_cardapio = Avaliacao.objects.filter(tipo='1')

    context = {
        'mensagens_carinho': mensagens_carinho,
        'avaliacoes_cardapio': avaliacoes_cardapio,
    }
    # Altera de 'avaliacoes.html' para 'avaliacoes/avaliacoes.html'
    return render(request, 'avaliacoes/avaliacoes.html', context)


def cadastrar_avaliacao(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        mensagem = request.POST.get('mensagem')
        nota = request.POST.get('nota', 1)

        autor = request.user.first_name or request.user.username if request.user.is_authenticated else 'Anónimo'

        Avaliacao.objects.create(
            nome_autor=autor,
            tipo=tipo,
            mensagem=mensagem,
            nota=int(nota)
        )

        return redirect('pagina_avaliacoes')

    # Altera de 'cadastroAvaliacoes.html' para 'avaliacoes/cadastroAvaliacoes.html'
    return render(request, 'avaliacoes/cadastroAvaliacoes.html')