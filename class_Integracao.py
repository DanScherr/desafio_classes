from class_Conta import Conta
from classteste import Banco
from Class_CartaoDeCredito import CartaoDeCredito

class Integracao:

    def fazer_pix(self, conta: Conta,chave_pix_destino:str, qtd:float, banco_destino:Banco) -> bool:
        '''Dada um objeto de conta origem, e uma chave pix destino, e quantidade da transferencia, fazer redução no saldo de uma conta e aumento de saldo na conta destino'''
        for conta in banco_destino.lista_clientes:
            if (( conta.get_chave_pix() != chave_pix_destino ) or
                ( conta.get_saldo() < qtd )):
                return False
            else:
                conta.set_saldo(self.get_saldo() - qtd)
                conta.set_saldo(qtd)
                return True
        pass
    