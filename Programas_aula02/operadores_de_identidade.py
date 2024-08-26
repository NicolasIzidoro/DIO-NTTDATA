# Operadores de identidade É (is) são operadores que são usados para comparar se dois objetos testados 
# ocupam o mesmo posição na memoria. Quando sendo usando com o NOT  vai verificar se ele não é tal coisa 

curso = "Curso de python"
nome_curso = curso
saldo, limite = 200, 200

exp1 = curso is nome_curso

exp2 = curso is not nome_curso

exp3 = saldo is limite 

exp4 = saldo is not limite 

(exp1,  exp2, exp3, exp4)


Saldo = 1000
Limite = 500

print(Saldo is Limite)
print(Saldo is not Limite)
