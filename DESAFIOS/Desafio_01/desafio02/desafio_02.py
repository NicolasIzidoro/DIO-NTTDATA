from datetime import datetime
import textwrap

def menu(): 
    menu =  """\n
    ~~~~~~~~~~BEM VINDO: ~~~~~~~~~~~
    [1]\t depositar
    [2]\t sacar
    [3]\t transação
    [4]\t extrato
    [0]\t sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato, deposito): 
    
    if deposito > 0:
            saldo += deposito
            extrato += f"deposito: R$ {deposito:.2f}\n"
            print("deposito realizado com sucesso!")       
    else:
            print("Não foi possivel realizar o deposito.")

    return saldo, extrato

def sacar(limite, LIMITE_DE_SAQUES, saldo, numero_de_saques, extrato,saque):
        

    if saque > limite:
        print("Não é possivel sacar mais que R$ 500 por vez")   

    elif numero_de_saques >= LIMITE_DE_SAQUES:
        print("Não foi possível sacar, pois atingiu seu limite diário.")

    elif saque > saldo:
        print(f"Saldo insuficiente. Saldo disponível: R$ {saldo:.2f}")

    elif saldo > 0:
        saldo -= saque
        extrato += f"saque: R$ {saque:.2f}\n"
        numero_de_saques += 1
        print("saque realizado com sucesso")

    else:
        print("Não foi possivel completar a operação, o valor informado é invalido!")

    return saldo, extrato
 
def transacao(LIMITE_DE_TRANSAÇOES, qntd_transações, saldo):
             
        if transacao > saldo:
            print("Não foi possivel ralizar a transação, valor digitado maior que saldo")
        elif LIMITE_DE_TRANSAÇOES == qntd_transações:
                    print("Não foi possivel realizar a transação. Limite diario atingido.")
        elif transacao < saldo:
                print(f"Transação de R${transacao:.2f} realizada com sucesso!")
                if transacao:
                    saldo -= transacao
                    qntd_transações += 1
                    transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        return saldo, extrato, transacao
                   
def extrato(qntd_transações,saldo,data_hora):
        print("~~~~~~~~~~~~EXTRATO~~~~~~~~~~~~")
        print("Não foram realizadas transações em sua conta!" if not extrato else extrato)
        print(f"Você realizou {qntd_transações} transações hoje.")
        print(f"\n saldo: R$ {saldo:.2f}")
        print(f"\n \n \nData/Hora: {data_hora} - Valor: R${qntd_transações and transacao:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
def main():
    LIMITE_DE_SAQUES = 3
    LIMITE_DE_TRANSAÇOES = 10

    saldo = 0
    limite = 500
    extrato = ""
    transacao = 0
    numero_de_saques = 0
    qntd_transações = 0

    while True:
        opcao = int(menu())

        if opcao == 1:
            deposito = float(input(f"digite o quanto gostaria de despositar:  "))
            
            saldo, extrato = depositar((saldo, extrato, deposito))

        elif opcao == 2: 
            sacar = float(input(f"digite o quanto gostaria de sacar:  "))
                
            saldo, extrato = sacar(
                limite=limite,
                limite_de_saques = LIMITE_DE_SAQUES, 
                saldo=saldo, 
                numero_de_saques=numero_de_saques, 
                extrato=extrato
            )
        elif opcao == 3:
            transacao = float(input(f"digite o valor que deseja transferir:  "))

            saldo, extrato, transacao = transacao(
                limite_de_transaçoes = LIMITE_DE_TRANSAÇOES,
                qntd_transações=qntd_transações,
                saldo=saldo
                ) 
        elif opcao == 4:
            extrato(qntd_transações,saldo,data_hora=datetime)
            