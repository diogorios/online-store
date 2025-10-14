"""
URL configuration for lojavirtual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('ajuda/', TemplateView.as_view(template_name='ajuda.html'), name='ajuda'),
    path('fale-conosco/', views.ViewFaleConosco.as_view(), name='fale_conosco'),
    path('carrinho/', include('carrinho.urls',namespace='carrinho')),
    path('pedidos/', include('pedidos.urls',namespace='pedidos')),
    path('servicos/', include(('servico.urls', 'servico'), namespace='servico')),
    #path('', include('main.urls',namespace='main')),
    path('', include(('main.urls', 'main'), namespace='main')),
]

# aqui você concatena corretamente
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)