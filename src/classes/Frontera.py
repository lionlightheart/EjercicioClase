from src.classes.Pais import Pais

class Frontera:
    def __init__(self, pais: Pais,fronteraid, frontera):
        self.idPaisFront = fronteraid
        self.idPais = pais.id
        self.cca3Frontera = frontera