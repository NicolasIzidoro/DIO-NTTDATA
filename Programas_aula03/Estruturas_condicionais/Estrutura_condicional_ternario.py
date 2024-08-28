saldo = 1900
saque = 16100

status = "Sucesso" if saldo >= saque else "Erro"

print(f"{status} ao realizar o saque!")

# Tudo que estiver no começo do IF TERNARIO sera o que ira retornar verdadeiro caso a 
# condição venha a ser atendida e tudo oque ficar no final sera o que ira aparecer caso a 
# condição não seja atendida