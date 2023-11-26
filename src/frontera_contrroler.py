from src.classes.Pais import Pais
from src.classes.Frontera import Frontera
from src.conf import myDB
from typing import List
import json

class FronteraController:
    @staticmethod
    def create_fronteraObj(paises: List[Pais]):
        cursor= myDB.cursor()
        fronteras = []
        for pais in paises:
            for frontera in pais.fonteras:
                cursor.execute(f"select idpais from paises where cca3='{frontera}'")
                fronteraId = cursor.fetchall()
                if len(fronteraId) > 0:
                    obj = Frontera(pais,fronteraId[0][0], frontera)
                    fronteras.append(obj)
        myDB.commit()
        cursor.close()
        return fronteras
    
    @staticmethod
    def add_to_db(fronteras: List[Frontera]):
        cursor = myDB.cursor()
        sql = "insert into fronteras (idfronteras, idpais, cca3_frontera) values(%s,%s, %s)"
        valores = [(
            frontera.idPaisFront,
            frontera.idPais,
            frontera.cca3Frontera) 
                   for frontera in fronteras]
        cursor.executemany(sql, valores)
        myDB.commit()
        cursor.close