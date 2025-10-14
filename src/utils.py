import json
import os

def cargar_palabras(path=None):
    if path is None:
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "palabras.json")
    if not os.path.exists(path):
        raise FileNotFoundError("No se encontró el archivo de palabras.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validar_lista_palabras(lista):
    if len(lista) != 5:
        return False, "❌ La lista tiene ",len," palabras, debe tener 5."
    if len(lista) != len(set(lista)):
        return False, "❌ La lista contiene palabras repetidas"
    for palabra in lista:
        if not palabra or palabra.strip() == "":
            return False, "❌ Hay palabras vacías o nulas"
        if not palabra.isalpha():
            return False, f"❌ La palabra '{palabra}' contiene caracteres inválidos"
    return True, "✅ Lista válida"

def validar_letra(letra, letras_usadas, idioma="es"):
    letra = letra.upper()
    if len(letra) != 1 or not letra.isalpha():
        if idioma == "es":
            return False, "⚠️ Ingresá solo una letra."
        else:
            return False, "⚠️ Enter only one letter."
    if letra in letras_usadas:
        if idioma == "es":
            return False, "⚠️ Ya usaste esa letra."
        else:
            return False, "⚠️ You already used that letter."
    return True, letra
