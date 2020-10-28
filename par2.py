import time
path = "C:/Users/GersonGM/github/lab2par2SH/"

def analisar_archivo():

def validar_archivo():
    try:
        abrir_archivo = open(path+nombre_archivo)
        abrir_archivo.close()
        print ('Archivo encontrado')
        analisar_archivo()
    except FileNotFoundError:
        print('El archivo no existe')

def validacion_menu():
    opcion_correcta = False
    num = 0
    while(not opcion_correcta):
        try:
            num = int(input("Introduce un numero entero del menu: "))
            opcion_correcta = True
        except ValueError:
            print('Error, introduce un numero entero que se encuentre en el menu')
    return num

while True:
    salir = False
    opcion = 0
    while not salir:
        print ("1. Ingresar el nombre del archivo para analizarlo")
        print ("2. Salir")
        print ("Elige una opcion")
        opcion = validacion_menu()
        if opcion == 1:
            nombre_archivo = input ("ingresa el nombre del archivo con extensión: ")
            validar_archivo()
        elif opcion == 2:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 2")
 
    print ("Finalizado")
