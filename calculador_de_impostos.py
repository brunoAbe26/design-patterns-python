class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':
    from orcamento import Orcamento
    from impostos import ICMS, ISS

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento.valor, ICMS())
    calculador_de_impostos.realiza_calculo(orcamento.valor, ISS())