# numeros = [1, 23, 45, 25, 56, 78, 89, 67, 33, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#          pares.append(numero)
#          print(numero)


# # filtro versão mais simplificada

numeros = [1, 23, 45, 25, 56, 78, 89, 67, 33, 14, 16, 18, 20, 22, 24, 26, 28, 30]
pares = [numero for numero in numeros if numero % 2 == 0]
