from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cardapios/', views.lista_cardapios, name='cardapio'),
    path('cardapios/novo/', views.novo_cardapio, name='novo_cardapio'),
    path('cardapios/<int:pk>/editar/', views.editar_cardapio, name='editar_cardapio'),
    path('cardapios/<int:pk>/excluir/', views.excluir_cardapio, name='excluir_cardapio'),
    path('importar/', views.importar_cardapio, name='importar_cardapio'),
    path('comentarios/', views.resumo_comentarios, name='resumo_comentarios'),
]