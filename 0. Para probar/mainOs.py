import time

def intro():
    print("🔮 ¡Bienvenido al Adivinador de Humor Cósmico! 🔮")
    time.sleep(1)
    print("Responderé tu estado de ánimo basándome en tus vibraciones...")
    time.sleep(1.5)
    print("Solo necesitas responder con un 'sí' o un 'no' a las siguientes preguntas.")
    time.sleep(2)

def pregunta(texto):
    while True:
        respuesta = input(f"{texto} (sí/no): ").lower()
        if respuesta in ["sí", "si", "no"]:
            return respuesta == "sí" or respuesta == "si"
        else:
            print("Por favor, responde con 'sí' o 'no'.")

def analizar_respuestas(r1, r2, r3):
    if r1 and r2 and r3:
        return "¡Radiante y lleno de energía positiva! ✨"
    elif r1 and r2 and not r3:
        return "Te sientes alegre, ¡aprovecha este buen momento! 😄"
    elif r1 and not r2 and r3:
        return "Hay una chispa de curiosidad en ti, ¡explórala! 🤔"
    elif r1 and not r2 and not r3:
        return "Pareces tranquilo y relajado. Disfruta de la calma. 😌"
    elif not r1 and r2 and r3:
        return "Sientes algo de entusiasmo y ganas de hacer cosas. ¡Adelante! 💪"
    elif not r1 and r2 and not r3:
        return "Quizás un poco pensativo, pero con una actitud positiva. 😊"
    elif not r1 and not r2 and r3:
        return "Te sientes reflexivo, tal vez buscando inspiración. 💡"
    else:
        return "Hmm... percibo una necesidad de recargar energías. ¡Cuídate! 😴"

def resultado(humor):
    print("\n🌀 Analizando tus respuestas cósmicas...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print(f"¡El Adivinador de Humor Cósmico dice que hoy te sientes: {humor}!")
    time.sleep(2.5)
    print("\n¡Que tengas un día maravilloso! 🌟")

if __name__ == "__main__":
    intro()
    respuesta1 = pregunta("¿Te sientes con mucha energía hoy?")
    respuesta2 = pregunta("¿Has sonreído hoy?")
    respuesta3 = pregunta("¿Tienes curiosidad por aprender algo nuevo?")
    humor_final = analizar_respuestas(respuesta1, respuesta2, respuesta3)
    resultado(humor_final)