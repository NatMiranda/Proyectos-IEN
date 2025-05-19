#Estructuras de Decisión

""" Definiciones:
1. Condicional simple
    IF - ELSE - ELSEIF
2. Condicional múltiple
    CASE o SWITCH
3. Operadores lógicos
    And, OR

Definicion:

    Las sentencias de decision o tambien llamadas de CONTROL DE FLUJO 
    son estructuras de control que realizan una pregunta la cual retorna
    verdadero o falso, evaluando una condicion, y selecciona la siguiente 
    instruccion a ejecutar dependiendo la respuesta o resultado.

    Las instrucciones commienzan a ejecutarse de forma secuencial (en orden)
    y cuando se llega a una estructura condicional, la cual está asociada a 
    una condicion, se decide que camino tomar dependiendo siempre del resultado
    de la condicion siendo esta falsa o verdadera

    Cuando se termina de ejecutar este bloque de instrucciones se reanuda la ejecucion
    en la instrucción siguiente a la de la condicional.
"""

a = 5
b = 7

if a > b :
    print("A es mayor")
elif b > a:
    print("B es mayor")
else:
    print("Son iguales")


""" Estructuras de Decisión 

CONDICIONAL SIMPLE

La instruccion [IF] es, por excelencia, la más utilizada para construir estructuras
de control.

"""

#Escribe un programa que tome como entrada las calificaciones de un 
#estudiante en tres asignaturas y calcule su promedio. 
#Luego, determine si el estudiante aprobó o reprobó, considerando 
#que la nota mínima aprobatoria es 60 puntos.
#Son 4 notas por materia - Base de datos, Programación e Ingles.

#Calculo de promedio

def promedio():
    calificacionUno = int(input("Ingrese la primer calificacion: "))
    calificacionDos= int(input("Ingrese la segunda calificacion: "))
    calificacionTres = int(input("Ingrese la tercer calificacion: "))
    calificacionCuatro = int(input("Ingrese la cuarta calificacion: "))
    promedioNotas = (calificacionTres + calificacionDos + calificacionCuatro + calificacionUno) / 4
    return promedioNotas

def imprimirPromedio(promedio , materia):
    if promedio >= 60:
        print(f"El estudiante aprobó {materia} con un promedio de: {promedio}")
    else:
        print(f"El estudiante reprobó {materia} con un promedio de: {promedio}")


#Calculo para base de datos.
print("Ingrese las calificaciones de base de datos")
promedioBase = promedio()
imprimirPromedio = (promedioBase, "base de datos")

#Calculo para programación.
print("Ingrese las calificaciones de programación: ")
promedioProgramacion = promedio()
imprimirPromedio = (promedioProgramacion, "programación")

#Calculo para ingles.
print("Ingrese las calificaciones de ingles: ")
promedioIngles = promedio()
imprimirPromedio(promedioIngles, "inglés")

while a == 5:
    print("Hola")

