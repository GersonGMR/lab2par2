import time
import numpy as np
import glob

ejecucion = time.time()

global nombre_archivo

def analisar_archivo():
    path = "C:/Users/GersonGM/github/lab2par2SH/"
    leyendo_archivo = open(path+nombre_archivo, "r")
    datos = leyendo_archivo.read()

    conversion_datos = str(datos)
    mis_datos = conversion_datos

    separando_palabras = datos.split()
    cantidad_palabras = len(separando_palabras)
    cantidad_caracteres = len(mis_datos)

    leyendo_archivo.readline()
    leyendo_archivo.seek(0)
    cantidad_lineas = len(leyendo_archivo.readlines())

    leyendo_archivo.close()

    for i in range(0,cantidad_caracteres,1):
        if ((ord(mis_datos[i]) >= 97) and (ord(mis_datos[i]) <= 122)):
            letras_minusculas=letras_minusculas+1
        elif ((ord(mis_datos[i]) >= 65) and (ord(mis_datos[i]) <= 90)):
            letras_mayusculas+=1
        elif ((ord(mis_datos[i]) >= 48) and (ord(mis_datos[i]) <= 57)):
            digitos+=1
        elif (ord(mis_datos[i])==32):
            espacios+=1
        else:
            others+=1
    
    print("Cantidad de palabras: %d \n Cantidad de caracteres: %d \n Cantidad de lineas: %d \n" 
    %(cantidad_palabras,cantidad_caracteres,cantidad_lineas))


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
 
    print ("1. Ingresar el nombre del archivo con su extension para analizarlo")
    print ("2. Salir")
    print ("Elige una opcion")
 
    opcion = mi_menu()
 
    if opcion == 1:
        nombre_archivo = input ("ingresa el nombre del archivo: ")
        analisar_archivo()
    elif opcion == 2:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 2")
 
print ("Finaliconversion_datosado")
