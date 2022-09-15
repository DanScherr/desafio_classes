from class_Conta import Conta


class CartaoDeCredito:

    def __init__(self, nome_cartao: str, limite_total: float):

        # vamos importar as informações do nome e limite criadas no class_Conta e puxar os valores
        #   do cartão do cidadão 
        self.nome_cartao     = nome_cartao

        self.__limite_cartao = limite_total
        self.limite_atual    = limite_total

        self.valor_fatura          = 0.0


    def comprar(self, valor_compra: float) -> bool:

        self.valor_compra = valor_compra

        if (self.valor_compra <= self.limite_atual):

            self.limite_atual = self.limite_atual - self.valor_compra
            self.valor_fatura       = self.valor_fatura + self.valor_compra

            return "Compra efetuada"

        else:
            return "Limite Insuficiente"


    def consultar_valor_fatura(self):
        return self.valor_fatura


    def checar_limite(self):
        return self.limite_atual

    def pagar_fatura(self, conta:Conta):       # -> bool
        '''Pagar fatura, reistituir limite'''
       
        valor_pag_fatura = float(input("Digite o valor da fatura a ser pago: "))
#        self.valor_fatura = self.valor_fatura - valor_pag_fatura


        if (valor_pag_fatura >= self.valor_fatura):

            self.valor_fatura = 0
            self.limite_atual = self.__limite_cartao

            troco = round(valor_pag_fatura - self.valor_fatura, 2)
            print(f"Seu troco é de R${troco}.")

        else:

            self.valor_fatura = self.valor_fatura - valor_pag_fatura
            self.limite_atual = self.limite_atual - self.valor_fatura
            print("Lamentamos que não seja dinheiro o suficiente.")
            print(f"Ainda faltam R${self.valor_fatura} a serem pagos da fatura.")
            print(f"Seu limite atual fica de R${self.limite_atual}.")


