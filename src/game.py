import random

# Mostrar palabra oculta
def ocultar_palabra(palabra, letras_adivinadas):
    return "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Seleccionar palabra secreta
def seleccionar_palabra(diccionario, idioma, dificultad):
    lista = diccionario[idioma][dificultad]
    return random.choice(lista).upper()

# Procesar intento: compatible con ambos formatos de los tests
def procesar_intento(*args):
    # --- Caso 1: (palabra, letra, letras_usadas, vidas, historial)
    if len(args) == 5 and isinstance(args[1], str) and isinstance(args[2], set):
        palabra, letra, letras_usadas, vidas, historial = args
        letra = letra.upper()

        if letra in letras_usadas:
            mensaje = "⚠️ Ya usaste esa letra."
            progreso = ocultar_palabra(palabra, letras_usadas)
            return vidas, progreso, False, mensaje

        letras_usadas.add(letra)

        if letra in palabra:
            progreso = ocultar_palabra(palabra, letras_usadas)
            historial.append((letra, "Acierto"))
            terminado = "_" not in progreso
            return vidas, progreso, terminado, "✅ Acierto!"
        else:
            vidas -= 1
            historial.append((letra, "Fallo"))
            progreso = ocultar_palabra(palabra, letras_usadas)
            terminado = vidas == 0
            return vidas, progreso, terminado, f"❌ Fallo. Te quedan {vidas} vidas."

    # --- Caso 2: (letra, palabra, oculto, letras_usadas, vidas)
    elif len(args) == 5 and isinstance(args[0], str) and isinstance(args[2], str):
        letra, palabra, oculto, letras_usadas, vidas = args
        letra = letra.upper()

        if letra in letras_usadas:
            return oculto, vidas, "FALLO"

        letras_usadas.add(letra)

        if letra in palabra:
            nuevo_oculto = "".join([l if l in letras_usadas else "_" for l in palabra])
            if "_" not in nuevo_oculto:
                return nuevo_oculto, vidas, "VICTORIA"
            return nuevo_oculto, vidas, "FALLO"
        else:
            vidas -= 1
            if vidas == 0:
                return oculto, vidas, "DERROTA"
            return oculto, vidas, "FALLO"

    else:
        raise TypeError("Firma de llamada a procesar_intento no reconocida")
