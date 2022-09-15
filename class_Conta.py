# ------------ IMPORTING -------------
# Imports of suporting classes
from class_Depena_String import Depena_String
from Class_CartaoDeCredito import CartaoDeCredito

# ------------ DEFINING CLASS ------------
class Conta:


# TODO: Criar construtor
    def __init__(self, nome:str, cpf:str, senha:str, renda:float, chave_pix:str, saldo:float) -> None:
        '''Terá atributos do usuário como:'''
        self._nome      = self.set_nome(nome)
        self._cpf       = self.set_cpf(cpf)
        self._renda     = self.set_renda(renda)
        self._senha     = self.set_senha(senha)
        self._chave_pix = self.set_chave_pix(chave_pix)
        self._saldo     = self.set_saldo(saldo)

        self.lista_cartoes_de_credito = list()


# TODO: Geters e Seters
    def get_nome(self) -> str:
        return self.nome
        pass

    def set_nome(self, nome) -> None:
        nome = Depena_String(nome)
        self.nome = nome.nomeComposto()
        pass

    def get_cpf(self) -> str:
        return self.cpf
        pass

    def set_cpf(self, cpf) -> None:
        cpf = Depena_String(cpf)
        self.cpf = cpf.cpf()
        pass
    
    def get_renda(self) -> float:
        return self.renda
        pass

    def set_renda(self, renda) -> None:
        self.renda = renda
        pass

    def get_senha(self) -> str:
        return self.senha
        pass

    def set_senha(self, senha) -> None:
        self.senha = senha
        pass

    def get_chave_pix(self) -> str:
        return self.chave_pix
        pass

    def set_chave_pix(self, chave_pix) -> None:
        self.chave_pix = chave_pix
        pass

    def get_saldo(self) -> float:
        return self.saldo
        pass

    def set_saldo(self, saldo) -> None:
        self.saldo = saldo
        pass

# TODO: Métodos da classe conta
    def criar_cartao_de_credito(self) -> CartaoDeCredito:
        '''Criar objeto cartao de credito na conta, dados limite e nome do cartão de crédito, chamará metodo de análise de crédito do banco
        para definir limite'''
        novo_cartao_de_credito = CartaoDeCredito('exemplo1', self.get_renda()*1.5)
        self.lista_cartoes_de_credito.append(novo_cartao_de_credito)
        pass

    def pagar_boleto(self, valor: float) -> bool:
        '''Pagar boleto dado valor'''
        # Se saldo corrente é menor que a qtd desejada de sacar, retorna false
        if (( self.get_saldo() < valor ) and
            ( type(valor) != float )):
            return False
        # Caso contrário subtrai o valor da conta e retorna true
        else:
            self.set_saldo(self.get_saldo() - valor)
            return True
        pass
    
    def sacar_dinheiro(self, qtd:float) -> bool:
        # Se saldo corrente é menor que a qtd desejada de sacar, retorna false
        if (( self.get_saldo() < qtd ) and 
            ( type(qtd) != float )):
            return False
        # Caso contrário subtrai o valor da conta e retorna true
        else:
            self.set_saldo(self.get_saldo() - qtd)
            return True
        pass 

    def depositar_dinheiro(self, qtd:float) -> bool:
        # Se saldo corrente é menor que a qtd desejada de depositar, retorna false
        if (type(qtd) != float):
            return False
        # Caso contrário subtrai o valor da conta e retorna true
        else:
            self.set_saldo(self.get_saldo() + qtd)
            return True
        pass

    def criar_alterar_chave_pix(self, nova_chave_pix:str) -> bool:
        if ( type(nova_chave_pix) == str ):
            self.set_chave_pix(nova_chave_pix)
        pass
