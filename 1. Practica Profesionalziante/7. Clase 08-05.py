"""
# ¿Qué es una lista? 

# Una lista es una sucesion finita de cero, uno o mas elementos del mismo tipo. 
# Desde el punto de vista de las estructuras de datos, una lista es un conjunto 
# finito de elementos, en el que para acceder a uno de ellos hay que pasar por 
# todos los situados antes que él. Una lista es, por lo tanto, una estructura de 
# datos secuencial. Es un conjunto de información del mismo tipo (string, entero, etc)

#Implementación

#Las listas den Python pueden definirse como una secuencia ordenada de elementos 
# encerrados entre cocrchetes y separados por coma. Python sigue una notación 
# especial para representar las listas. Python almacena las listas mediante la 
# utilización de punteros, que referencian la secuencia de elemento y puede 
# diagramarse de la siguiente manera:

#Por ejemplo, una lista con números que van del 1 al 3:
# Milista = [1, 2, 3]
# Podemos asignar listas a variables:
# lista1 = [1, 2, 3]

lista1= [1, 2, 4 ,5]
lista2= [3, 6]
milista3 = lista1 + lista2
print (milista3)

#La función len, aplicada sobre una lista, nos dice cuántos elementos la 
# integran (a partir de la posición 1, no 0):

print("----------------------------------------------------------------------------")

milista = [1,2,9,23]
print(len(milista))

#El operador "*", repite un número dado de veces una lista:

listamulti = [1,2]*2
print (listamulti)

#La forma de referenciar un elemento pparticular en una lista es:

listax = [12, 25, 32, 90]
print (listax[2])

#El operador append(x) permite añadir un elemento en la última posición de la lista:

listaA = [0]*10
listaA.append(8)
print(listaA)

#En caso de que el usuario ingrese el valor

# listaB = ["Jose", "Pedrito"]
# b = input ("ingrese nombre")
# listaB.append(b)
# print (listaB)

#El operador extend() permite concatenar dos listas, aadiendo a la primera la lista que se le indica:

listaExtend = [1,2,3,4]
listaExtend2 = [6,7,8] 
listaExtend.extend(listaExtend2)
print (listaExtend)

#El operador insert(i, x) inserta un elemento en la posición dada. 
# El primer argumento es el índice del elemento antes del que se inserta, 
# por lo que a.insert(0, x) inserta en la primer posición, y a.insert(len(a), 
# x) es lo mismo que a.append(x)

listaInsert = [0,0,0,0,0,0,2,3]
listaInsert.insert(0,2)
print (listaInsert)

#[2,0,0,0,0,0,2,3]

#listaInsert.insert(len(14), 5)

# .remove(), elimina el primer elemento de la lista cuyo valor es x, 
# provoca un error si no existe ese elemento.
# remove(1) elimina el valor 1, y .remove[1] elimina el índice 1

#El Operador index(x)devuelve el índice de la posicióon del primer 
# elemento de la lista cuyo valor sea x. Prvoca un error si no existe el elemento.

#El operador count(x) cuenta la cantidad de apariciones del elemento x en la lista.

listaCount = [2, 0, 0, 0, 0, 0, 0, 0, 3, 4]
listaCount.count(0)
print(listaCount)

#Los operadores sort() y reverse() sirven para ordenar de forma ascendente la 
# lista indicada (sort), y para invertir la lista (reverse).

listaSort = [2, 7, 3, 4, 9, 8]
listaSort.sort()
print (listaSort)

#---------------------------------------

listaSort.reverse()
print (listaSort)

"""



"""
Generar un programa que guarde la temperatura mínima y máxima de 6  días(Lunes a Sábados). 
El programa deberá mostrar la siguiente información:

- La temperatura máxima de cada día.
- Los días con temperatura Mínima.
"""

#Los dias se estableceran por indices (Tanto para temperatura maxima, como minima)
#Lunes:     Indice 0                  (Ya que las temperaturas estan divididas   )
#Martes:    Indice 1                  (por dos listas diferentes.                )
#Miercoles: Indice 2 
#Jueves:    Indice 3 
#Viernes:   Indice 4 
#Sabado:    Indice 5

import time

temperaturaMaxima = 0
temperaturaMinima = 0

registroMaximas = []
registroMinimas = []

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

opc = 0

def diaMasBajo(temperatura, dia):
    auxTemp = temperatura[0]
    auxDia = dia[0]
    for i in range(6):
        if temperatura[i] < auxTemp:
            auxTemp = temperatura[i]
            auxDia = dia[i]
    print(f"El dia con la temperatura mas baja fue el {auxDia} con {auxTemp}°C")

def diaMasAlto(temperatura, dia):
    auxTemp = temperatura[0]
    auxDia = dia[0]
    for i in range(6):
        if temperatura[i] > auxTemp:
            auxTemp = temperatura[i]
            auxDia = dia[i]
    print(f"El dia con la temperatura mas alta fue el {auxDia} con {auxTemp}°C")

def registrarTemperaturaMaxima(dias):
    temperaturas = []
    for i in range(6):
        print("Ingrese la temperatura maxima del dia: ", dias[i]," en celcius.")
        temperaturaMaxima = int(input("--> "))
        temperaturas.append(temperaturaMaxima)
    return temperaturas

def registrarTemperaturaMinima(dias):
    temperaturas = []
    for i in range(6):
        print("Ingrese la temperatura minima del dia: ", dias[i]," en celcius.")
        temperaturaMinima = int(input("--> "))
        temperaturas.append(temperaturaMinima)
    return temperaturas

while opc != 6:

    opc = int(input(("Bienvenido/a al registro de temperaturas.\n1. Registrar las temperaturas de la semana.\n2. Consultar temperatura maxima de cada dia.\n3. Consultar temperatura minima de cada dia.\n4. Mostrar el dia con la temperatura mas alta\n5. Mostrar el dia con la temperatura mas baja.\n6. Salir.\n--> ")))

    if opc == 1:
        print("-*" * 10)
        registroMaximas = registrarTemperaturaMaxima(dias)
        print(". . .")
        time.sleep(1.5)
        print("-*" * 10)
        registroMinimas = registrarTemperaturaMinima(dias)
        print(". . .")
        time.sleep(1.5)
        print("Registro realizado con exito.")
    elif opc == 2:
        for i in range(6):
            print(f"La temperatura maxima del dia: ", dias[i], " fue de ", registroMaximas[i], " °C. ")
            time.sleep(0.5)
        print("-" * 10)
    elif opc == 3:
        for i in range(6):
            print(f"La temperatura minima del dia: ", dias[i], " fue de ", registroMinimas[i], " °C. ")
            time.sleep(0.5)
        print("-" * 10)
    elif opc == 4:
        diaMasAlto(registroMaximas, dias)
    elif opc == 5:
        diaMasBajo(registroMinimas, dias)
    elif opc == 6:
        print("Gracias vuelvas prontos!")
    else:
        print("Opcion no disponible.")

