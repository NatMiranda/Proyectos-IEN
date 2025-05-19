#Escribe un programa que tome como entrada las calificaciones de un 
#estudiante en tres asignaturas y calcule su promedio. 
#Luego, determine si el estudiante aprobó o reprobó, considerando 
#que la nota mínima aprobatoria es 60 puntos.

calificacionUno = int(input("Ingrese la primer calificacion: "))
calificacionDos= int(input("Ingrese la segunda calificacion: "))
calificacionTres = int(input("Ingrese la tercer calificacion: "))

promedio = (calificacionDos + calificacionTres + calificacionUno) / 3

if promedio >= 60:
    print(f"El estudiante aprobo con un promedio de: {promedio}")
else:
    print(f"El estudiante reprobo con un promedio de: {promedio}")