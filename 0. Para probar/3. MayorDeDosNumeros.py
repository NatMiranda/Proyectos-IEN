numeroA = float(input("Ingrese un primer valor: "))
numeroB = float(input("Ingrese un segundo valor: "))

if numeroA > numeroB:
    print(f"El numero {numeroA} es mayor que el numero {numeroB}")
elif numeroA < numeroB:
    print(f"El numero {numeroB} es mayor que el numero {numeroA}")
else:
    print(f"Los numeros ingresados son iguales. {numeroA} | {numeroB}")