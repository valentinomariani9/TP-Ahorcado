# TP-Ahorcado
## Trabajo Práctico Integrador Metodologías Ágiles en el Desarrollo de Software
## 👤 Grupo 8️⃣
- Hinternesch Lara Valentina
- Mariani Valentino
- Roca Ramiro Felipe

# 🎮 Ahorcado Flash

*Ahorcado Flash* es un juego digital rápido y entretenido, basado en el clásico **Ahorcado**, desarrollado aplicando la metodología **Scrum**.  
El objetivo es adivinar una palabra secreta antes de quedarse sin vidas, con interfaz simple en consola y soporte para distintas dificultades e idiomas.

## 🚀 Instalación y ejecución

1. Clonar el repositorio o descargar el proyecto.
```bash
git clone https://github.com/tuusuario/TP-Ahorcado-1.git
cd TP-Ahorcado-1
```

2. Asegurarse de tener **Python 3.8+** instalado.

3. Instalar dependencias (opcional, solo para testing):
```bash
pip install -r requirements.txt
```

4. Ejecutar el juego desde la raíz del proyecto:
```bash
python3 python3 -m streamlit run app.py
```

# 🧪 Testing
## Tests Unitarios
Ejecutan pruebas sobre las funciones principales del juego:
```bash
python3 -m pytest -v
```

## Tests de UI
Simulan partidas completas automáticamente:
```bash
python3 -m pytest -v tests/test_ui.py
```

## Tests ATDD (con Behave)
Implementados con lenguaje Gherkin, permiten describir escenarios en lenguaje natural:
```bash
python3 -m behave
```
