def somar(a, b):
    a + b 

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultad é = {resultado}")

exibir_resultado(10, 12, somar)