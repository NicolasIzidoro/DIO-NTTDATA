#depositar, Sacar, extrato

menu = """
[1] depositar
[2] sacar
[3] extrato
[0] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input(f"digite o quanto gostaria de despositar:  "))

        if deposito > 0:
            saldo += deposito
            extrato += f"deposito: R$ {deposito:.2f}\n"
            print("saque realizado com sucesso!")
             
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
        print("~~~~~~~~~~~~EXTRATO~~~~~~~~~~~~")
        print("Não foram realizadas transações em sua conta!" if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    elif opcao == 0:
        break