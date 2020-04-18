class Desconto__por_cinco_itens:

    def __init__(self, proximo_deesconto):
        self.__proximo_deesconto = proximo_deesconto


    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1 
        
        return self.__proximo_deesconto.calcula(orcamento)


class Desconto__por_mais_de_quinhentos_reais:

    def __init__(self, proximo_deesconto):
        self.__proximo_deesconto = proximo_deesconto


    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07 

        return self.__proximo_deesconto.calcula(orcamento)


class Sem_desconto:

    def calcula(self, orcamento):
        return 0