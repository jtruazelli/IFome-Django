from django.shortcuts import render


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
    return render(request, 'adm/resumo_comentarios.html')