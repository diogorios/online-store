from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms
from django .shortcuts import render, get_object_or_404
from .models import PrestadorServico, Servico
from servico.forms import FormAdicionarServicoAoCarrinho
    
def listar_servicos(request, slug_prestador=None):
    prestador = None
    lista_prestadores = PrestadorServico.objects.all()
    lista_servicos = Servico.objects.all()

    if slug_prestador:
        prestador = get_object_or_404(PrestadorServico, slug=slug_prestador)
        lista_servicos = Servico.objects.filter(PrestadorServico=prestador)

    contexto = {
        'prestador': prestador,
        'lista_prestadores': lista_prestadores,
        'lista_servicos': lista_servicos,
    }

    return render(request,'servico/listar_servico.html', contexto)
    
def detalhes_servico(request, id, slug_servico):
    servico = get_object_or_404(Servico, id = id,
                                 slug=slug_servico)
    
    form_adicionar_servico_ao_carrinho = FormAdicionarServicoAoCarrinho
    contexto = {
            'servico': servico,
            'form_servico_carrinho': servico, 'form_servico_carrinho': form_adicionar_servico_ao_carrinho,
        }
    
    return render(request,'servico/detalhes_servico.html', contexto)