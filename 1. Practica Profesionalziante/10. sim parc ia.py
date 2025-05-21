def procesar_vacunacion():
    print("Bienvenido/a al registro de vacunas.")
    print("------------------------------------")

    # Contadores
    vacunados_por_genero = {'m': 0, 'f': 0, 'o': 0}
    mujeres_mayores_60 = 0
    menores_12 = 0
    total_personas_vacunadas = 0

    while True:
        try:
            print("\n--- Ingrese datos de la persona ---")
            edad = int(input("Ingrese la edad de la persona: "))

            if not (0 <= edad <= 120): # Pequeña validación de edad
                print("Edad inválida. Por favor, ingrese una edad entre 0 y 120.")
                continue

            genero_input = input("Ingrese el género ('M' para masculino, 'F' para femenino, 'O' para otros).\n"
                                 "Ingrese cualquier otro valor para finalizar: ").lower()

            if genero_input not in ['m', 'f', 'o']:
                print("Valor de género no reconocido. Finalizando el programa.")
                break

            # Actualizar contadores por género
            vacunados_por_genero[genero_input] += 1
            total_personas_vacunadas += 1

            # Contadores específicos
            if genero_input == 'f' and edad >= 60:
                mujeres_mayores_60 += 1
            
            if edad < 12:
                menores_12 += 1
            
            print("Persona registrada con éxito.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para la edad.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    print("\n--- Estadísticas de vacunación ---")
    if total_personas_vacunadas == 0:
        print("No se registraron personas vacunadas.")
        return

    # Género con mayor cantidad de personas vacunadas
    genero_mas_vacunado = max(vacunados_por_genero, key=vacunados_por_genero.get)
    cantidad_mas_vacunados = vacunados_por_genero[genero_mas_vacunado]

    # Convertir 'm', 'f', 'o' a nombres legibles para la salida
    mapa_genero = {'m': 'Masculino', 'f': 'Femenino', 'o': 'Otros'}
    
    # Verificar si hay empates en el género con mayor cantidad
    generos_con_max = [g for g, count in vacunados_por_genero.items() if count == cantidad_mas_vacunados]

    if len(generos_con_max) > 1:
        nombres_empate = [mapa_genero[g] for g in generos_con_max]
        print(f"Múltiples géneros tuvieron la misma cantidad de vacunados ({cantidad_mas_vacunados}): {', '.join(nombres_empate)}.")
    else:
        print(f"El género con mayor cantidad de vacunados fue **{mapa_genero[genero_mas_vacunado]}** con **{cantidad_mas_vacunado}** personas.")

    # Cuántas mujeres mayores de 60 años se vacunaron
    print(f"Un total de **{mujeres_mayores_60}** mujeres mayores de 60 años fueron vacunadas.")

    # Si hubo algún menor de 12 años vacunado
    if menores_12 > 0:
        print(f"Sí, se vacunaron **{menores_12}** menores de 12 años.")
    else:
        print("No hubo ningún menor de 12 años vacunado.")

# Ejecutar el programa
procesar_vacunacion()