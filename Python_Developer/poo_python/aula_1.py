#CRIANDO O PRIMEIRO PROGRAMA COM POO
class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim, pilm...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("VrUMMMM....")

    def __str__(self):
        return f"Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"

b2 = Bicicleta("Verde", "Monark", 2000, 189)
print(b2)
