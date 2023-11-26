from src.classes.Pais import Pais
from src.conf import myDB
import json


class PaisController:
    @staticmethod
    def get_paises():
        with open('./files/paises.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
    @staticmethod
    def create_paisObj(paises):
        paisesObj = []
        for pais in paises:
            frontera = pais['borders'] if 'borders' in pais else []
            paisObj = Pais(pais['cca2'],
                           pais['cca3'],
                           pais['name']['common'],
                           pais['capital'],
                           pais['region'],
                           pais['subregion'],
                           pais['unMember'],
                           pais['latlng'][0],
                           pais['latlng'][1],
                           frontera
                           )
            paisesObj.append(paisObj)
        return paisesObj
    
    @staticmethod
    def save_paises_DB(paises):
        cursor = myDB.cursor()
        cursor.execute("delete from paises")
        sql = "INSERT INTO paises (idpais, cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Crear una lista de tuplas con los valores de los objetos Pais
        valores = [(pais.id,
                    pais.cca2,
                    pais.cca3,
                    pais.nombre,
                    pais.capital,
                    pais.region,
                    pais.subregion,
                    pais.miebroUE,
                    pais.latitud,
                    pais.longitud) for pais in paises]

        # Ejecutar la consulta SQL para insertar múltiples registros
        cursor.executemany(sql, valores)

        myDB.commit()
        cursor.close()