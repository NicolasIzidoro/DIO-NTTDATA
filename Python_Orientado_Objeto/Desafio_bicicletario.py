class bicicleta: 
    def __init__ (self, cor, modelo, ano, valor):
            self.cor = cor
            self.modelo = modelo
            self.ano = ano 
            self.valor = valor

    def buzina(self):
          print("BUZINANDO")

    def parar(self):
          print("Parando a bicicleta.....")
          print("bicicleta parada!")

    def andando(self):
          print("Comecando a andar....")
          print("andando de bicicleta!")
b1 = bicicleta("Azul", "Caloi", 2003, 850)
    
b1.buzina
b1.parar
b1.andando

print(b1.cor)

