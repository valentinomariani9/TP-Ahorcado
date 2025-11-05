import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from behave import given

URL_JUEGO = "http://localhost:8501?test_word=CASA"


@given("que el juego está iniciado")
def step_iniciar_juego(context):
    print("🚀 Iniciando navegador y abriendo el juego...")

    options = Options()

    if os.getenv("CI", "false") == "true":
        print("🧪 Modo CI detectado → ejecutando en headless.")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")
    else:
        print("Modo local → ejecutando con interfaz visible.")
        options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

    print(f"Abriendo {URL_JUEGO}")
    context.driver.get(URL_JUEGO)

    wait = WebDriverWait(context.driver, 15)
    boton_comenzar = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Comenzar Juego')]"))
    )
    boton_comenzar.click()

    print("Juego iniciado correctamente.")


@given('la palabra secreta es "{palabra}"')
def step_set_palabra(context, palabra):
    context.palabra = palabra.upper()
    print(f"Palabra secreta configurada en contexto: {context.palabra}")

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
    print(f"Buscando mensaje final: {mensaje}")
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

@when("el jugador ingresa letras correctas pero con errores")
def step_letras_correctas_errores(context):
    wait = WebDriverWait(context.driver, 10)
    letras_correctas_errores = ["C", "Q", "A", "Y", "T", "S"]

    print("Ingresando letras...")

    for letra in letras_correctas_errores:
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

@when("el jugador ingresa letras incorrectas y correctas hasta quedarse sin vidas")
def step_letras_incorrectas_aciertos(context):
    wait = WebDriverWait(context.driver, 10)
    letras_incorrectas_aciertos = ["Z", "A", "Q", "W", "Y", "T", "S", "X"]

    print("💣 Ingresando letras incorrectas...")

    for letra in letras_incorrectas_aciertos:
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