import random
from .utils import validar_letra

def ocultar_palabra(palabra, letras_adivinadas):
    return "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def seleccionar_palabra(diccionario, idioma, dificultad):
    lista = diccionario[idioma][dificultad]
    return random.choice(lista).upper()

def procesar_intento(palabra, letra, letras_adivinadas, vidas, historial):
    letra = letra.upper()
    if isinstance(letras_adivinadas, str):
        letras_adivinadas = set(l for l in letras_adivinadas if l != "_")
    elif not isinstance(letras_adivinadas, set):
        letras_adivinadas = set(letras_adivinadas)

    if isinstance(vidas, set):
        vidas = len(vidas) if vidas else 5

    if letra in letras_adivinadas:
        mensaje = "⚠️ Ya usaste esa letra"
        progreso = ocultar_palabra(palabra, letras_adivinadas)
        return vidas, progreso, False, mensaje

    letras_adivinadas.add(letra)

    if letra in palabra:
        mensaje = "✅ Acierto!"
        historial.append((letra, "Acierto"))
    else:
        vidas -= 1
        mensaje = f"❌ Fallo. Te quedan {vidas} vidas."
        historial.append((letra, "Fallo"))

    progreso = ocultar_palabra(palabra, letras_adivinadas)

    if "_" not in progreso:
        return vidas, progreso, True, "🏆 ¡Ganaste!"
    if vidas <= 0:
        return vidas, progreso, True, f"💀 Perdiste. La palabra era {palabra}"

    return vidas, progreso, False, mensaje