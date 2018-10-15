#-*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não podem ir para finalizado diretamente')


class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        raise Exception('Orçamento já está em estado de aprovação')

    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de aprovação e não pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem descontos extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de reprovação')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem descontos extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado já foi aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('Orçamento já foi finalizado')


class Orcamento(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)


    @property
    def total_itens(self):
        return len(self.__itens)


    def adiciona_item(self, item):
        self.__itens.append(item)


class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor


    @property
    def valor(self):
        return self.__valor


    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
    orcamento.aprova()

    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
    orcamento.finaliza()

    orcamento.aplica_desconto_extra()
