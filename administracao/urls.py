from django.urls import path
from . import views

app_name = 'administracao'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cardapios/', views.lista_cardapios, name='cardapio'),
    path('cardapios/novo/', views.novo_cardapio, name='novo_cardapio'),
    path('cardapios/<int:pk>/editar/', views.editar_cardapio, name='editar_cardapio'),
    path('cardapios/<int:pk>/excluir/', views.excluir_cardapio, name='excluir_cardapio'),
    path('importar/', views.importar_cardapio, name='importar_cardapio'),
    path('comentarios/', views.resumo_comentarios, name='resumo_comentarios'),
    path('comentarios/<int:pk>/excluir/', views.excluir_comentario, name='excluir_comentario'),
]