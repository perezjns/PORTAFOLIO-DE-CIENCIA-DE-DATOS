
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
Aquí tienes el contenido limpio, sin etiquetas de citación y listo para copiar en un solo clic:

Markdown
# SpotifyPredictor 🎵🤖

¡Bienvenido a **SpotifyPredictor**! Este proyecto es un ecosistema completo de Machine Learning diseñado para auditar, analizar y predecir el comportamiento comercial y estilístico de pistas musicales en Spotify.

Utilizando un pipeline robusto en Python y Scikit-Learn, el sistema aborda de manera simultánea dos problemas fundamentales de la analítica de datos:
1. **Regresión:** Estimación de la popularidad comercial de una canción (escala 0-100).
2. **Clasificación:** Identificación automatizada del género musical basándose en sus atributos acústicos.

---

## 📊 Arquitectura del Sistema

El núcleo del proyecto está estructurado bajo la clase de producción `SpotifyPredictor`, la cual encapsula todo el ciclo de vida del dato:

+-------------------------------------------------------------+
|                       SpotifyPredictor                      |
+-------------------------------------------------------------+
| - Carga de Modelos y Serializaciones                        |
| - Pipeline Interno de Preprocesamiento (MinMaxScaler)       |
| - Validación de Columnas de Entrada                         |
+-------------------------------------------------------------+
| + predict_popularity(new_track_features)                    |
| + predict_genre(new_track_features)                         |
+-------------------------------------------------------------+


---

## ⚡ Características Principales

* **Auditoría de Calidad:** Limpieza automática del dataset, detección de valores nulos y control de registros duplicados.
* **Pipeline Homogéneo:** Preprocesamiento mediante escalado Min-Max lineal para normalizar variables con rangos masivos (como `duration_ms` o `tempo`) al intervalo [0, 1], evitando sesgos algorítmicos.
* **Visualización en Alta Definición (EDA):** Generación interactiva de gráficos de distribución (KDE de popularidad), balance de clases de géneros y matrices de correlación de Pearson (Heatmaps).
* **Entrenamiento Multimodelo:** Experimentación y evaluación comparativa entre regresores lineales simples/múltiples, Support Vector Machines (SVM) y Random Forests.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Manipulación de Datos:** `pandas`, `numpy`
* **Modelado Predictivo:** `scikit-learn`
* **Visualización Científica:** `matplotlib`, `seaborn`

---

## 🚀 Instalación y Uso Rápido

### 1. Clonar el repositorio e instalar dependencias
```bash
git clone [https://github.com/tu-usuario/SpotifyPredictor.git](https://github.com/tu-usuario/SpotifyPredictor.git)
cd SpotifyPredictor
pip install pandas numpy matplotlib seaborn scikit-learn
2. Estructura del dataset
Asegúrate de colocar tu archivo de datos con el nombre spotify_tracks.csv en la raíz del proyecto. El script procesará automáticamente los atributos musicales clave (danceability, energy, loudness, valence, etc.).

3. Ejecutar el pipeline completo
Bash
python main.py
🧪 Experimentación y Resultados
El script ejecuta un pipeline de pruebas exacto comparando diferentes arquitecturas:

Modelos de Regresión (Popularidad)
Regresión Lineal Simple: Configurado como baseline rápido utilizando únicamente el índice de instrumentalidad (instrumentalness).

Regresión Lineal Múltiple: Utiliza todo el espectro de características acústicas correlacionadas.

Random Forest Regressor: Modelo ensemble configurado para capturar relaciones no lineales complejas.

Modelos de Clasificación (Género Musical)
SVM Lineal: Vector de soporte clásico optimizado mediante regularización C=1.0.

Random Forest Classifier: Ajustado con pesos balanceados (class_weight='balanced') para mitigar cualquier desequilibrio en las muestras de entrenamiento.

💻 Ejemplo de Uso en Producción
Puedes importar la clase integradora para realizar inferencias inmediatas sobre nuevas canciones sin necesidad de relanzar la etapa de experimentación:

Python
from main import SpotifyPredictor

# Inicializar el predictor con el dataframe histórico
predictor = SpotifyPredictor(df)

# Definir los atributos acústicos de una nueva canción
nueva_cancion = {
    'duration_ms': 215000, 'explicit': 0, 'danceability': 0.82, 
    'energy': 0.75, 'key': 5, 'loudness': -5.2, 'mode': 1, 
    'speechiness': 0.06, 'acousticness': 0.12, 'instrumentalness': 0.0, 
    'liveness': 0.08, 'valence': 0.88, 'tempo': 118.0, 'time_signature': 4
}

# Realizar la predicción completa
resultado = predictor.predecir_exito(nueva_cancion)
print(f"Género Sugerido: {resultado['genero_predicho']}")
print(f"Popularidad estimada: {resultado['popularidad_estimada']} / 100")


Desarrollado con pasión por los datos y la música. 🎸
