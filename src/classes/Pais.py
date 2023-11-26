import uuid

class Pais:
    def __init__(self, cca2, cca3, nombre, capital, region, subregion, miebroUE, latitud, longitud, fonteras=[]):
        self.id = str(uuid.uuid4())
        self.cca2 = cca2
        self.cca3 = cca3
        self.nombre = nombre
        self.capital = capital[0]
        self.region = region
        self.subregion = subregion
        self.miebroUE = miebroUE
        self.latitud = latitud
        self.longitud = longitud
        self.fonteras = fonteras
    
    def __str__(self):
        return f"{self.nombre} {self.cca3} {self.fonteras}"