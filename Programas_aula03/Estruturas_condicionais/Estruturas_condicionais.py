#IF realiza uma condição logica se caso a 1 condição seja verdadeira faça tal coisa 
# e se caso for falsa entraria no ELSE e faria  uma outra coisa

# MAIOR_IDADE = 18 

# idade = int(input("Informe a sua idade:  "))

# if idade >= 18:
#         print("Você já pode tirar sua CNH.")
# if idade < 18:
#         print("Você ainda não tem idade para tirar sua CNH")




# MAIOR_IDADE = 18 

# idade = int(input("Informe a sua idade:  "))

# if idade >= 18:
#     print("Você já pode tirar sua CNH.")
# else:
#     print("Você ainda não tem idade para tirar sua CNH")




MAIOR_IDADE = 18 
IDADE_ESPECIAL = 16

idade = int(input("Informe a sua idade:  "))

if idade >= 18:
    print("Você já pode tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
    print("Você já pode assistir as aulas teoricas, mas não pode fazer as aulas praticas!  ")
else:
    print("Você ainda não tem idade para tirar sua CNH")



