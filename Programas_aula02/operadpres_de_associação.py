# Operadores de associação EM (in) são comumente usandos quando querem verificar se tal numero 
# esta naquela lista, tbm sendo ultilizado com o NOT para saber se tal nome NÃO esta na lista 
# Sendo tbm case sensitive ou seja se importando com as letras maiusculas e minuscukas

curso = "Curso De Python"
frutas = ["banana", "laranja", "morango"]
saques = [1600, 15]

exp1 = "Python" in curso

exp2 = "laranja" not in frutas

exp3 = 200 in saques

print(exp1, exp2, exp3)