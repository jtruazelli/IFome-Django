from django.urls import path
from . import views

urlpatterns = [
    path('mural/', views.pagina_mural, name='pagina_mural'),
]