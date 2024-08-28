conta_normal = False
conta_universitaria = False

saldo = 1200
saque = 1100
cheque_especial = 320

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else:
        print("Não foi possivel realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Não foi possivel realizar o seu saque, o sistrma não reconheceu o seu tipo de conta, entrar em contato com o banco!")