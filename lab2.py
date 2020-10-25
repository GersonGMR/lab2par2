import time
import numpy as np

ejecucion = time.time()

with open('file.txt') as el_archivo:
    leyendo_archivo = list(map(int, el_archivo.read().split('\n')))