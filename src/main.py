from utils import cargar_palabras, validar_letra
from game import seleccionar_palabra, ocultar_palabra, procesar_intento

def jugar():
    print("\n\n🎮 Bienvenido a Ahorcado Flash 🎮")

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

    # 3. Mapeo de idioma y dificultad
    if idioma == 1:
        idioma = "es"
    else:
        idioma = "en"

    if dificultad == 1:
        dificultad = "easy"
    elif dificultad == 2:
        dificultad = "medium"
    else:
        dificultad = "hard"

    # 4. Selección de palabra secreta
    palabra = seleccionar_palabra(diccionario, idioma, dificultad)

    # Inicializar variables
    vidas = 6
    letras_adivinadas = set()
    historial = []

    if idioma == "es":
        print("\nPalabra secreta:", ocultar_palabra(palabra, letras_adivinadas))
    else:
        print("\nSecret word:", ocultar_palabra(palabra, letras_adivinadas))

    # Bucle principal
    while True:
        if idioma == "es":
            letra_input = input("\nIngresa una letra: ")
        else:
            letra_input = input("\nEnter a letter: ")
        valido, resultado = validar_letra(letra_input, letras_adivinadas, idioma)

        if not valido:
            print(resultado)
            continue

        letra = resultado
        vidas, progreso, fin, mensaje = procesar_intento(
            palabra, letra, letras_adivinadas, vidas, historial, idioma
        )

        print(mensaje)
        if idioma == "es":
            print("Palabra secreta:", progreso)
        else:
            print("Secret word:", progreso)

        if fin:
            if vidas > 0:
                if idioma == "es":
                    print("\n🏆 ¡Ganaste! Adivinaste la palabra correctamente. 🏆\n")
                else:
                    print("\n🏆 You won! You guessed the word correctly. 🏆\n")
            else:
                if idioma == "es":
                    print(f"\n💀 Perdiste. La palabra secreta era: {palabra.upper()}\n")
                else:
                    print(f"\n💀 You lost. The secret word was: {palabra.upper()}\n")

            break

if __name__ == "__main__":
    jugar()