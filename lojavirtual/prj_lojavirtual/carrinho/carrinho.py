from decimal import Decimal
from django.conf import settings
from main.models import Produto


class Carrinho:
    def __init__(self, request):
        """Inicializa o carrinho usando a sessão do usuário."""
        self.__sessao = request.session
        carrinho = self.__sessao.get(settings.ID_CARRINHO)
        if not carrinho:
            carrinho = self.__sessao[settings.ID_CARRINHO] = {}
        self.__carrinho = carrinho

    def adicionar(self, produto, quantidade=1, atualizar_quantidade=False):
        """Adiciona um produto ao carrinho ou atualiza sua quantidade."""
        id_produto = str(produto.id)
        if id_produto not in self.__carrinho:
            self.__carrinho[id_produto] = {
                'quantidade': 0,
                'preco': str(produto.preco),
            }
        if atualizar_quantidade:
            self.__carrinho[id_produto]['quantidade'] = quantidade
        else:
            self.__carrinho[id_produto]['quantidade'] += quantidade
        self.__salvar() 
    
    def __salvar(self):
        """Marca a sessão como modificada para que o Django salve."""
        self.__sessao[settings.ID_CARRINHO] = self.__carrinho
        self.__sessao.modified = True

    def remover(self, produto):
        """Remove um produto do carrinho."""
        id_produto = str(produto.id)
        if id_produto in self.__carrinho:
            del self.__carrinho[id_produto]
            self.__salvar()

    def __iter__(self):
        """Itera sobre os itens do carrinho, adicionando os produtos do banco de dados."""
        ids_produtos = self.__carrinho.keys()
        produtos = Produto.objects.filter(id__in=ids_produtos)
        carrinho = self.__carrinho.copy()

        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto

        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['subtotal'] = item['preco'] * item['quantidade']
            yield item

    def __len__(self):
        resultado = 0
        for item in self.__carrinho.values():
            resultado += item['quantidade']
        return resultado
        
    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.__carrinho.values():
            subtotal = Decimal(item['quantidade']) * Decimal(item['preco'])
            resultado = resultado + subtotal
        return resultado
        
    def limpar_carrinho(self):
        """Limpa todos os itens do carrinho."""
        if settings.ID_CARRINHO in self.__sessao:
            del self.__sessao[settings.ID_CARRINHO]
        self.__sessao.modified = True
        
        # def limpar_carrinho(self):
        #     for key in request.session.keys():
        #         del request .session[key]
        #     request.session.modified = True

    # def __len__(self):
    #     """Retorna o total de itens no carrinho."""
    #     return sum(item['quantidade'] for item in self.carrinho.values())

    # def get_total_geral(self):
    #     """Calcula o valor total do carrinho."""
    #     return sum(
    #         Decimal(item['preco']) * item['quantidade']
    #         for item in self.__carrinho.values()
    #     )

    # def limpar_carrinho(self):
    #     """Limpa todos os itens do carrinho."""
    #     if settings.ID_CARRINHO in self.sessao:
    #         del self.sessao[settings.ID_CARRINHO]
    #     self.sessao.modified = True
