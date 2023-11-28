from src.controlador_de_paises_json import Controlador_paises as paises
from src.pais_controller import PaisController as pais_controller
from src.frontera_contrroler import FronteraController as front
from src.temperaturas_controller import Temperatura_controller as temp_controller
from src.conf import myDB
import os


class Main:
    def __init__(self):
        self.cargar_datos()
    
    def main(self):
        menuBucle = False
        while not menuBucle:
            os.system("cls")
            self.print_menu()
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.recargar_tiempo()
            elif opcion == "2":
                self.mostrar_paises()
            elif opcion == "3":
                self.buscar_pais()
            elif opcion == "4":
                self.buscar_pais_con_frontera()
            elif opcion == "5":
                menuBucle = True
            else:
                print("Opcion invalida")
    
    
    def recargar_tiempo(self):
        os.system("cls")
        print("Recargando tiempo")
        temps = temp_controller.generate_temperatura_obj_arr()
        temp_controller.add_to_db(temps)
        print("Temperaturas recargadas")
        input("Presione cualquier tecla para continuar")
    
    def mostrar_paises(self):
        os.system("cls")
        cursor = myDB.cursor()
        cursor.execute("select paises.nombre, temperaturas.timestamp, temperaturas.temperatura, \
            temperaturas.sensacion, temperaturas.minima, temperaturas.maxima, temperaturas.humedad,\
                temperaturas.amanecer, temperaturas.atardecer from temperaturas join paises on temperaturas.idpais = paises.idpais")
        resultado = cursor.fetchall()
        cursor.close()
        for pais in resultado:
            print(f"Nombre: {pais[0]}")
            print(f"Fecha: {pais[1]}")
            print(f"Temperatura: {pais[2]}")
            print(f"Sensacion: {pais[3]}")
            print(f"Minima: {pais[4]}")
            print(f"Maxima: {pais[5]}")
            print(f"Humedad: {pais[6]}")
            print(f"Amanecer: {pais[7]}")
            print(f"Atardecer: {pais[8]}")
            print("------------------------------------------------------")
        input("Presione cualquier tecla para continuar")
    
    def buscar_pais(self):
        os.system("cls")
        pais = input("Ingrese el nombre del pais: ")
        os.system("cls")
        print("----------------------------------------------")
        cursor = myDB.cursor()
        cursor.execute("select paises.nombre, temperaturas.timestamp, temperaturas.temperatura, \
            temperaturas.sensacion, temperaturas.minima, temperaturas.maxima, temperaturas.humedad,\
                temperaturas.amanecer, temperaturas.atardecer from temperaturas join paises on temperaturas.idpais = paises.idpais\
                    where paises.nombre like %s", (pais,))
        resultado = cursor.fetchall()
        cursor.close()
        for pais in resultado:
            print(f"Nombre: {pais[0]}")
            print(f"Fecha: {pais[1]}")
            print(f"Temperatura: {pais[2]}")
            print(f"Sensacion: {pais[3]}")
            print(f"Minima: {pais[4]}")
            print(f"Maxima: {pais[5]}")
            print(f"Humedad: {pais[6]}")
            print(f"Amanecer: {pais[7]}")
            print(f"Atardecer: {pais[8]}")
            print("------------------------------------------------------")
        input("Presione cualquier tecla para continuar")
    
    def buscar_pais_con_frontera(self):
        os.system("cls")
        pais = input("Ingrese el nombre del pais: ")
        os.system("cls")
        print("----------------------------------------------")
        cursor = myDB.cursor()
        cursor.execute("select \
                distinct p.nombre,\
                t.timestamp,\
                t.temperatura,\
                t.sensacion,\
                t.minima,\
                t.maxima,\
                t.humedad,\
                t.amanecer,\
                t.atardecer\
                FROM\
                    temperaturas t JOIN \
                    paises p ON t.idpais = p.idpais\
                JOIN \
                    fronteras f ON t.idpais = f.idfronteras OR t.idpais = f.idpais\
                WHERE \
                    p.nombre = %s OR f.idpais = (SELECT idpais FROM paises WHERE UPPER(nombre) = UPPER(%s));", (pais,pais))
        resultado = cursor.fetchall()
        cursor.close()
        for pais in resultado:
            print(f"Nombre: {pais[0]}")
            print(f"Fecha: {pais[1]}")
            print(f"Temperatura: {pais[2]}")
            print(f"Sensacion: {pais[3]}")
            print(f"Minima: {pais[4]}")
            print(f"Maxima: {pais[5]}")
            print(f"Humedad: {pais[6]}")
            print(f"Amanecer: {pais[7]}")
            print(f"Atardecer: {pais[8]}")
            print("------------------------------------------------------")
        input("Presione cualquier tecla para continuar")
    
    def cargar_datos(self):
        try:
            paises.guardar_paises(paises.descargar_paises())
            paises_objarr = pais_controller.create_paisObj(pais_controller.get_paises())
            pais_controller.save_paises_DB(paises_objarr)
            fronteras_obj = front.create_fronteraObj(paises_objarr)
            front.add_to_db(fronteras_obj)
            temps = temp_controller.generate_temperatura_obj_arr()
            temp_controller.add_to_db(temps)
        except():
            print("No se pudo descargar los paises")
            
    def print_menu(self):
        print("+------------------------------------+")
        print("|           Menu Principal           |")
        print("+------------------------------------+")
        print("| 1. recargar tiempo                 |")
        print("| 2. mostrar paises                  |")
        print("| 3. buscar un pais                  |")
        print("| 4. buscar un pais con frontera     |")
        print("| 5. salir                           |")
        print("+------------------------------------+")
    

    


if __name__ == "__main__":
    main = Main()
    main.main()
