valorUno = input("Ingrese un primer valor: ")
valorDos = input("Ingrese un segundo valor: ")

valorUno = float(valorUno)
valorDos = float(valorDos)

decisionUsuario = input("1. Suma\n2. Resta\n3. Multiplicación\n4. Division\nIngrese que desea hacer: ")

if decisionUsuario == "1":
    print("La suma de los numeros es: ", valorUno + valorDos)
elif decisionUsuario == "2":
    print("La resta de los numeros es: ", valorUno - valorDos)
elif decisionUsuario == "3":
    print("La multiplicacion de los numeros es: ", valorDos * valorUno)
elif decisionUsuario == "4":
    if valorDos == 0:
        print("No se puede dividir por cero")
    else:
        print("La division de los numeros es: ", valorUno / valorDos)
else:
    print("Gracias por calcular :)")