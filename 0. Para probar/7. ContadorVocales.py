vocales = "aeiou"
contador = 0

texto = input("Ingrese un texto: ")

for letra in texto.lower():
    if letra in vocales:
       contador += 1

print(f"En la palabra {texto} hay: {contador} vocales.")