import time
import numpy as np

ejecucion = time.time()

with open('file.txt') as el_archivo:
    leyendo_archivo = list(map(int, el_archivo.read().split('\n')))

def mi_menu():
    print("[1] Ingrese el nombre del archivo a analizar")
    print("[0] Terminar")
mi_menu()
opcion_menu = int (input("Elija una opción del menu: "))