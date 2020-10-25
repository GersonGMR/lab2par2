import time
import numpy as np
import glob

ejecucion = time.time()
global nombre_archivo
def analisar_archivo():
    path = "C:/Users/GersonGM/github/lab2par2SH/"
    leyendo_archivo = open(path+nombre_archivo, "r")
    datos = leyendo_archivo.read()
    z = str(datos)
    s = z
    letras_minusculas = 0
    letras_mayusculas = 0
    digitos = 0
    espacios = 0
    others = 0
    x = len(s)
    for i in range(0,x,1):
        if ((ord(s[i]) >= 97) and (ord(s[i]) <= 122)):
            letras_minusculas=letras_minusculas+1
        elif ((ord(s[i]) >= 65) and (ord(s[i]) <= 90)):
            letras_mayusculas+=1
        elif ((ord(s[i]) >= 48) and (ord(s[i]) <= 57)):
            digitos+=1
        elif (ord(s[i])==32):
            espacios+=1
        else:
            others+=1
    print("letras minusculas: %d \n letras mayusculas: %d \n digitos: %d \n espacios: %d \n others: %d \n" %(letras_minusculas,letras_mayusculas,digitos,espacios,others))

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
        nombre_archivo = input ("ingresa el nombre del archivo: ")
        analisar_archivo()
    elif opcion == 2:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 2")
 
print ("Finalizado")
