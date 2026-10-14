from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('cardapio/editar/', views.editar_cardapio, name='editar_cardapio'),
    path('cardapio/novo/', views.novo_cardapio, name='novo_cardapio'),
    path('cardapio/importar/', views.importar_cardapio, name='importar_cardapio'),
    path('comentarios/', views.resumo_comentarios, name='resumo_comentarios'),
]