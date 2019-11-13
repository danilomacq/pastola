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