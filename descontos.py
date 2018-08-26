class Desconto_por_cinco_itens(object):
    def __init__(self, proximo):
        self.__proximo = proximo


    def calcular(self, orcamento):
        if orcamento.total_itens > 5: return orcamento.valor * 0.1
        else: return self.__proximo.calcular(orcamento)


class Desconto_mais_de_quinhentos_reais(object):
    def __init__(self, proximo):
        self.__proximo = proximo


    def calcular(self, orcamento):
        if orcamento.valor > 500: return orcamento.valor * 0.07
        else: return self.__proximo.calcular(orcamento)


class Sem_desconto(object):
    def calcular(self, orcamento):
        return 0
