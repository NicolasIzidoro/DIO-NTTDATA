# Bem temos dois jeitos de passar parametros sendo um por posição, nome e os dois ao mesmo tempo sendo o exemplo abaixo os dois ao mesmo tempo 
# onde é invalido passar somente pelo nome que é a segunda metade depoois da barra e valido se passarmos so pelo nome ou meio a meio  
# argumentos nomeados por posição vai usr o asterisco 
# e por posição vai usar a barra (que é o que ocorre no exemplo abaixo )  

def criar_carro(modelo, ano, placa, /, *,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 2000, "akd-483", marca="fiat", motor=1.0, combustivel="Gasolina")


