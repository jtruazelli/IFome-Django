from django.urls import path
from . import views

urlpatterns = [
    path('mural/', views.pagina_avaliacoes, name='pagina_avaliacoes'),
    path('cadastrar/', views.cadastrar_avaliacao, name='cadastrar_avaliacao'),
]