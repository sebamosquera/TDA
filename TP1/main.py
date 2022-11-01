import sys
from Socio import *
from Pila import Pila

# recorre todos los conocidos de un socio
# devuelve la cantidad de ellos que cumplan ser invitables
def cantidad_conocidos_invitables(socio):
    conocidos = socio.get_conocidos()
    cantidad = 0
    for c in conocidos:
        if socios[c].es_invitable():
            cantidad += 1
    return cantidad

# apila los conocidos de un socio a una pila
def apilar_conocidos(pila, socio):
    numero_socio = socio.get_numero()
    conocidos = socio.get_conocidos()
    for c in conocidos:
        if socios[c].es_invitable(): #socios[c].get_numero() < numero_socio and
            pila.apilar(socios[c])

k = 4 # minimo de conocidos

socios = {}

# recibe un archivo, carga un diccionario de socios
def cargar_datos(archivo, socios):
    for line in archivo:
        line.replace('\n', '')
        values = line.split(',')
        numero_socio = int(values[0])
        nombre = values[1]
        conocidos = [int(x) for x in values[2:]] # convierte a numeros enteros
        socio = Socio(numero_socio, conocidos, nombre)
        socios[numero_socio] = socio

## CARGA DE DATOS
if(len(sys.argv) > 2):
    n = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    with open(nombre_archivo, "r") as archivo:
        cargar_datos(archivo, socios)
else:
    print("Indicar numero de socios: n\n")
    print("Uso: python main.py n socios.txt")
    sys.exit(1)


## ALGORITMO

pila = Pila()
for s in socios:
    pila.apilar(socios[s])

while not pila.es_vacia():
    socio = pila.desapilar()
    if cantidad_conocidos_invitables(socio) < k:
        socio.desinvitar()
        apilar_conocidos(pila, socio)
        # pila.imprimir()

print("Los invitados serán: ")
for s in socios:
    if socios[s].es_invitable():
        print(socios[s])
