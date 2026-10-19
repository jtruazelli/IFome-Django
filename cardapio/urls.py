from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tabela/', views.tabela, name='tabela'),
    path('tabela/index', views.tabela, name='tabela'),
    path('', ('cardapio.urls')),
]