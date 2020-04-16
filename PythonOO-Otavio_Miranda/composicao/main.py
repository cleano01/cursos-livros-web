from classes import Cliente

c = Cliente('luiz',32)
c.insere_endereco('bayeux', 'pb')
c.lista_enderecos()
print()

c2 = Cliente('maria',38)
c2.insere_endereco('joão pessoa', 'pb')
c2.insere_endereco('santa rita', 'pb')
c2.lista_enderecos()
print()

c3 = Cliente('rosa',18)
c3.insere_endereco('são paulo', 'sp')
c3.lista_enderecos()

print('##################')




