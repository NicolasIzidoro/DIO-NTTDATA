from datetime import datetime
menu = """
[1] depositar
[2] sacar
[3] transação
[4] extrato
[0] sair

"""

saldo = 0
limite = 500
extrato = ""
transacao = 0
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
LIMITE_DE_TRANSAÇOES = 10
qntd_transações = 0


while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input(f"digite o quanto gostaria de despositar:  "))

        if deposito > 0:
            saldo += deposito
            extrato += f"deposito: R$ {deposito:.2f}\n"
            print("deposito realizado com sucesso!")
             
        else:
            print("Não foi possivel realizar o deposito.")

    elif opcao == 2:
        saque = float(input(f"digite o quanto gostaria de sacar:  "))

        if saque > limite:
            print("Não é possivel sacar mais que R$ 500 por vez")   

        elif numero_de_saques > LIMITE_DE_SAQUES:
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

    
    elif opcao == 3:
        transacao =  float(input(f"digite o valor que deseja transferir:  "))

        if transacao > saldo:
            print("Não foi possivel ralizar a transação, valor digitado maior que saldo")
        elif LIMITE_DE_TRANSAÇOES == qntd_transações:
             print("Não foi possivel realizar a transação. Limite diario atingido.")
        elif transacao < saldo:
         print(f"Transação de R${transacao:.2f} realizada com sucesso!")
         if transacao:
          saldo -= transacao
          qntd_transações += 1
         data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
          
          
    elif opcao == 4:
        print("~~~~~~~~~~~~EXTRATO~~~~~~~~~~~~")
        print("Não foram realizadas transações em sua conta!" if not extrato else extrato)
        print(f"Você realizou {qntd_transações} transações hoje.")
        print(f"\n saldo: R$ {saldo:.2f}")
        print(f"\n \n \nData/Hora: {data_hora} - Valor: R${qntd_transações and transacao:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
      



    
    elif opcao == 0:
        break