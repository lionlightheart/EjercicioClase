from src.controlador_de_paises import Controlador_paises as paises
from src.pais_controller import PaisController as pais_controller
from src.frontera_contrroler import FronteraController as front

def main():
  try:
    paises.guardar_paises(paises.descargar_paises())
    paises_objArr = pais_controller.create_paisObj(pais_controller.get_paises())
    pais_controller.save_paises_DB(paises_objArr)
    fronteras_obj = front.create_fronteraObj(paises_objArr)
    front.add_to_db(fronteras_obj)
    
  except():
    print("No se pudo descargar los paises")
  
  
if __name__ == "__main__":
  main()