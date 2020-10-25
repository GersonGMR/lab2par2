import time
import numpy as np

ejecucion = time.time()

with open('file.txt') as el_archivo:
    leyendo_archivo = list(map(int, el_archivo.read().split('\n')))

def mi_menu():
 
    opcion_correcta = False
    num = 0
    while(not opcion_correcta):
        try:
            num = int(input("Introduce un numero entero del menu: "))
            opcion_correcta = True
        except ValueError:
            print('Error, introduce un numero entero que se encuentre en el menu')
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Ingresar el nombre del archivo de texto para analizar")
    print ("2. Salir")
    print ("Elige una opcion")
 
    opcion = mi_menu()
 
    if opcion == 1:
        print ("Opcion 1")
    elif opcion == 2:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 2")
 
print ("Finalizado")