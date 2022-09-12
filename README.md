# Trilha Endenharia de Dados - IBM - Classes e Orientação a Objetos
### Setembro 2022

***

<br>

## Desafio Banco
**Descrição:** Para práticar o aprendizado de Classes e Objetos iremos trabalhar com a representação de um Banco e suas funcionalidades.
<br>

***
<br>

### <b>Classes Base</b>
'''python <br><br>
<b>class Banco:</b>

    def __init__(self, nome_banco:str):

        self.nome = nome

        self.lista_clientes = list()

    
    def cadastrar_cliente(self, cpf:str, senha:str, renda:float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
        pass

    def acessar_conta(self, cpf:str, senha:str) -> Conta:
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta''''
        pass

    def analisar_credito(self, conta:Conta) -> float:
        '''Dada renda de uma conta, definir regras que retornem um limite adequado para o cliente''''
        pass



<b>class Conta:</b>

    def __init__(self, nome:str, cpf:str, senha:str, renda:float, chave_pix:str, saldo:float):
        '''Terá atributos do usuário como:'''

        self.nome      = nome
        self.cpf       = cpf
        self.senha     = senha
        self.renda     = renda
        self.chave_pix = chave_pix
        self.saldo     = saldo
        
        self.lista_cartoes_de_credito = list()

    def criar_cartao_de_credito(self) -> CartaoDeCredito:
        '''Criar objeto cartao de credito na conta, dados limite e nome do cartão de crédito, chamará metodo de análise de crédito do banco
        para definir limite'''
        pass
    
    def pagar_boleto(self) -> bool:
        '''Pagar boleto dado valor'''
        pass
    
    def sacar_dinheiro(self, qtd:float) -> bool:
        pass 

    def depositar_dinheiro(self, qtd:float) -> bool:
        pass

    def criar_alterar_chave_pix(self, chave_pix:str) -> bool:
        pass

    def fazer_pix(self, chave_pix_destino:str, qtd:float, banco_destino:Banco) -> bool:
        '''Dada um objeto de conta origem, e uma chave pix destino, e quantidade da transferencia, fazer redução no saldo de uma conta e aumento de saldo na conta destino'''
        pass    
    

<b>class CartaoDeCredito:</b>

    def __init__(self, nome_cartao:str, limite_total:float):

        self.nome_cartao   = nome_cartao
        
        self.limite_cartao = limite_total
        self.limite_atual  = limite_total

    def comprar(self, valor_compra:float) -> bool:
        '''Checar limite, se é possivel realizar a compra, reduzir limite, etc'''
        pass
    
    def consultar_valor_fatura(self):
        '''Retornar valor fatura'''
        pass

    def pagar_fatura(self, conta:Conta) -> bool:
        '''Pagar fatura, reistituir limite'''
        pass
    

