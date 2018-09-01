class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':
    from orcamento import Orcamento, Item
    from impostos import ICMS, ISS, ICPP, IKCV

    orcamento = Orcamento()
    calculador_de_impostos = Calculador_de_impostos()
    orcamento.adiciona_item(Item('Item A', 50.0))
    orcamento.adiciona_item(Item('Item B', 200.0))
    orcamento.adiciona_item(Item('Item C', 250.0))
    print('ICMS e ISS')
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
    calculador_de_impostos.realiza_calculo(orcamento, ISS())

    print('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())
