#Implementa una calculadora que permita al usuario calcular 
#el monto final de una inversión, dados el monto inicial, la tasa de 
#interés anual y el número de años de la inversión. El programa debe 
#utilizar la fórmula del interés compuesto.

"""
    principal: El capital inicial (monto de la inversión).
    tasa: La tasa de interés anual (en decimal, por ejemplo, 0.05 para 5%).
    tiempo: El tiempo de la inversión en años.
    frecuencia: La frecuencia con la que se capitaliza el interés por año.
                Por ejemplo:
                  - 1 para anual
                  - 2 para semestral
                  - 4 para trimestral
                  - 12 para mensual
                  - 365 para diario
  """



montoInversion = float(input("Ingrese el monto incial: "))
tasaInteres = float(input("Ingrese la tasa de interes anual: ")) / 100
tiempoInversion = int(input("Indique los años de inversion: "))
frecuenciaPago = int(input("Indique la frecuencia de pago: "))

tasaPorPeriodo = tasaInteres * tiempoInversion
numeroPeriodos = tiempoInversion


montoFinal = 0

print(f"Si empiezas con ${montoInversion} al {tasaInteres}% anual por {tiempoInversion} años tendras al final: ${montoFinal:.2f}")

def calcular_interes_compuesto_simple(principal, tasa_anual, tiempo_en_anios, veces_al_ano):
  """Calcula cuánto dinero tendrás al final con interés compuesto."""

  # Primero, convertimos la tasa anual a la tasa por cada vez que se calcula el interés.
  tasa_por_periodo = tasa_anual / veces_al_ano

  # Calculamos cuántas veces en total se calculará el interés.
  numero_de_periodos = veces_al_ano * tiempo_en_anios

  # Aplicamos la fórmula mágica del interés compuesto.
  monto_final = principal * (1 + tasa_por_periodo) ** numero_de_periodos

  return monto_final

# Vamos a probarlo con el ejemplo de antes:
mi_dinero_inicial = 100
mi_tasa_anual = 0.10  # 10%
mi_tiempo = 3
frecuencia = 1        # Se calcula una vez al año

total_al_final = calcular_interes_compuesto_simple(mi_dinero_inicial, mi_tasa_anual, mi_tiempo, frecuencia)
print(f"Si empiezas con ${mi_dinero_inicial} al {mi_tasa_anual * 100}% anual por {mi_tiempo} años (calculado anualmente), tendrás al final: ${total_al_final:.2f}")

# Probemos ahora si el interés se calcula cada mes:
frecuencia_mensual = 12
total_mensual = calcular_interes_compuesto_simple(mi_dinero_inicial, mi_tasa_anual, mi_tiempo, frecuencia_mensual)
print(f"Si se calcula mensualmente, tendrás al final: ${total_mensual:.2f}")








