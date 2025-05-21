"""
El cine "Cine de la Costa" desea llevar un control detallado de la cantidad de espectadores 
por función ofrecido en un día, incluyendo el nombre de la película, el turno (Mañana, Tarde, Noche) 
y la sala donde se proyectó. El programa debe permitir el ingreso de múltiples funciones durante el día, 
el registro finalizará cuando se ingrese la palabra "FIN" como nombre de la película.

Por cada función se deben ingresar nombre de la película, turno (Mañana, Tarde o Noche), 
sala (entre 1 y 4) y cantidad de espectadores.

Luego determinar:

    Informar la cantidad total de funciones registradas.
    Calcular el total de espectadores.
    Indicar cuántas funciones tuvieron entre 50 y 110 espectadores.
    Contar cuántas funciones registraron exactamente 100, 150 o 200 espectadores.
    Informar si hubo funciones con menos de 20 espectadores.
    Mostrar cuál fue el turno con mayor cantidad de espectadores acumulados.
    Mostrar cuántas funciones se realizaron por cada sala (de la 1 a 4).
    Informar cuál fue la película con mayor asistencia registrada en una sola función.

Consideraciones:

Utilizar los condicionales vistos hasta el momento.
Además de la funcionalidad del código se valorará su correcto diseño.
"""

opcion = ""
opcionTurno = 0
opcionSala = 0
totalFunciones = 0
contadorFuncion50y110 = 0
contadorFuncion100150200 = 0
contadorFuncionMenos20 = 0
contadorTurnoManana = 0
contadorTurnoTarde = 0
contadorTurnoNoche = 0
contadorEspectadoresManana = 0
contadorEspectadoresTarde = 0
contadorEspectadoresNoche = 0
cantidadEspactadoresTotal = 0
contadorSala1 = 0
contadorSala2 = 0
contadorSala3 = 0
contadorSala4 = 0
contadorRapidosyFuriosos = 0
contadorDestinoFinal = 0
        

print("Bienvenido/a al registro de Cines de la Costa.")

while True:

    opcion = int(input("¿Que desea realizar?\n1. Registrar función."))
    
    if opcion == 1:
        
        opcionPelicula = input("Indique la opcion de pelicula:\n1. Rapidos y Furiosos.\n2. Destino Final.")
        if opcionPelicula == 1:
            nombrePelicula = "Rapidos y furiosos"
            contadorRapidosyFuriosos = contadorRapidosyFuriosos + 1
        elif opcionPelicula == 2:
            nombrePelicula = "Destino Final"
            contadorDestinoFinal = contadorDestinoFinal + 1
        else:
            print("Opcion Invalida")
        
        opcionTurno = int(input("Ingrese el turno:\n1. Mañana.\n2. Tarde.\n3. Noche."))
        if opcionTurno == 1:
            contadorTurnoManana = contadorTurnoManana + 1
            contadorEspectadoresManana = int(input("Ingrese la cantidad de espectadores por la mañana --> "))
        elif opcionTurno == 2:
            contadorTurnoTarde = contadorTurnoTarde + 1
            contadorEspectadoresTarde = int(input("Ingrese la cantidad de espectadores por la tarde --> "))
        elif opcionTurno == 3:
            contadorTurnoNoche = contadorTurnoNoche + 1
            contadorEspectadoresNoche = int(input("Ingrese la cantidad de espectadores por la noche --> "))
        else:
            print("Opcion Invalida")
        
        opcionSala = int(input("Ingrese el numero de sala (1 , 2 , 3 , 4) --> "))
        if opcionSala == 1:
            contadorSala1 = contadorSala1 + 1 
        elif opcionSala == 2:
            contadorSala2 = contadorSala2 + 1
        elif opcionSala == 3:
            contadorSala3 = contadorSala3 + 1
        elif opcionSala == 4:
            contadorSala4 = contadorSala4 + 1
        else:
            print("Opcion Invalida")
        

        


