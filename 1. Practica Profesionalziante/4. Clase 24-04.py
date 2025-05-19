#Condicional Multiple    #Programación y Practica Profesionalizante

"""
Switch es otra de las instrucciones que permiten la construccion de estructuras
de control.

A diferencia de if, para controlar el flujo por medio de una sentencia switch
se debe de combinar con el uso de las sentencias case y break.

Cualquier numero de casos a evaluar
"""

#Estructuras de Interacción

"""
1. ¿Que es una iteración?
2. FOR
3. WHILE
4. DO [...] WHILE
5. Contadores
6. Acumuladores

Las sentencias de itercion o ciclos son estructuras de control que repiten la ejecucion de un grupo de instrucciones

Una sentencia de iteracion es una estructura de control condicional, ya que dentro de la misma
se repite la ejecucion de una o mas instruciones mientras que una condicion especifica se cumpla

muchas veces tenemos que repetir un numero definido o indefinico de veces un grupo de instrucciones

FOR

La sentencia for es útil para los casos en donde se conoce de antemano el numero de veces que una o mas 
sentencias han de repetirse

WHILE

La sentencia while es util en aquellos casos en donde no se conoce de antemano el numero de veces 
que una o mas sentencias se tienen que repetir

Es decir, mientras se cumpla mi condicion se ejecutara el codigo

    while true: 
    
DO [...] WHILE

La sentencia do es usada generalmente en cooperacion con while para garantizar que una o mas instrucciones
se ejecuten al menos una vez.

BREAK - CONTINUE

En la condicion switch, la sentencia break es utilizada con el proposito de forzar un salto dentro del
bloque switch hacia el final del mismo.
	
	Mientras opc =! 3 Hacer
		Escribir "¿Que barrio quiere consultar?";
		Escribir "1. Barrios Zona Norte.";
		Escribir "2. Barrios Zona Sur.";
		Escribir "3. Finalizar programa";
		Leer opc;
		
		Segun opc Hacer
			1:
				contadorZonaNorte <- contadorZonaNorte + 1;
				Escribir "-------------";
				Escribir "1. Barrio Paykin.";
				Escribir "2. Barrio Atlantico sur.";
				Escribir "3. Villa Rio Negro.";
				
				Escribir "Ingrese el numero de Barrio que quiere consultar";
				Leer opc2;
			2:
				secuencia_de_acciones_2
			3:
				secuencia_de_acciones_3
			De Otro Modo:
				secuencia_de_acciones_dom
		FinSegun
		
		
		
	FinMientras
	
FinProceso

"""
