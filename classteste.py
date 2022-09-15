from class_Conta import Conta

class Banco:

    def __init__(self, nome:str):

        self.nome = nome

        self.lista_clientes = list()

    
    def cadastrar_cliente(self, nome: str, cpf: str, senha: str, renda:float, chave_pix: str, saldo: float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
        # Primeiro: instanciar um objeto da classe cliente
        novo_cliente = Conta(nome, cpf, senha, renda, chave_pix, saldo)
        # Segundo: adiciono objeto cliente recem criado à lista lista_clientes
        self.lista_clientes.append(novo_cliente)
        # Terceiro: retornar confirmação
        return True

    def acessar_conta(self, cpf:str, senha:str) -> Conta :
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta'''
        # Primeiro: percorrer lista de clientes do banco
        for objeto in self.lista_clientes:
            # Segundo: comparar parametros
            if( objeto.cpf == cpf and 
                objeto.senha == senha ):
                # Terceiro: retorna caso encontrar
                return objeto
            # Segundo: caso contrário
            else:
                # Terceiro: retorna nada
                return None
            

    def analisar_credito(self, conta: Conta.get_renda) :
        for i in Conta.get_renda:
            if Conta.get_renda>= 2000:
                i = Conta.get_renda *2
        else:
            'Limite Negado'
            
      

#cliente1 = Banco('Joao').cadastrar_cliente('154.594.647-03', '1326',10000)
#cliente2 = Banco('Breno').cadastrar_cliente('152.590.647-06', '1020',9000)
#cliente3 = Banco('Ana').cadastrar_cliente('155.599.647-09', '2888',12000)
#cliente4 = Banco('Bia').cadastrar_cliente('153.598.647-15', '4560',5000)
#cliente5 = Banco('Pedro').cadastrar_cliente('151.592.647-21', '9087',1000)

#acesso_conta = Banco('Bia').acessar_conta('153