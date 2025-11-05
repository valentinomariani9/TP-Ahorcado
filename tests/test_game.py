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
    assert oculto == "______"

def test_ocultar_palabra_con_aciertos():
    palabra = "PERRO"
    oculto = ocultar_palabra(palabra, ["R"])
    assert oculto == "__RR_"

# Sprint 4
def test_validar_letra_valida():
    letras_usadas = set()
    ok, letra = validar_letra("a", letras_usadas)
    assert ok is True
    assert letra == "A"

def test_validar_letra_invalida():
    letras_usadas = set()
    ok, mensaje = validar_letra("1", letras_usadas)
    assert ok is False
    assert mensaje == "⚠️ Ingresá solo una letra."

def test_procesar_intento_acierto():
    palabra = "GATO"
    letras_usadas = set()
    historial = []
    vidas = 5

    vidas, progreso, terminado, mensaje = procesar_intento(
        palabra,    # palabra secreta
        "A",        # letra que intenta
        letras_usadas,
        vidas,
        historial,
        idioma="es"
    )

    assert "A" in progreso
    assert terminado is False
    assert vidas == 5
    assert mensaje == "✅ ¡Acierto!"

def test_procesar_intento_fallo():
    palabra = "GATO"
    letras_usadas = set()
    historial = []
    vidas, progreso, terminado, mensaje = procesar_intento(
        palabra,
        "Z",
        letras_usadas,
        5,
        historial,
        idioma="es"
    )

    assert progreso == "____"
    assert vidas == 4
    assert terminado is False
    assert "Fallo" in mensaje

def test_procesar_intento_victoria():
    palabra = "SOL"
    letras_usadas = {"S", "L"}
    historial = []
    vidas, progreso, terminado, mensaje = procesar_intento(
        palabra,
        "O",
        letras_usadas,
        5,
        historial,
        idioma="es"
    )

    assert progreso == "SOL"
    assert terminado is True
    assert "Acierto" in mensaje or "Well done" in mensaje

def test_procesar_intento_derrota():
    palabra = "SOL"
    letras_usadas = set()
    historial = []
    vidas, progreso, terminado, mensaje = procesar_intento(
        palabra,
        "X",
        letras_usadas,
        1,
        historial,
        idioma="es"
    )

    assert vidas == 0
    assert terminado is True
    assert "vidas" in mensaje or "lives" in mensaje