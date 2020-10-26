import time

def analisar_archivo():
    # Iniciando tiempo de ejecucion del programa
    ejecucion = time.time()

    # Asignando a la variable path mi ruta del proyecto
    path = "C:/Users/GersonGM/github/lab2par2SH/"

    # Leyendo los datos del archivo proporcionado
    leyendo_archivo = open(path+nombre_archivo, "r")
    datos = leyendo_archivo.read()

    # Convertiendo nuestros datos del archivo a string
    conversion_datos = str(datos)
    mis_datos = conversion_datos

    # Separando las palabras para poder realizar su conteo
    separando_palabras = datos.split()
    cantidad_palabras = len(separando_palabras)
    cantidad_caracteres = len(mis_datos)

    # Realizando conteo de lineas para sumarlas
    leyendo_archivo.readline()
    leyendo_archivo.seek(0)
    cantidad_lineas = len(leyendo_archivo.readlines())
    
    # Realizando separacion de palabras unicas 
    palabras_unicas = set()
    for filas in datos:
        palabras_unicas |= set(filas.split())

    contador_palabras_unicas = len(palabras_unicas)    

    # Cerrando el archivo de texto
    leyendo_archivo.close()
    
    print("Cantidad de palabras: %d \n Cantidad de caracteres: %d \n Cantidad de lineas: %d \n Cantidad de palabras unicas: %d \n" %(cantidad_palabras,cantidad_caracteres,cantidad_lineas,contador_palabras_unicas))
    print('Duracion: {} segundos'.format(time.time() - ejecucion))


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
