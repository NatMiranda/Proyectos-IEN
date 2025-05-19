"""
Desarrollar un programa que permita procesar los datos de un vacunatorio de un centro de salud  
contra la gripe. Por cada persona se debe ingresar Género (M para masculino, F para femenino, O otro) 
y edad.

La carga de datos finaliza cuando se ingresa cualquier otro valor distinto de M, F, O como género.

El programa deberá obtener: 

- El género con mayor cantidad de personas vacunadas.
- Cuántas mujeres mayores de 60 años se vacunaron.
- Si hubo algún menor de 12 años vacunado.
"""

#Consideraciones:

"""
Elabore una aplicación de consola en Python.
Podrá hacer uso de los elementos del lenguaje vistos hasta el momento.
Además de la funcionalidad del código se valorará su correcto diseño.
"""
#Version Python 3.13.3
#Variables a utilizar.

edad = 0

#Contadores para cada género que nos servira para mostrar el género
#con mayor cantidad de vacunas.
contadorMasculino = 0
contadorFemenino = 0
contadorOtros = 0
#Contadores para registrar cuantos menores de 12 años
#y cuantas mujeres mayores de 60 han recibido la vacuna.
contadorMenorDoce = 0
contadorMujeresMayores = 0

#Constante inicializada en >m< para que el programa pueda comenzar.
#Luego es utilizada para registrar los géneros.
generoPersona = "m"

print("Bienvenido/a al registro de vacunas.\n- Al finalizar el programa se mostrarán los datos solicitados en la consigna.")

while generoPersona.lower() == "m" or generoPersona.lower() == "f" or generoPersona.lower() == "o":
    print("*-*" * 20)
    print("Primero ingrese la edad de la persona, luego se le solicitara el género.")
    edad = int(input("Ingrese la edad de la persona --> "))

    #Este input registra el género de la persona y en caso de que se coloque otra opcion el programa no funcionaria
    generoPersona = input("Ingrese el genero de la persona\n- 'F' para femenino.\n- 'M' para masculino.\n- 'O' para otros.\nIngrese cualquier otro valor para finalizar el programa.\n-->")
    
    #Aqui con estos if y elif comienzan los registros correspondientes sobre cada genero y edad.
    #Ademas se coloca tanto >m< como >masculino< por ejemplo, ya que se interpreta que
    #el usuario es tonto. Aclaracion: Se utiliza la funcion .lower() para minimizar errores humanos de tipeo.
    
    if generoPersona.lower() == "m" or generoPersona.lower() == "masculino":
        if edad <= 12:
            contadorMenorDoce = contadorMenorDoce + 1
        contadorMasculino = contadorMasculino + 1
        print("Persona registrada con exito.")
    elif generoPersona.lower() == "f" or generoPersona.lower() == "femenino":
        if edad >= 60:
            contadorMujeresMayores = contadorMujeresMayores + 1
        elif edad <= 12:
            contadorMenorDoce = contadorMenorDoce + 1
        contadorFemenino = contadorFemenino + 1
        print("Persona registrada con exito.")
    elif generoPersona.lower() == "o" or generoPersona.lower() == "otros":
        if edad <= 12:
            contadorMenorDoce = contadorMenorDoce + 1
        contadorOtros = contadorOtros + 1
        print("Persona registrada con exito.")
    else:
        print("Gracias por utilizar nuestro programa.")
        break

#Aqui se muestran los datos solicitados en las consignas.
print("Estadisticas:")

#- El género con mayor cantidad de personas vacunadas.

if contadorMasculino > contadorFemenino and contadorMasculino > contadorOtros:
    print(f"El genero Masculino tuvo mas vacunados con un total de: {contadorMasculino} vacunados.")
elif contadorFemenino > contadorMasculino and contadorFemenino > contadorOtros:
    print(f"El genero Femenino tuvo mas vacunados con un total de: {contadorFemenino} vacunados.")
elif contadorOtros > contadorMasculino and contadorOtros > contadorFemenino:
    print(f"El genero Otros tuvo mas vacunados con un total de: {contadorOtros} vacunados.")
else:       #En este Else si hubo la misma cantidad de vacunados nos lo índica.
    print(f"Todos los generos tuvieron la misma cantidad de vacunados: {contadorOtros} por cada genero.")

#- Cuántos menores de 12 años se vacunaron.
print(f"Un total de {contadorMenorDoce} menores de 12 años han sido vacunados.")

#- Cuántas mujeres mayores de 60 años se vacunaron.
print(f"Un total de {contadorMujeresMayores} mujeres mayores de 60 años han sido vacunadas.")

