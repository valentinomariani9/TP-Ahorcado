import random

# Mostrar palabra oculta
def ocultar_palabra(palabra, letras_adivinadas):
    return "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Seleccionar palabra secreta
def seleccionar_palabra(diccionario, idioma, dificultad):
    lista = diccionario[idioma][dificultad]
    return random.choice(lista).upper()

# Procesar intento
def procesar_intento(palabra, letra, letras_usadas, vidas, historial, idioma="es"):
    letra = letra.upper()

    if letra in letras_usadas:
        mensaje = "⚠️ Ya usaste esa letra." if idioma == "es" else "⚠️ You already used that letter."
        progreso = ocultar_palabra(palabra, letras_usadas)
        return vidas, progreso, False, mensaje

    letras_usadas.add(letra)

    if letra in palabra:
        progreso = ocultar_palabra(palabra, letras_usadas)
        historial.append((letra, "Acierto"))
        terminado = "_" not in progreso
        mensaje = "✅ ¡Acierto!" if idioma == "es" else "✅ Well done!"
        return vidas, progreso, terminado, mensaje
    else:
        vidas -= 1
        historial.append((letra, "Fallo"))
        progreso = ocultar_palabra(palabra, letras_usadas)
        terminado = vidas == 0
        mensaje = (
            f"❌ Fallo. Te quedan {vidas} vidas." if idioma == "es"
            else f"❌ Failed. You have {vidas} lives left."
        )
        return vidas, progreso, terminado, mensaje
    
def jugar_automatica(palabra_secreta, letras):
    """
    Simula una partida automática de Ahorcado.
    Se usa solo para los tests con Behave (sin pedir input al usuario).
    """
    print("🎮 Bienvenido a Ahorcado Flash 🎮\n")

    # 🔑 Asegurarse de que la palabra esté limpia y en mayúsculas
    palabra_secreta = palabra_secreta.strip().upper()
    palabra = ["_" for _ in palabra_secreta]
    vidas = 6

    print(f"Palabra secreta: {''.join(palabra)}")

    for letra in letras:
    # Limpieza completa: quitar comillas, espacios y puntos
        letra = (
            letra.strip()
            .replace('"', '')
            .replace("'", '')
            .replace(",", '')
            .replace(" ", '')
            .upper()
        )

        if not letra:
            continue  # si quedó vacía, pasar

        if letra in palabra_secreta:
            for i, ch in enumerate(palabra_secreta):
                if ch == letra:
                    palabra[i] = letra
            print("✅ ¡Acierto!")
        else:
            vidas -= 1
            print(f"❌ Fallo. Te quedan {vidas} vidas.")

        print(f"Palabra secreta: {''.join(palabra)}")

        if "_" not in palabra:
            print("\n🏆 ¡Ganaste! Adivinaste la palabra correctamente. 🏆")
            return

        if vidas == 0:
            print(f"\n💀 Perdiste. La palabra secreta era: {palabra_secreta}")
            return