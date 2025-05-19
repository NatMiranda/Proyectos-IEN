"""
Un centro de donaciones de sangre necesita registrar a las personas que se presentan
para donar en un dia. Para ello, se ingresa la informacion de cada donante como ser
    -Nombre.
    -Edad.
    -Tipo de sangre.
El registro de donantes continua mientras el operador no ingresa el nommbre "FIN".

Desarrolle un algoritmo que:
    -Cuente la cantidad total de donantes registrados.
    -Contar cuantas donaciones se hicieron para cada tipo de sangre.
    -Para cada registro, solo se debe aceptar la donacion si el donante es mayor de 18 años.

"""

import time

#Variables para cada persona
nombrePersona = ""
edadPersona = 0
tipoSangre = 0

#Variables de Sangre Factor Positivo
contadorAPOS = 0
contadorBPOS = 0
contadorABPOS = 0
contadorOPOS = 0
#Variables de Sangre Factor Negativo
contadorANEG = 0
contadorBNEG = 0
contadorABNEG = 0
contadorONEG = 0

opcion = 0
def personaRegistrada():
    print(". . .")  
    time.sleep(1.5)
    print("Persona registrada con exito.")

while opcion != 4:

    opcion = int(input("Ingrese que desea realizar:\n1. Registrar donante\n2. Consultar total de donantes\n3. Consultar donantes por tipo de sangre.\n4. Finalizar programa\n--> "))

    if opcion == 1:
        nombrePersona = input("Ingrese el nombre de la persona ->")
        edadPersona = int(input("Ingrese la edad de la persona -> "))
        if edadPersona < 18:
            print(f"{nombrePersona} no está en edad de donar sangre.")
        elif edadPersona >= 18:
            tipoSangre = int(input(f"Ingrese el tipo de sangre que posee {nombrePersona}\n1. Factor A+\n2. Factor A-\n3. Factor B+\n4. Factor B-\n5. Factor AB+\n6. Factor AB-\n7. Factor 0+\n8. Factor 0-\n0. Cancelar\n--> "))
            if tipoSangre == 1:
                contadorAPOS = contadorAPOS + 1
                personaRegistrada()
            elif tipoSangre == 2:
                contadorANEG = contadorANEG + 1
                personaRegistrada()
            elif tipoSangre == 3:
                contadorBPOS = contadorBPOS + 1
                personaRegistrada()
            elif tipoSangre == 4:
                contadorBNEG = contadorBNEG + 1
                personaRegistrada()
            elif tipoSangre == 5:
                contadorABPOS = contadorABPOS + 1
                personaRegistrada()
            elif tipoSangre == 6:
                contadorABNEG = contadorABNEG + 1
                personaRegistrada()
            elif tipoSangre == 7:
                contadorOPOS = contadorOPOS + 1
                personaRegistrada()
            elif tipoSangre == 8:
                contadorONEG = contadorONEG + 1
                personaRegistrada()
            elif tipoSangre == 0:
                personaRegistrada()
            else:
                print("Opcion no disponible.")
    elif opcion == 2:
        totalDonantes = contadorAPOS + contadorANEG + contadorBPOS + contadorBNEG + contadorABPOS + contadorBNEG + contadorOPOS + contadorONEG
        print(f"El total de donantes registrados es de: {totalDonantes}")
    elif opcion == 3:
        print(f"El total de donantes por tipo de sangre son: \n -Factor A+: {contadorAPOS}\n -Factor A-: {contadorANEG}\n -Factor B+: {contadorBPOS}\n -Factor B-: {contadorBNEG}\n -Factor AB+: {contadorABPOS}\n -Factor AB-: {contadorABNEG}\n -Factor 0+: {contadorOPOS}\n -Factor O-: {contadorONEG}")
    elif opcion == 4:
        print(". . .")
        time.sleep(1.5)
        print("Gracias por utilizar nuestro programa :)")
        
    