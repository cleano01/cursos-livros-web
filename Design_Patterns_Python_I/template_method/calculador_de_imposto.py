from impostos  import ICMS, ISS, ICPP, IKCV

class Calculador_de_Impostos:

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)

    
if __name__ == '__main__':
    
    from orcamento import Orcamento, Item

    calculador = Calculador_de_Impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1', 50))
    orcamento.adiciona_item(Item('ITEM-2', 200))
    orcamento.adiciona_item(Item('ITEM-3', 250))
    
    print('ISS e Icms')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('Icpp e Ikcv')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

