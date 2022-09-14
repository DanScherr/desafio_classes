from Class_CartaoDeCredito import CartaoDeCredito
import classteste

# Vamos supor que já estamos logados na conta, que será feito no classteste.py 
#   através do método 'acessar_conta'

comando_inicial = input(''' Digite o número do que deseja realizar 
                            1 - comprar, 
                            2 - consultar valor da fatura, 
                            3 - consultar limite atual ou 
                            4 - pagar fatura
                            -> ''')

if (comando_inicial == "1"):

    valor_compra = float(input("Digite o valor da compra: "))
    print(victoria_deb.comprar(valor_compra))

elif (comando_inicial == "2"):

    print("O valor atual da fatura é de R$", victoria_deb.consultar_valor_fatura())

elif (comando_inicial == "3"):

    print("O valor atual do limite disponível é de R$", victoria_deb.checar_limite())