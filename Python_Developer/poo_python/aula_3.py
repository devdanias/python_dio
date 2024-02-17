##HERANÇA SIMPLES
class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    pass

carro = Carro("branco", "CXS-23131", 2)
carro.ligar_motor()


caminhao = Caminhao("Preto", "CXS-6794", 4)
carro.ligar_motor()
