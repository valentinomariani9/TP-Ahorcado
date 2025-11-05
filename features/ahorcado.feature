Feature: Jugar una partida de Ahorcado Flash
  Como jugador del Ahorcado Flash
  Quiero poder adivinar una palabra secreta
  Para ganar antes de quedarme sin vidas

  Background:
    Given que el juego está iniciado
    And la palabra secreta es "CASA"

  @victoria-perfecta
  Scenario: El jugador gana la partida
    When el jugador ingresa letras correctas sin errores
    Then el sistema muestra "🏆 ¡Ganaste! Adivinaste la palabra correctamente. 🏆"
  
  @victoria-con-errores
  Scenario: El jugador gana la partida con errores
    When el jugador ingresa letras correctas pero con errores
    Then el sistema muestra "🏆 ¡Ganaste! Adivinaste la palabra correctamente. 🏆"

  @derrota-perfecta
  Scenario: El jugador pierde la partida
    When el jugador ingresa letras incorrectas hasta quedarse sin vidas
    Then el sistema muestra "💀 Perdiste. La palabra secreta era: CASA"
  
  @derrota-con-aciertos
  Scenario: El jugador pierde la partida con aciertos
    When el jugador ingresa letras incorrectas y correctas hasta quedarse sin vidas
    Then el sistema muestra "💀 Perdiste. La palabra secreta era: CASA"