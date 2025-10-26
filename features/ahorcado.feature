Feature: Jugar una partida de Ahorcado Flash
  Como jugador del Ahorcado Flash
  Quiero poder adivinar una palabra secreta
  Para ganar antes de quedarme sin vidas

  Background:
    Given que el juego está iniciado
    And la palabra secreta es "CASA"

  @victoria
  Scenario: El jugador gana la partida
    When el jugador ingresa las letras "C", "A" y "S"
    Then el sistema muestra "🏆 Ganaste"

  @derrota
  Scenario: El jugador pierde la partida
    When el jugador ingresa letras incorrectas hasta quedarse sin vidas
    Then el sistema muestra "💀 Perdiste"