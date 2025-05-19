import random

def generar_combinacion():
    return sorted(random.sample(range(46), 6))

tu_combinacion = sorted([23, 18, 35, 4, 14, 28])

for _ in range(5):  # Ejecutar el programa principal 5 veces
    intentos = 0
    encontrado = False

    while not encontrado:
        intentos += 1
        combinacion_sorteada = generar_combinacion()
        if combinacion_sorteada == tu_combinacion:
            encontrado = True

    print(f"Intento {_ + 1}: Se necesitaron {intentos - 1} intentos fallidos antes de que saliera la combinación {tu_combinacion}.")

print("\nEl programa se ha ejecutado 5 veces.")