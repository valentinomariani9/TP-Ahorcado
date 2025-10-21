import pytest
from src.main import jugar

def test_juego_completo_fallo(capsys, monkeypatch):
    """Simula una partida donde el jugador pierde todas las vidas."""
    entradas = iter(["1", "1", "a", "e", "i", "o", "u", "s", "p", "r", "t", "l"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "💀" in salida or "Perdiste" in salida or "Fallaste" in salida


def test_juego_completo_victoria(capsys, monkeypatch):
    """Simula una partida donde el jugador gana (palabra fija)."""

    # Forzamos que la palabra secreta sea "CASA"
    import random
    monkeypatch.setattr(random, "choice", lambda _: "CASA")

    # Entradas suficientes para descubrir CASA
    entradas = iter(["1", "1", "C", "A", "S"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out

    assert "🎮 Bienvenido a Ahorcado Flash 🎮" in salida
    assert "🏆" in salida or "Ganaste" in salida or "Victoria" in salida