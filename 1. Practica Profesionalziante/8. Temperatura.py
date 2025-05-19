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

#Se establecen temperaturas aleatorias para pruebas
registroMaximas = [23, 20, 34, 19, 17, 19]
registroMinimas = [18, 12, 20, 14, 9, 10]

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

opc = 0

#Esta funcion muestra por consola  el dia con la temperatura mas baja

def diaMasBajo(temperatura, dia):
    auxTemp = temperatura[0]
    auxDia = dia[0]
    for i in range(6):
        if temperatura[i] < auxTemp:
            auxTemp = temperatura[i]
            auxDia = dia[i]
    print(f"El dia con la temperatura mas baja fue el {auxDia} con {auxTemp}°C")

#Esta funcion muestra por consola el dia con la temperatura mas alta

def diaMasAlto(temperatura, dia):
    auxTemp = temperatura[0]
    auxDia = dia[0]
    for i in range(6):
        if temperatura[i] > auxTemp:
            auxTemp = temperatura[i]
            auxDia = dia[i]
    print(f"El dia con la temperatura mas alta fue el {auxDia} con {auxTemp}°C")

#Esta funcion establece la temperatura maxima por dia.

def registrarTemperaturaMaxima(dias):
    temperaturas = []
    for i in range(6):
        print("Ingrese la temperatura maxima del dia: ", dias[i]," en celcius.")
        temperaturaMaxima = int(input("--> "))
        temperaturas.append(temperaturaMaxima)
    return temperaturas

#Esta funcion establece la temperatura minima por dia.

def registrarTemperaturaMinima(dias):
    temperaturas = []
    for i in range(6):
        print("Ingrese la temperatura minima del dia: ", dias[i]," en celcius.")
        temperaturaMinima = int(input("--> "))
        temperaturas.append(temperaturaMinima)
    return temperaturas

#Programa principal

while opc != 6:

    #Indice del programa con sus opciones
    opc = int(input(("Bienvenido/a al registro de temperaturas.\n1. Registrar las temperaturas de la semana.\n2. Consultar temperatura maxima de cada dia.\n3. Consultar temperatura minima de cada dia.\n4. Mostrar el dia con la temperatura mas alta\n5. Mostrar el dia con la temperatura mas baja.\n6. Salir.\n--> ")))
    
    #Esta opcion llama las funciones de establecer temperaturas de las lineas 45 y 55
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
    
    #Esta opcion muestra por pantalla la temperatura maxima de todos los dias
    elif opc == 2:
        for i in range(6):
            print(f"La temperatura maxima del dia: ", dias[i], " fue de ", registroMaximas[i], " °C. ")
            time.sleep(0.5)
        print("-" * 10)
    
    #Lo mismo que la anterior pero con las temperaturas minimas
    elif opc == 3:
        for i in range(6):
            print(f"La temperatura minima del dia: ", dias[i], " fue de ", registroMinimas[i], " °C. ")
            time.sleep(0.5)
        print("-" * 10)
    
    #Esta opcion llama a la funcion de la linea 34 y muestra el dia con mayor temperatura
    elif opc == 4:
        print(". . .")
        time.sleep(0.5)
        diaMasAlto(registroMaximas, dias)
        print("-*" * 10)
    
    #Lo mismo que la anterior pero con la temperatura minima.
    elif opc == 5:
        print(". . .")
        time.sleep(0.5)
        diaMasBajo(registroMinimas, dias)
        print("-*" * 10)
    elif opc == 6:
        print("Gracias vuelvas prontos!")
    else:
        print("Opcion no disponible.")

