# 🎵 Spotify ML Predictor

> *Un pipeline de extremo a extremo para la ciencia de datos musical.*

Spotify ML Predictor es una herramienta robusta diseñada para analizar, clasificar y predecir el éxito comercial y el género de canciones basándose en sus atributos acústicos. Este proyecto demuestra el ciclo de vida completo de un modelo de Machine Learning: desde la auditoría de datos hasta la creación de un predictor listo para producción.

---

### 🛠 Tech Stack

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
* ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

### 🏗️ Arquitectura del Pipeline

El flujo de trabajo está diseñado de forma modular para garantizar la integridad y escalabilidad:

| Fase | Descripción |
| :--- | :--- |
| **Data Audit** | Limpieza de nulos, duplicados y auditoría de calidad. |
| **Preprocessing** | Escalado con `MinMaxScaler`, binarización y feature selection. |
| **EDA** | Visualización interactiva (Correlaciones, Distribuciones). |
| **Regresión** | Modelos Lineales y *Random Forest* para predecir popularidad. |
| **Clasificación** | SVM y *Random Forest* para categorización de géneros. |

---

### 🚀 Instalación y Uso

**1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/spotify-ml-predictor.git
cd spotify-ml-predictor
2. Configurar entorno virtual

Bash
# macOS/Linux
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && venv\Scripts\activate
3. Ejecución
Asegúrate de tener spotify_tracks.csv en la raíz y ejecuta:

Bash
pip install -r requirements.txt
python estudio_completo.py
Nota: El script abrirá ventanas gráficas interactivas. Ciérralas para avanzar a la siguiente fase.

💡 Implementación en Producción
El pipeline incluye una clase SpotifyPredictor encapsulada para facilitar la inferencia en tiempo real:

Python
from predictor import SpotifyPredictor

# Inferencia rápida
cancion_prueba = {'danceability': 0.82, 'energy': 0.75}
resultado = predictor.predecir_exito(cancion_prueba)
print(f"Predicción: {resultado}")
📊 Modelos y Métricas
Regresión: Evaluamos MAE, RMSE y R^2 para asegurar precisión en la popularidad.

Clasificación: Reportes detallados de Precision, Recall y F1-Score para el género musical.

🌟 ¿Qué hace especial a este proyecto?
Diseño orientado a la producción: No solo analiza, sino que exporta un objeto listo para inferencia.

Validación robusta: Uso de partición estratificada para evitar sesgos distributivos.

Enfoque técnico: Uso de algoritmos no lineales (Random Forest) para capturar dinámicas complejas.

Desarrollado con pasión por los datos y la música. 🎸
