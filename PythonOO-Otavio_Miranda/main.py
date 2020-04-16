from pessoa import Pessoa
from produto import Produto
from base_de_dados import BaseDeDados




'''
bd = BaseDeDados()

bd._dados = 'teste'
print( bd._dados)


bd.inserir_cliente(1, 'maria')
bd.inserir_cliente(2, 'joao')
bd.inserir_cliente(3, 'rose')

bd.apaga_cliente(2)
bd.lista_clientes()
'''
'''

p1 = Produto('CAMISA', 50)
p1.desconto(10)
print( p1.nome , p1.preco)


p2 = Produto('caneca', 'R$15')
p2.desconto(10)
print( p2.nome ,p2.preco)

'''
'''

p1 = Pessoa('jose', 40)
print(Pessoa.gera_id())
print(p1.gera_id())

p1 = Pessoa('jose', 40)
p1.comer('banana')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('maca')
print(p1.get_ano_nascimento())
print('####')


p2 = Pessoa('Maria', 20)
p2.comer('Pipoca')
p2.falar('aulas')
p2.parar_comer()
p2.falar('aulas')
p2.comer('sorverte')
print(p2.get_ano_nascimento())
'''

