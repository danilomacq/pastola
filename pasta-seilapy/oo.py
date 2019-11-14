class Mamiferos():
    olhos = 2
    patas = 4
    
    def __init__(self, pelo, especie, rabo, cor):
        self.pelo = pelo
        self.especie = especie
        self.rabo = rabo
        self.cor = cor

    def comer(self):
        print("comendo")
    def fazer_som(self):
        print("som")

mami = Mamiferos("Curto", "Doguinhos Caninus", True, "Caramelo")
mami2 = Mamiferos("Longo", "Agrarios Monata", False, "Purple")

mami.fazer_som()

class Gato(Mamiferos):
    def __init__(self, pelo, especie, rabo, cor, bigodes):
        super().__init__(pelo, especie, rabo, cor)
        self.bigodes = bigodes
    def fazer_som(self):
        print("EU TUDO")

gatinho = Gato("super curto", "peladus egiptum", True, "Bege Orgânico", 5)
gatinho.fazer_som()

 