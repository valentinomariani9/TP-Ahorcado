from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# --- CONFIGURACIÓN DEL JUEGO WEB ---
URL_JUEGO = "http://localhost:8501?test_word=CASA"  # 👈 fuerza palabra para el test


@given("que el juego está iniciado")
def step_iniciar_juego(context):
    print("🚀 Iniciando navegador y abriendo el juego...")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    context.driver = webdriver.Chrome(options=options)
    context.driver.get(URL_JUEGO)

    wait = WebDriverWait(context.driver, 10)

    # 🔹 Esperar el botón "Comenzar Juego" y hacer clic
    print("⏳ Esperando botón 'Comenzar juego'...")
    boton_comenzar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Comenzar Juego')]")))
    boton_comenzar.click()

    print("🎮 Juego iniciado!")


@given('la palabra secreta es "{palabra}"')
def step_set_palabra(context, palabra):
    # Nota: la palabra se pasa por la URL, así que no se cambia en el DOM
    context.palabra = palabra.upper()
    print(f"📖 Palabra secreta configurada en contexto: {context.palabra}")


@when('el jugador ingresa letras correctas sin errores')
def step_letras_correctas(context):
    wait = WebDriverWait(context.driver, 10)
    letras_correctas = ["C", "A", "S"]

    print("Ingresando letras correctas...")

    for letra in letras_correctas:
        input_letra = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        input_letra.send_keys(letra)
        time.sleep(1)
        boton_adivinar = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adivinar')]"))
        )
        boton_adivinar.click()
        time.sleep(1)

@then('el sistema muestra "{mensaje}"')
def step_verificar_mensaje(context, mensaje):
    print(f"🔍 Buscando mensaje final: {mensaje}")
    wait = WebDriverWait(context.driver, 20)

    try:
        # Espera hasta que el mensaje esté visible en la página
        elemento_mensaje = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{mensaje}')]")
            )
        )
        assert mensaje in elemento_mensaje.text
        print(f"✅ Mensaje encontrado: {elemento_mensaje.text}")

        # Esperamos unos segundos antes de cerrar el navegador
        time.sleep(3)
    except Exception as e:
        print("❌ No se encontró el mensaje esperado o la ventana se cerró antes.")
        print("Error:", e)
        context.driver.save_screenshot("error_final.png")
        raise e

@when("el jugador ingresa letras incorrectas hasta quedarse sin vidas")
def step_letras_incorrectas(context):
    wait = WebDriverWait(context.driver, 10)
    letras_incorrectas = ["Z", "Q", "W", "Y", "T", "X"]  # 6 errores → derrota

    print("💣 Ingresando letras incorrectas...")

    for letra in letras_incorrectas:
        input_letra = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        input_letra.send_keys(letra)
        time.sleep(1)
        boton_adivinar = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adivinar')]"))
        )
        boton_adivinar.click()
        time.sleep(1)