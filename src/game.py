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