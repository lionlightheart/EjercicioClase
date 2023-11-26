import uuid
import pytz 
from datetime import datetime

class Temperatura:
    def __init__(self,idpais, temperatura, sensacion, minima, maxima,humedad, amanecer, atardecer):
        self.idtemperaturas = uuid.uuid4()
        self.timestamp = datetime.now()
        self.idpais = idpais
        self.temperatura = temperatura
        self.sensacion = sensacion
        self.minima = minima
        self.maxima = maxima
        self.humedad = humedad
        self.amanecer = self.formatet_time(amanecer)
        self.atardecer = self.formatet_time(atardecer)

    def __str__(self):
        return "Temperatura: " + str(self.temperatura) + " Sensación: " \
            + str(self.sensacion) + " Mínima: " + str(self.minima) + " Máxima: " \
                + str(self.maxima) + " Humedad: " + str(self.humedad) \
                + " Amanecer: " + str(self.amanecer) + " Atardecer: " + str(self.atardecer)
                
    
    def formatet_time(self, tiempo):
        zonaHoraria = pytz.timezone('Europe/Madrid')
        result = datetime.utcfromtimestamp(tiempo)
        result = result.replace(tzinfo=pytz.utc).astimezone(zonaHoraria)
        return result
