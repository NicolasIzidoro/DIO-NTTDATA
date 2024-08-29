# Interpolação de variaveis, Temos como fazer interppolação sendo a primeira com prcentagem (% (e usando sempre %s, %d ou %f)), a segunda com a palavra format, e a terceira com o fstring 
#mas para que serve a interpolação?? a interpolação serve para você colocar valores de variaveis dentro de strings de forma direta 
#%s tipo string
#%D tipo inteiro
#%f para tipos float

#OldStile (%)

nome = "Nicolas"
idade = 21
profissao = "programador"
Curso ="Engenharia de Software"
media = 9.5 

print("Olá, me chamo %s e tenho %d de idade, atualmente sou um %s, e estudo %s na Anhanguera e minha media é %f"\
       %(nome, idade,profissao,Curso,media))

#>format 
print("Olá, me chamo {} e tenho {} de idade, atualmente sou um {}, e estudo {} na Anhanguera e minha media é {}" \
      .format(nome, idade,profissao,Curso,media))

print("Olá, me chamo {4} e tenho {0} de idade, atualmente sou um {1}, e estudo {3} na Anhanguera e minha media é {2}" \
      .format(idade, profissao,media,Curso,nome))

print("Olá, me chamo {N} e tenho {I} de idade, atualmente sou um {P}, e estudo {C} na Anhanguera e minha media é {M}" \
      .format(N = nome, I = idade,P = profissao,C = Curso,M = media))

#f-string(esse final ccom a media e os dois pontos o que vem depois serve para mostrar quantas casas decimais voce gostaria de mostrar)
nome = "Phillp"
idade = 31
idade2 = 19
profissao = "programador"
Curso ="Engenharia de Dados"
media = 10.5675856

print(f"Olá, meu nome é {nome}, tenho {idade} de idade, sou {profissao}\
       e fiz {Curso} quando tinha {idade2} anos e minha media era {media: .2f} ")



