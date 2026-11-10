from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_view, logout_view, recuperar_senha

urlpatterns = [
    # Painel Administrativo
    path('admin/', admin.site.urls),

    # Autenticação (Login / Logout / Recuperar Senha)
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('recuperar-senha/', recuperar_senha, name='recuperar_senha'),
    path('usuarios/', include('usuarios.urls')),

    # Apps do Sistema
    path('administracao/', include('administracao.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('principal/', include('principal.urls')),

    # Cardápio na Raiz (carrega os alimentos na home '/')
    path('', include('cardapio.urls')),
]