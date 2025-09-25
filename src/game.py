import random
from utils import validar_letra

# Mostrar palabra oculta con guiones (Sprint 3)
def ocultar_palabra(palabra, letras_adivinadas):
    return "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Seleccionar palabra secreta (Sprint 2)
def seleccionar_palabra(diccionario, idioma, categoria):
    lista = diccionario[idioma][categoria]
    return random.choice(lista).upper()

# Procesar intento (Sprint 5)
def procesar_intento(palabra, letra, letras_adivinadas, vidas, historial):
    if letra in palabra:
        letras_adivinadas.append(letra)
        historial.append((letra, "Acierto"))
        mensaje = "✅ Acierto!"
    else:
        vidas -= 1
        historial.append((letra, "Fallo"))
        mensaje = f"❌ Fallo. Te quedan {vidas} vidas."

    progreso = ocultar_palabra(palabra, letras_adivinadas)

    if "_" not in progreso:
        return vidas, progreso, True, "🏆 ¡Ganaste!"
    if vidas == 0:
        return vidas, progreso, True, f"💀 Perdiste. La palabra era {palabra}"

    return vidas, progreso, False, mensaje