# OPERADORES LOGICOS são nada mais nada menos que uma combinação de de operadores
# logicos junto a operadores de comparação que unidos formam  uma expressão logica 
# que retorna um resultado booleano 

# primeiro exemplo sendo um bem simples e usando eles separados 

saldo = 1250
saque = 560
limite = 874

print(saldo >= saque)

print(saldo <= limite)

# Agora vamos misturar os operadores logicos junto ao de comparação ultilizando o
# operador E (and) (explicando as duas comparaçãoes tem que ser verdadeiras para 
# que o resultado seja verdadeiro caso o contrario sera FALSO)

saldo = 1250
saque = 560
limite = 874
print(saldo >= saque and saque <= limite)

# Agora ultilizando o operador OU (or), sendo que uma das comparações tem que ser 
# verdadeira para que o resultado seja verdadeiro

saldo = 1240
saque = 2260
limite = 864
print(saldo >= saque or saque >= limite)

# operador de negação  NÂO (not) o operador not vai inverter o resultado que der ou seja 
# se a respota for positiva ele transforma em negativa e se a resposta for positiva ele 
# transforma em negativa

saldo = 240
saque = 260
limite = 364

print(not saque >= saldo)
print(not limite <= saldo)



print(not "saquei 1900;")

print(not "")

########
saldo = 1240
saque = 260
limite = 364
conta_especial = True


print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))


# um outro jeito de fazer e deixar mais enchuto
exp1 = saldo >= saque and saque <= limite 
exp2 = conta_especial and saldo >= saque
exp3 = exp1 or exp2 

print(exp3)