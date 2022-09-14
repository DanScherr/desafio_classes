class Banco:

    def __init__(self, nome:str):

        self.nome = nome

        self.lista_clientes = list()

    
    def cadastrar_cliente(self, cpf: str, senha: str, renda:float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
        conta = [self.nome,cpf,senha,renda]
        self.lista_clientes.append(conta)


        return conta

    def acessar_conta(self, cpf:str, senha:str) :
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta'''
        for acessar in self.lista_clientes:
            if cpf == cpf:
                print(f'Sua conta e {self.lista_clientes}')
            if senha == senha:
                print(f'sua conta e {self.lista_clientes}')
            
            return acessar
        

cliente1 = Banco('Joao').cadastrar_cliente('154.594.647-03', '1326',10000)
cliente2 = Banco('Breno').cadastrar_cliente('152.590.647-06', '1020',9000)
cliente3 = Banco('Ana').cadastrar_cliente('155.599.647-09', '2888',12000)
cliente4 = Banco('Bia').cadastrar_cliente('153.598.647-15', '4560',5000)
cliente5 = Banco('Pedro').cadastrar_cliente('151.592.647-21', '9087',1000)

acesso_conta = Banco('Bia').acessar_conta('153.598.647-15', '4560')
print(acesso_conta)