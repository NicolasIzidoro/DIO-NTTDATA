# Identação , serve para que ele fique mais legivel e para que a manutenção nele seja mais facil 
# e se caso não houver identação o codigo, provavelmente vai funcionar errado isso se funcionar, alem da legibilidade ficar um coco 
# Exemplo:

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor_sacado!")

sacar(100)
#jeito errado pois depois dos dois pontos ele espera que haja uma identação para queo codigo funcione da maneira esperada
def depositar(valor):
 saldo = 500
 saldo+= valor


sacar(1000)

#e é por identação que o codigo sabe onde cada bloco começa e cada bloco termina
