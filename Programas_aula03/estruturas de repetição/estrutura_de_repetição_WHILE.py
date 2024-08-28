opcao = -1

while opcao !=0:
    opcao = int(input("[1] sacar \n [2] depositar \n [3] ajuda \n [0] sair \n: "))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2: 
        print("depositando....")
    elif opcao == 3:
        print("A ajuda ja vai chegar!")
    


# BREAK serve para quebrar o loop, assim como o brak temos o \CONTINUE  que serve para exibir tudo oq estiver no seu for por exemplo menos algo especifico

for numero in range(100):
    if numero == 22:
        continue

    print(numero, end=" ")