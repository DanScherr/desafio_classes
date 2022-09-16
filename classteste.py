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
            

    def analisar_credito(self, cpf:str):
        for i in self.lista_clientes:
            if i.get_cpf() == cpf:
                if i.renda >= 2000:
                    limite_cartao = i.renda * 0.3
                    break
                else: 
                    limite_cartao = i.renda * 0.1
                    break
            else:
                return None
        return limite_cartao
