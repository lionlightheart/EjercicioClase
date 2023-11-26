import json
import requests


class Controlador_paises:
    @staticmethod
    def descargar_paises():
        url = 'https://restcountries.com/v3.1/region/europe'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return json.loads(respuesta.text)
        else:
            return None
    @staticmethod
    def guardar_paises(paises):
        with open('./files/paises.json', 'w', encoding='utf-8') as archivo:
            json.dump(paises, archivo, indent=2)
    @staticmethod       
    def cargar_paises():
        with open('./files/paises.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)