class Banco:

    def __init__(self, nome:str):

        self.nome = nome

        self.lista_clientes = list()

    
    def cadastrar_cliente(self, cpf: str, senha: str, renda:float) -> bool:
        '''Criar um objeto conta dado nome, cpf, senha e renda'''
        cadastro = (cpf,senha,renda)
        self.lista_clientes.append(cadastro)
        


        return self.lista_clientes

    #def acessar_conta(self, cpf:str, senha:str)  :
        '''Dado um cpf e senha, procurar a conta na lista de clientes e retornar a conta'''
        #for acessar in self.lista_clientes:
            #if acessar.cpf = cpf
            #rint(f'sua conta e {self.lista_clientes}')
            
            
            

    def analisar_credito(self):
        for i in self.lista_clientes:
            if i.renda >= 2000:
                limite_cartao = i.renda * 0.3
               
            else: 
                limite_cartao = i.renda * 0.1

        return limite_cartao
      


