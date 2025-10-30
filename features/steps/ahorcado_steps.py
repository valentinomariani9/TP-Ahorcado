from behave import given, when, then
from io import StringIO
import sys
import builtins
import threading
import time
from src.main import jugar


def run_game_with_inputs(inputs):
    
    output = StringIO()
    sys.stdout = output

    entradas = iter(inputs)

    def fake_input(_):
        try:
            return next(entradas)
        except StopIteration: # Siempre devolver algo para evitar bloqueos
            return "A"

    builtins.input = fake_input

    def target():
        try:
            jugar()
        except Exception:
            pass  # Ignora errores si el juego termina forzado

    hilo = threading.Thread(target=target)
    hilo.start()

    # Esperamos hasta 3 segundos a que termine
    for _ in range(30):
        salida = output.getvalue()
        if "Ganaste" in salida or "Perdiste" in salida:
            break
        time.sleep(0.1)

    sys.stdout = sys.__stdout__
    return output.getvalue()


@given("que el juego está iniciado")
def step_iniciado(context):
    context.output = None


@given('la palabra secreta es "CASA"')
def step_palabra(context):
    import src.main 
    src.main.seleccionar_palabra = lambda *args, **kwargs: "CASA"


@when('el jugador ingresa las letras "C", "A" y "S"')
def step_ganar(context):
    context.output = run_game_with_inputs(["1", "1", "C", "A", "S"])


@then('el sistema muestra "🏆 Ganaste"')
def step_verificar_ganar(context):
    salida = context.output or ""
    assert "Ganaste" in salida or "🏆" in salida, f"Salida inesperada:\n\n{salida}"


@when("el jugador ingresa letras incorrectas hasta quedarse sin vidas")
def step_perder(context):
    context.output = run_game_with_inputs(["1", "1", "Z", "X", "Q", "W", "P", "R", "T", "M", "N"])


@then('el sistema muestra "💀 Perdiste"')
def step_verificar_perder(context):
    salida = context.output or ""
    assert "Perdiste" in salida or "💀" in salida, f"Salida inesperada:\n\n{salida}"