import streamlit as st
import urllib.parse  # 👈 necesario para leer parámetros de la URL
from src.utils import cargar_palabras, validar_letra
from src.game import seleccionar_palabra, ocultar_palabra, procesar_intento


# --- Funciones de Lógica del Juego (Web) ---

def procesar_intento_web(letra_input):
    """
    Procesa un intento del usuario y actualiza el st.session_state.
    """
    idioma = st.session_state.idioma

    valido, resultado = validar_letra(
        letra_input,
        st.session_state.letras_adivinadas,
        idioma=idioma
    )

    if not valido:
        st.session_state.mensaje = resultado
        return

    letra = resultado
    vidas, progreso, fin, mensaje = procesar_intento(
        st.session_state.palabra,
        letra,
        st.session_state.letras_adivinadas,
        st.session_state.vidas,
        st.session_state.historial,
        idioma=idioma
    )

    # Actualizar el estado con los resultados
    st.session_state.vidas = vidas
    st.session_state.mensaje = mensaje
    st.session_state.juego_terminado = fin


# --- Flujo Principal de la Aplicación ---

st.title("🎮 Ahorcado Flash – Grupo 8 🎮")

# ESTADO 1: PANTALLA DE CONFIGURACIÓN
if 'partida_iniciada' not in st.session_state:

    st.subheader("Configura tu partida")

    # Cargar diccionario una sola vez
    if 'diccionario' not in st.session_state:
        st.session_state.diccionario = cargar_palabras()

    idioma_opcion = st.selectbox(
        "Elige el idioma:",
        ("Español 🇦🇷", "English 🇬🇧")
    )

    if idioma_opcion == "Español 🇦🇷":
        dificultad_opcion = st.selectbox(
            "Elige la dificultad:",
            ("Facil", "Medio", "Dificil")
        )
    else:
        dificultad_opcion = st.selectbox(
            "Choose the difficulty:",
            ("Easy", "Medium", "Hard")
        )

    # --- Botón para comenzar el juego ---
    if st.button("Comenzar Juego"):
        # Mapear opciones a claves internas
        idioma_key = "es" if idioma_opcion == "Español 🇦🇷" else "en"
        dificultad_key = "easy"
        if dificultad_opcion in ["Medio", "Medium"]:
            dificultad_key = "medium"
        elif dificultad_opcion in ["Dificil", "Hard"]:
            dificultad_key = "hard"

        # ✅ Verificar si viene palabra de test (por parámetro en URL)
        query_params = st.experimental_get_query_params()
        test_word = query_params.get("test_word", [None])[0]

        if test_word:
            # Si se pasa una palabra por URL, usarla (modo test)
            st.session_state.palabra = test_word.upper()
            print(f"🔧 Palabra de test forzada: {test_word}")
        else:
            # Si no, elegir aleatoriamente del diccionario
            st.session_state.palabra = seleccionar_palabra(
                st.session_state.diccionario,
                idioma_key,
                dificultad_key
            )

        # Inicializar el resto del estado del juego
        st.session_state.vidas = 6
        st.session_state.letras_adivinadas = set()
        st.session_state.historial = []
        st.session_state.juego_terminado = False
        st.session_state.idioma = idioma_key
        st.session_state.mensaje = (
            "¡Adivina la palabra!" if idioma_key == "es" else "Guess the word!"
        )
        st.session_state.partida_iniciada = True
        st.rerun()


# ESTADO 2: PANTALLA DE JUEGO
else:

    idioma = st.session_state.idioma

    progreso_actual = ocultar_palabra(
        st.session_state.palabra,
        st.session_state.letras_adivinadas
    )
    st.header(f"`{progreso_actual}`")

    st.info(st.session_state.mensaje)

    vidas_label = "Vidas restantes" if idioma == "es" else "Lives remaining"
    st.write(f"**{vidas_label}:** {st.session_state.vidas} ❤️")

    # --- Lógica de fin de juego ---
    if st.session_state.juego_terminado:
        if st.session_state.vidas > 0:
            msg_final = (
                "🏆 ¡Ganaste! Adivinaste la palabra correctamente. 🏆"
                if idioma == "es"
                else "🏆 You won! You guessed the word correctly. 🏆"
            )
            st.success(msg_final)
        else:
            msg_final = (
                f"💀 Perdiste. La palabra secreta era: {st.session_state.palabra.upper()}"
                if idioma == "es"
                else f"💀 You lost. The secret word was: {st.session_state.palabra.upper()}"
            )
            st.error(msg_final)

        # Botón para reiniciar
        boton_reiniciar = "Jugar de nuevo" if idioma == "es" else "Play again"
        if st.button(boton_reiniciar):
            diccionario_cacheado = st.session_state.diccionario
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.diccionario = diccionario_cacheado
            st.rerun()

    # --- Lógica de juego activo ---
    else:
        label_input = "Ingresa una letra:" if idioma == "es" else "Enter a letter:"
        label_boton = "Adivinar" if idioma == "es" else "Guess"

        with st.form(key="input_form", clear_on_submit=True):
            letra_usuario = st.text_input(
                label_input,
                max_chars=1,
                key="letra_input"
            )
            submit_button = st.form_submit_button(label=label_boton)

        if submit_button and letra_usuario:
            procesar_intento_web(letra_usuario)
            st.rerun()