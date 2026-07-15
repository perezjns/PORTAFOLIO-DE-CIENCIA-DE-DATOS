# Spotify Predictor: Pipeline de Ingeniería de Datos y Modelado

Este proyecto consiste en un pipeline completo de Machine Learning e ingeniería de datos desarrollado en Python. Su propósito principal es analizar, clasificar y predecir el comportamiento comercial (popularidad) y la etiqueta de género de diferentes canciones utilizando el conjunto de datos de Spotify.

El sistema abarca de extremo a extremo la auditoría de calidad del dataset, el análisis estadístico exploratorio (EDA), la preparación matemática de las características físicas del audio, la experimentación con algoritmos supervisados y, finalmente, la consolidación en un objeto predictor orientado a la producción.

---

## 🛠️ Requisitos e Instalación

### 1. Clonar el repositorio
Descarga el código fuente en tu máquina local:

git clone [https://github.com/tu-usuario/spotify-ml-predictor.git](https://github.com/tu-usuario/spotify-ml-predictor.git)
cd spotify-ml-predictor

2. Configurar el Entorno Virtual (Recomendado)
Para asegurar el aislamiento de las librerías y evitar conflictos de dependencias con otros proyectos de tu sistema, ejecuta:

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate

3. Instalar las Dependencias
El proyecto hace uso de librerías científicas y de análisis estándar en el ecosistema de Python. Instálalas con el siguiente comando:

pip install pandas numpy matplotlib seaborn scikit-learn

4. Ubicación del Dataset
Asegúrate de colocar el archivo de origen spotify_tracks.csv en el mismo directorio raíz que el script ejecutable estudio_completo.py. El código está configurado para realizar la lectura de rutas relativas de manera automática.

🚀 Ejecución del Script
Para iniciar el análisis descriptivo completo, entrenar los modelos y validar el predictor final, ejecuta el script principal en tu consola:

python estudio_completo.py

⚠️ Nota sobre la Visualización: El script utiliza la interfaz de Matplotlib/Seaborn para abrir de forma interactiva ventanas gráficas en alta definición (diagramas de distribución de popularidad, balanceo de géneros, mapas de calor de correlación y la matriz de confusión). Es necesario cerrar manualmente cada ventana gráfica para que el script continúe procesando las siguientes fases en la terminal.

🏗️ Arquitectura y Fases del Pipeline

El programa ejecuta de manera secuencial los siguientes módulos lógicos:

Fase 1 y 2: Carga de Datos y Definición de Objetivos

* Carga de Datos: Lectura del CSV mediante pandas con diagnóstico inicial de dimensiones (filas y columnas).

* Definición de Targets: Establecimiento de popularity para la regresión continua y track_genre para la clasificación de categorías.

Auditoría de Calidad

* Análisis automático para identificar registros nulos o campos vacíos.

* Búsqueda y eliminación de registros duplicados exactos para garantizar la integridad de las particiones de entrenamiento y test.

Fase 3: Preprocesamiento y Limpieza Técnica

* Filtrado de Identificadores: Exclusión de campos de texto irrelevantes para los cálculos matemáticos (track_id, artists, album_name, track_name).

* Binarización: Mapeo de campos lógicos booleanos como explicit a valores numéricos (0 y 1).

* Escalado de Características: Transformación lineal mediante MinMaxScaler para proyectar todas las variables predictoras continuas (como la energía, la acústica o el tempo) al intervalo estandarizado [0, 1].

Fases 4 y 6: Visualización Gráfica (EDA)

* Generación de gráficos analíticos para estudiar la densidad de la popularidad y el volumen de muestras por género musical.

* Mapa de calor con la correlación de Pearson para aislar la colinealidad de las variables de audio.

Fase 5: Partición Estratificada del Dataset

* División del conjunto de datos en un 80% para el entrenamiento de algoritmos y un 20% para la evaluación de pruebas (test), utilizando técnicas de estratificación para evitar sesgos distributivos en las variables objetivo.

Fases 7 y 8: Modelado de Regresión (Popularidad)

* Entrenamiento y comparación de tres enfoques técnicos:

* Regresión Lineal Simple: Ajuste básico tomando la variable instrumentalness como única entrada predictora.

* Regresión Lineal Múltiple: Modelo aditivo lineal computando coeficientes para todas las variables físicas del audio.

* Random Forest Regressor: Ensamble de árboles de decisión no lineales para capturar dinámicas y relaciones complejas entre los atributos.

Métricas evaluadas: Error Absoluto Medio (MAE), Raíz del Error Cuadrático Medio (RMSE) y Coeficiente de Determinación (R^2).

Fases 9 y 10: Modelado de Clasificación (Género Musical)

Contraste de dos arquitecturas de clasificación multiclase:

* Máquinas de Vector de Soporte (SVM) con Kernel Lineal: Generación de hiperplanos de separación con margen máximo en espacios vectoriales continuos.

* Random Forest Classifier: Ensamble de bosques aleatorios configurado con pesos balanceados (class_weight='balanced') para neutralizar el desbalance de categorías de destino.

Métricas evaluadas: Reporte de clasificación detallado (Precision, Recall, F1-Score) y visualización interactiva de la Matriz de Confusión.

⚡ Implementación para Producción e Inferencia Final

El pipeline integra un módulo de producción mediante la clase SpotifyPredictor:

* Inicialización y Entrenamiento: La clase encapsula el preprocesamiento, el guardado del escalador Min-Max y entrena los estimadores finales optimizados utilizando el paralelismo de tu procesador (n_jobs=-1).

* Inferencia en Tiempo Real: Cuenta con el método predecir_exito(datos_cancion) que recibe un diccionario de Python con los atributos de una canción y devuelve la predicción del género y su popularidad de 0 a 100.

Ejemplo de Prueba Unitaria de Inferencia

El programa finaliza ejecutando un test de validación enviando una muestra de prueba para verificar el comportamiento de la clase en producción:

cancion_prueba = {
    'duration_ms': 215000,
    'explicit': 0,
    'danceability': 0.82,
    'energy': 0.75,
    'key': 5,
    'loudness': -5.2,
    'mode': 1,
    'speechiness': 0.06,
    'acousticness': 0.12,
    'instrumentalness': 0.0,
    'liveness': 0.08,
    'valence': 0.88,
    'tempo': 118.0,
    'time_signature': 4
}

# Ejecución de la inferencia
resultado = predictor.predecir_exito(cancion_prueba)
print(resultado)