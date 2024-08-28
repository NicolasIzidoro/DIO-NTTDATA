# FOR e WHILE e quando usa-las

#FOR faz sentido usar ele quando sabemos quantas vezes queremos repetir o bloco de codigo, ou quando queremos percorrer um objeto iteravel
#Exemplo usando um iteravel
texto = input("Digite o seu texto: ")
Vogais = "AEIOU"

for palavra in texto:
    if palavra.upper() in Vogais:
        print(palavra, end="")
else: 
    print("não tem vogais na palavra digitada!")

print()
