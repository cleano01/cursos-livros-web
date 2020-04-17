from descontos import Desconto__por_cinco_itens,\
     Desconto__por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_Descontos:

    def calcula(self, orcamento):

        desconto = Desconto__por_cinco_itens(
            Desconto__por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcula(orcamento)

        return desconto
            


if __name__ == '__main__':
    
    from orcamento import Orcamento , Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1', 100))
    orcamento.adiciona_item(Item('ITEM-2', 50))
    orcamento.adiciona_item(Item('ITEM-3', 400))


    calculador = Calculador_de_Descontos()

    desconto_calculado = calculador.calcula(orcamento)
    print(desconto_calculado)


