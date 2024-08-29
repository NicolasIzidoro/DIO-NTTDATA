# Nesssa seção estou revendo e aprendendo sobre o upper que deixa toda a string maiuscula, 
# lower que deixa toda a string em minusculo, e o title que deixa somente a primeira letra da string em maiusculo

nome = "nIcOlAs"

print(nome.upper())

print(nome.lower())

print(nome.title())

# Já a funçao strip serve para retirar os espaços em branco de uma string o strip sozinho 
# vai retirar os espaços dos dois lados, ja se você usar o lstrip você vai retirar tudo a 
# direita da string e o rstrip vai retirar todo o espaço em branco da esquerda da string

texto = "  Olá mundo!          "

print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")


#junção e Centralização

menu = "programação"

print(menu.center(24))
print(menu.center(24, "¨"))

print("-".join(menu))