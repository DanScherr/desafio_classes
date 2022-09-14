class CartaoDeCredito:

    def __init__(self, nome_cartao: str, limite_total: float):

        self.nome_cartao = nome_cartao

        self.__limite_cartao = limite_total
        self.limite_atual = limite_total
        self.fatura = 0.0


    def comprar(self, valor_compra: float) -> bool:

        self.valor_compra = valor_compra

        if (self.valor_compra <= self.limite_atual):

            self.limite_atual = self.limite_atual - self.valor_compra
          
            self.fatura = self.fatura + self.valor_compra

            return "Compra efetuada"

        else:

            return "Limite Insuficiente"


    def consultar_valor_fatura(self):

        return self.fatura

        pass


    def checar_limite(self):

        return self.limite_atual



'''   def pagar_fatura(self, conta:Conta) -> bool:
        Pagar fatura, reistituir limite
        pass
'''
