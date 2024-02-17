#METODOS DE CLASSE
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nasciment(self,ano,mes,dia,nome):
        idade = 2022 - ano
        return Pessoa (nome,idade)



p = Pessoa.criar_apartir_data_nasciment(1998,3,21,"Guilherme")
print(p.nome, p.idade)