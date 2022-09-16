class CartaoDeCredito:

    def __init__(self, nome_cartao: str, limite_total: float):

        # vamos importar as informações do nome e limite criadas no class_Conta e puxar os valores
        #   do cartão do cidadão 
        self.nome_cartao     = nome_cartao

        self.__limite_cartao = limite_total
        self.limite_atual    = limite_total

        self.valor_fatura    = 0.0


    def comprar(self, valor_compra: float) -> bool:

        if (valor_compra <= self.limite_atual):

            self.limite_atual = self.get_limite() - valor_compra
            self.valor_fatura = self.get_valor_fatura() + valor_compra

            return True

        else:
            return False


    def get_valor_fatura(self):
        return self.valor_fatura

    def set_fatura(self, valor_fatura):
        self.fatura = valor_fatura


    def get_limite(self):
        return self.limite_atual

    def set_limite(self, limite_atual):
        self.limite = limite_atual

    # self.set_limite(0) -> alteramos o valor na atribuição do novo valor no parametro

    def pagar_fatura(self, valor_pagar_fatura:float) -> bool :      
        '''Pagar fatura, reistituir limite'''

        if (valor_pagar_fatura >= self.get_valor_fatura()):

            self.set_fatura(0)
            self.limite_atual = self.__limite_cartao

            troco = round(valor_pagar_fatura - self.valor_fatura, 2)
            print(f"Seu troco é de R${troco}.")

            return True

        else:

            self.valor_fatura = self.get_valor_fatura() - valor_pagar_fatura
            self.limite_atual = self.get_limite() - self.get_valor_fatura()
            
            print("Lamentamos que não seja dinheiro o suficiente.")
            print(f"Ainda faltam R${self.get_valor_fatura()} a serem pagos da fatura.")
            print(f"Seu limite atual fica de R${self.get_limite()}.")

            return False
