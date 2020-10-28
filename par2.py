import time
path = "C:/Users/GersonGM/github/lab2par2SH/"

def analisar_archivo():
    # Iniciando tiempo de ejecucion del programa
    ejecucion = time.time()
    # Leyendo los datos del archivo proporcionado
    leyendo_archivo = open(path+nombre_archivo, 'r', encoding = "utf8")
    mis_datos = leyendo_archivo.read()
    # Operaciones
    cantidad_caracteres = len(mis_datos)
    cantidad_palabras = len(mis_datos.split())
    cantidad_lineas = len(mis_datos.splitlines())
    # Obteniendo valores unicos con set()
    seperando_palabras = mis_datos.split()
    palabras_unicas = set(seperando_palabras)
    cantidad_palabras_unicas = len(palabras_unicas)
    # Mostrando resultados
    print (" Cantidad de palabras: {} \n Cantidad de caracteres: {} \n Cantidad de lineas: {} \n Cantidad de palabras unicas: {} \n".format(cantidad_palabras,cantidad_caracteres,cantidad_lineas,cantidad_palabras_unicas))
    print('Duracion: {} segundos'.format(time.time() - ejecucion))

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
 
print ("Cerrando el programa")
