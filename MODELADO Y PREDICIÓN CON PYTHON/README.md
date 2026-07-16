
# 🎵 estudio_completo

> *Pipeline de Ingeniería de Datos y Modelado de Machine Learning para Spotify.*

**estudio_completo** es un sistema modular diseñado para analizar, clasificar y predecir el éxito comercial y el género musical de pistas de Spotify utilizando sus atributos acústicos.

---

### 🏗️ Fases del Pipeline
El sistema ejecuta una secuencia lógica para garantizar la calidad e integridad del modelo:

| Fase | Descripción |
| :--- | :--- |
| **1-2** | **Carga y Definición:** Lectura de datos y establecimiento de targets (popularidad y género). |
| **Auditoría** | Limpieza automatizada de valores nulos y registros duplicados. |
| **3** | **Preprocesamiento:** Escalado MinMaxScaler [0, 1] y binarización de variables booleanas. |
| **4-6** | **EDA y Correlación:** Análisis gráfico interactivo y estudio de colinealidad. |
| **7-8** | **Regresión:** Modelado de popularidad con Regresión Lineal y Random Forest (MAE, RMSE, R²). |
| **9-10** | **Clasificación:** Modelado de género con SVM y Random Forest (Precision, Recall, F1-Score). |

---

### 🧪 Validación de Inferencia (Prueba Unitaria)
Para validar el comportamiento en producción, el sistema realiza una prueba con una canción real, procesando los siguientes parámetros:

*   **Atributos de Entrada**: 
    `duration_ms: 215000`, `explicit: 0`, `danceability: 0.82`, `energy: 0.75`, `key: 5`, `loudness: -5.2`, `mode: 1`, `speechiness: 0.06`, `acousticness: 0.12`, `instrumentalness: 0.0`, `liveness: 0.08`, `valence: 0.88`, `tempo: 118.0`, `time_signature: 4`.

*   **Resultado de la Inferencia**:
    El método `predecir_exito` procesa estos valores bajo el mismo escalador del entrenamiento para retornar:
    1.  **Género Sugerido**: Clasificación lógica basada en hiperplanos del modelo.
    2.  **Popularidad Estimada**: Valor continuo (0-100) calculado por el ensamble Random Forest.

---

### 🚀 Instalación y Uso

**1. Clonar el repositorio**
```bash
git clone [https://github.com/tu-usuario/estudio_completo.git](https://github.com/tu-usuario/estudio_completo.git)
cd estudio_completo
2. Ejecución
Asegúrate de tener spotify_tracks.csv en la raíz y ejecuta:

Bash
pip install -r requirements.txt
python estudio_completo.py
Nota: El script abrirá ventanas gráficas interactivas; es necesario cerrarlas para continuar con las fases del pipeline.

💡 Inferencia en Producción
Python
from estudio_completo import SpotifyPredictor

# Inferencia rápida con el modelo entrenado
resultado = predictor.predecir_exito(cancion_prueba)
print(f"Género: {resultado['genero_predicho']}, Popularidad: {resultado['popularidad_estimada']}")

Desarrollado con pasión por los datos y la música. 🎸
