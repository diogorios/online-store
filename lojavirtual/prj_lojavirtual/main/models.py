from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    # Um slug é uma versão amigável de um texto usada em URLs.
    # Mais organizado e legível que usar um ID (ex: /categoria/comida-brasileira/ ao invés de /categoria/5/);
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    # A Meta é uma classe interna que define metadados do modelo, ou seja, 
    # configurações adicionais que dizem ao Django como o modelo deve se comportar.
    # Categoria.objects.all()  # já virá ordenado por nome
    class Meta:
        ordering = ('nome',) 
        verbose_name = 'categoria', 
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome
    
    # Deixa a URL mais amigável indexa página, usada em mecanismo
    # de busca pelo google - testar
    def get_absolute_url(self):
        return reverse('main:listar_produtos_por_categoria', args=[self.slug])

class Produto(models.Model):
    # Categoria -> Modelo de destino (a tabela pai). Cada produto está ligado a uma categoria.
    # related_name='produtos' -> Permite acessar todos os produtos de uma categoria usando: categoria.produtos.all()
    # null=True	-> Permite que o produto não tenha uma categoria (campo pode ser nulo no banco de dados).
    # on_delete=models.CASCADE -> Se a categoria for apagada, os produtos também serão deletados automaticamente.
    categoria = models.ForeignKey(Categoria, related_name='produtos',null=True, on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nome',) 
        # Cria um índice composto no banco de dados, ou seja, um índice único para a combinação dos campos id e slug.
        # Para que serve? Melhora a performance de buscas onde os dois campos são usados juntos.
        # Exemplo: Produto.objects.get(id=5, slug='coca-cola')
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    # É um método especial do Python que define a representação legível do objeto quando ele é convertido em string
    # Para aprender segue comparação
    ## SEM def __str__(self): ##
    # produto = Produto.objects.first()
    #    print(produto)          # <Produto: Produto object (1)>
    #    print(produto.nome)     # Coca-Cola

    ## COM def __str__(self): ##
    # produto = Produto.objects.first()
    # print(produto)          # Coca-Cola

    def __str__(self):
        return self.nome

    # Deixa a URL mais amigável indexa página, usada em mecanismo
    # de busca pelo google - testar
    def get_absolute_url(self):
        return reverse('main:detalhes_produto', args=[self.id, self.slug])
        #return reverse('main:detalhes_produto', args=[self.slug])    


    