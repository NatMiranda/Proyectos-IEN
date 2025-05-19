#1.- Solicita tres números al usuario y muestra su suma.

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un segundo valor: "))
num3 = int(input("Ingrese un tercer valor: "))

suma = num1 + num2 + num3

print(f"La suma de los numeros es: {suma}")

#2.- Pide al usuario cuatro números y muestra su promedio.

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un segundo valor: "))
num3 = int(input("Ingrese un tercer valor: "))
num4 = int(input("Ingrese un cuarto valor: "))

promedio = (num1 + num2 + num3 + num4) / 4

print(f"El promedio de los 4 numeros es: {promedio}")

#3.- Pide al usuario la base y la altura de un rectángulo y muestra su área.

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = base * altura
print(f"El area del rectangulo es: {area}")

#4.- Declara dos variables con valores numéricos y luego intercambia sus valores.

varUno = 5
varDos = 10

varAux = varUno
varUno = varDos
varDos = varAux

print(f"El valor de A es: {varUno}\nEl valor de B es: {varDos}")

#5.- Concatenación de nombre completo.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print((f"El nombre completo es: {nombre} {apellido}"))
