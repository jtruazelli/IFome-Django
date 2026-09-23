from django.shortcuts import render

# Quando essa função for chamada, vai mostrar a página login.html
def login_view(request):
    return render(request, 'usuarios/login.html')