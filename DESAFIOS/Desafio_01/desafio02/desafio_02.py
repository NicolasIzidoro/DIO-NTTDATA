#desafio_02
from datetime import datetime
import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tTransação
    [4]\tExtrato
    []\tnova conta
    []\tlistar contas
    []\tnovo usuario
    [0]\tsair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato, deposito): 
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Depósito realizado com sucesso!")       
    else:
        print("Não foi possível realizar o depósito.")
    return saldo, extrato

def sacar(limite, LIMITE_DE_SAQUES, saldo, numero_de_saques, extrato, saque):
    if saque > limite:
        print("Não é possível sacar mais que R$ 500 por vez")   
    elif numero_de_saques >= LIMITE_DE_SAQUES:
        print("Não foi possível sacar, pois atingiu seu limite diário.")
    elif saque > saldo:
        print(f"Saldo insuficiente. Saldo disponível: R$ {saldo:.2f}")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso")
    else:
        print("Não foi possível completar a operação, o valor informado é inválido!")
    return saldo, extrato

def transacao(LIMITE_DE_TRANSAÇOES, qntd_transações, saldo, valor_transacao):
    if valor_transacao > saldo:
        print("Não foi possível realizar a transação, valor digitado maior que saldo")
    elif qntd_transações >= LIMITE_DE_TRANSAÇOES:
        print("Não foi possível realizar a transação. Limite diário atingido.")
    else:
        saldo -= valor_transacao
        qntd_transações += 1
        print(f"Transação de R${valor_transacao:.2f} realizada com sucesso!")
    return saldo, qntd_transações

def extrato(qntd_transações, saldo, extrato):
    print("~~~~~~~~~~~~EXTRATO~~~~~~~~~~~~")
    print("Não foram realizadas transações em sua conta!" if not extrato else extrato)
    print(f"Você realizou {qntd_transações} transações hoje.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def criar_usuarios(usuario):
    cpf = input(float(f"digite somente os numeros do CPF: "))
    usuario = filtrar_usuarios(cpf,usuario)

    if usuario:
        print("CPF invalido! rever o cpf novamente!")
        return
    

    nome_usario = input(str(f"digite seu nome completo: "))
    dt_nascimento = input("digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("informe seu endereço(rua, numero, bairro, cidade, estado):  ")

    usuario.append({"nome_usario": nome_usario, "dt_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})

    print("~~~~~~~USUARIO CRIADO COM SUCESSO !~~~~~~~")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuarios in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuario)

    if usuario:
        print("conta criada com sucesso !!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def main():
    LIMITE_DE_SAQUES = 3
    LIMITE_DE_TRANSAÇOES = 10
    AGENCIA = "0001"


    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    qntd_transações = 0
    usuario = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            deposito = float(input("Digite o quanto gostaria de depositar: "))
            saldo, extrato = depositar(saldo, extrato, deposito)

        elif opcao == 2: 
            saque = float(input("Digite o quanto gostaria de sacar: "))
            saldo, extrato = sacar(limite, LIMITE_DE_SAQUES, saldo, numero_de_saques, extrato, saque)

        elif opcao == 3:
            valor_transacao = float(input("Digite o valor que deseja transferir: "))
            saldo, qntd_transações = transacao(LIMITE_DE_TRANSAÇOES, qntd_transações, saldo, valor_transacao)

        elif opcao == 4:
            extrato(qntd_transações, saldo, extrato)
        
        elif opcao == 5:
            criar_usuarios(usuario)

        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario)
            if conta:
                contas.append(conta)

        elif opcao == 7:
            listar_contas(contas)

        elif opcao == 0:
            break

