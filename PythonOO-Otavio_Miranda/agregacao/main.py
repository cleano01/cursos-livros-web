from classes import CarrinhoDeCompra, Produto


carrinho = CarrinhoDeCompra()

p1 = Produto('c', 60)
p2 = Produto('a', 160)
p3 = Produto('b', 132)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)

carrinho.lista_produto()

print(carrinho.soma_total())