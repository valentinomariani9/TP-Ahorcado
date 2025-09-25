import pytest
from src.utils import cargar_palabras, validar_letra
from src.game import seleccionar_palabra, ocultar_palabra, procesar_intento

# Sprint 1
def test_cargar_palabras_tamano_correcto():
    diccionario = cargar_palabras()
    palabras = diccionario["es"]["easy"]
    assert len(palabras) == 5

def test_cargar_palabras_no_repetidas():
    diccionario = cargar_palabras()
    palabras = diccionario["es"]["easy"]
    assert len(palabras) == len(set(palabras))

def test_cargar_palabras_no_vacias():
    diccionario = cargar_palabras()
    palabras = diccionario["es"]["easy"]
    assert all(palabra.strip() != "" for palabra in palabras)

# Sprint 2
def test_seleccionar_palabra_esta_en_lista():
    diccionario = cargar_palabras()
    palabra = seleccionar_palabra(diccionario, "es", "easy")
    assert palabra.lower() in diccionario["es"]["easy"]

def test_seleccionar_palabra_no_nula():
    diccionario = cargar_palabras()
    palabra = seleccionar_palabra(diccionario, "es", "easy")
    assert palabra is not None and palabra != ""

# Sprint 3
def test_ocultar_palabra_inicial():
    palabra = "PERRO"
    oculto = ocultar_palabra(palabra, [])
    assert oculto == "_____"

def test_ocultar_palabra_con_aciertos():
    palabra = "PERRO"
    oculto = ocultar_palabra(palabra, ["R"])
    assert oculto == "__RR_"