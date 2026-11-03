from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_avaliacoes, name='pagina_avaliacoes'),
    path('cadastrar/', views.cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('mensagem-carinho/', views.mensagens_carinho, name='mensagem_carinho'),
]