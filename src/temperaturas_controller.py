import requests
from src.conf import myDB
from src.classes.temperaturas import Temperatura
from tqdm import tqdm
import time
class Temperatura_controller:
    @staticmethod
    def get_pais_lat_long():
        cursor = myDB.cursor()
        cursor.execute("select idpais, latitud, longitud from paises")
        lat_long = cursor.fetchall()
        cursor.close()
        return lat_long
    
    @staticmethod
    def get_temperatura_api(lat=40,lon=-4.0):
        resultado = {}
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,minutely&lang=es&appid=aa37610bc6932a7462fb997eaa19031e'
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            resultado = respuesta.json()
        else:
            print("Error al obtener la temperatura")
        
        return resultado
    
    @staticmethod
    def generate_temperatura_obj_arr():
        pais_arr = Temperatura_controller.get_pais_lat_long()
        tiempo_arr = []
        for pais in tqdm(pais_arr, desc="Obteniendo temperaturas", unit="iter", bar_format="{l_bar}{bar} [ time left: {remaining} ]"):
            temperatura = Temperatura_controller.get_temperatura_api(pais[1], pais[2])
            tem_pais_obj = Temperatura(pais[0],
                                       temperatura["current"]["temp"],
                                       temperatura["current"]["feels_like"],
                                       temperatura["daily"][0]["temp"]["min"],
                                       temperatura["daily"][0]["temp"]["max"],
                                       temperatura["current"]["humidity"],
                                       temperatura["daily"][0]["sunrise"],
                                       temperatura["daily"][0]["sunset"])
            tiempo_arr.append(tem_pais_obj)
        return tiempo_arr
    @staticmethod
    def add_to_db(temperaturas):
        print("Añadiendo temperaturas a la base de datos")
        cursor = myDB.cursor()
        cursor.execute("delete from temperaturas")
        sql = "INSERT INTO temperaturas (idpais,timestamp, temperatura,sensacion, minima, maxima, humedad, amanecer, atardecer) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s)"
        valores = [(temperatura.idpais,
                    temperatura.timestamp,
                    temperatura.temperatura,
                    temperatura.sensacion,
                    temperatura.minima,
                    temperatura.maxima,
                    temperatura.humedad,
                    temperatura.amanecer,
                    temperatura.atardecer) for temperatura in temperaturas]
        cursor.executemany(sql, valores)
        myDB.commit()
        cursor.close()
            
         