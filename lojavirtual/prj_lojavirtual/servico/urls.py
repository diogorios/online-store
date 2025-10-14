from django.urls import path
from django.views.generic import TemplateView
from . import views 

app_name='servico'

urlpatterns = [
    path('', views.listar_servicos, name='listar_servicos'),
    path('<str:slug_prestador>/', views.listar_servicos, name='listar_servicos_por_prestador'),
    path('<int:id>/<str:slug_servico>/', views.detalhes_servico, name='detalhes_servico'),
]