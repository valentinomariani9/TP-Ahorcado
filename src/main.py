from utils import cargar_palabras, validar_letra
from game import seleccionar_palabra, ocultar_palabra, procesar_intento

def jugar():
    print("🎮 Bienvenido a Ahorcado Flash 🎮")

    # 1. Cargar diccionario de palabras
    diccionario = cargar_palabras()

    # 2. Selección de idioma y dificultad
    idioma = int(input("Elige el idioma:\n1. Español 🇦🇷\n2. English 🇬🇧\n"))
    while (idioma > 2 or idioma < 1):
        idioma = int(input("Por favor ingresá una opción correcta.\n"))
    
    if idioma == 1:
        dificultad = int(input("\nElige la dificultad:\n1. Facil\n2. Medio\n3. Dificil\n"))
    else:
        dificultad = int(input("\nChoose the difficulty:\n1. Easy\n2. Medium\n3. Hard\n"))
    
    while (dificultad > 3 or dificultad < 1):
        if idioma == 1:
            idioma = int(input("Por favor ingresá una opción correcta.\n"))
        else:
            idioma = int(input("Please enter a correct option.\n"))

    # 3. Selección de palabra secreta
    palabra = seleccionar_palabra(diccionario, idioma, dificultad)

    # Inicializar variables
    vidas = 6
    letras_adivinadas = set()
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