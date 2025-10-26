import pytest
from src.main import jugar
import random


# Test 1 - Ganar sin fallos
def test_juego_perfecto(capsys, monkeypatch):
    """El jugador adivina todas las letras correctamente sin fallar."""
    # Forzamos la palabra secreta a "CASA"
    monkeypatch.setattr(random, "choice", lambda _: "CASA")

    entradas = iter(["1", "1", "C", "A", "S"])  # idioma, dificultad, letras correctas
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "✅" in salida
    assert "🏆" in salida or "Ganaste" in salida


# Test 2 - Perder sin aciertos
def test_peor_juego(capsys, monkeypatch):
    """El jugador no acierta ninguna letra."""
    monkeypatch.setattr(random, "choice", lambda _: "CASA")

    entradas = iter(["1", "1", "Z", "X", "Q", "W", "P", "R", "T", "M", "N"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "❌" in salida or "Fallo" in salida
    assert "💀" in salida or "Perdiste" in salida


# Test 3 - Ganar con algunos errores
def test_gano_con_errores(capsys, monkeypatch):
    """El jugador comete algunos errores pero logra ganar."""
    monkeypatch.setattr(random, "choice", lambda _: "CASA")

    entradas = iter(["1", "1", "Z", "C", "A", "S"])  # un error inicial
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "❌" in salida  # hubo errores
    assert "🏆" in salida or "Ganaste" in salida


# Test 4 - Perder con algunos aciertos
def test_pierdo_con_aciertos(capsys, monkeypatch):
    """El jugador acierta algunas letras pero pierde al final."""
    monkeypatch.setattr(random, "choice", lambda _: "CASA")

    entradas = iter(["1", "1", "A", "S", "D", "F", "G", "H", "J", "K", "L"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "✅" in salida  # algunos aciertos
    assert "💀" in salida or "Perdiste" in salida