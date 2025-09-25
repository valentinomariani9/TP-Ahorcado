from utils import cargar_palabras, validar_letra
from game import seleccionar_palabra, ocultar_palabra, procesar_intento

def jugar():
    print("🎮 Bienvenido a Ahorcado Flash 🎮")

    # 1. Cargar diccionario de palabras
    diccionario = cargar_palabras()

    # 2. Selección de idioma y dificultad
    idioma = input("Elige idioma (es/en): ").lower()
    dificultad = input("Elige dificultad (easy/medium/hard): ").lower()

    # 3. Selección de palabra secreta
    palabra = seleccionar_palabra(diccionario, idioma, dificultad)

    # Inicializar variables
    vidas = 6
    letras_adivinadas = []
    historial = []

    print(f"\nDificultad elegida: {dificultad}")
    print("Palabra secreta:", ocultar_palabra(palabra, letras_adivinadas))

    # Bucle principal
    while True:
        letra_input = input("\nIngresa una letra: ")
        valido, resultado = validar_letra(letra_input, letras_adivinadas)

        if not valido:
            print(resultado)
            continue

        letra = resultado
        vidas, progreso, fin, mensaje = procesar_intento(
            palabra, letra, letras_adivinadas, vidas, historial
        )

        print(mensaje)
        print("Progreso:", progreso)

        if fin:
            print("Historial de intentos:", historial)
            break


if __name__ == "__main__":
    jugar()