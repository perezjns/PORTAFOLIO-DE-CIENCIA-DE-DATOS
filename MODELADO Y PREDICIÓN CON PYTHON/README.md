🎵 Spotify ML Predictor: Pipeline de Ingeniería de Datos y ModeladoEste proyecto consiste en un pipeline completo de Machine Learning e ingeniería de datos desarrollado en Python. Su propósito principal es analizar, clasificar y predecir el comportamiento comercial (popularidad) y la etiqueta de género de diferentes canciones utilizando el conjunto de datos de Spotify.El sistema abarca de extremo a extremo la auditoría de calidad del dataset, el análisis estadístico exploratorio (EDA), la preparación matemática de las características físicas del audio, la experimentación con algoritmos supervisados y, finalmente, la consolidación en un objeto predictor orientado a la producción.🛠️ Requisitos e Instalación1. Clonar el repositorioDescarga el código fuente en tu máquina local:Bashgit clone https://github.com/tu-usuario/spotify-ml-predictor.git
cd spotify-ml-predictor
2. Configurar el Entorno Virtual (Recomendado)Para asegurar el aislamiento de las librerías y evitar conflictos de dependencias con otros proyectos de tu sistema, ejecuta:En macOS/Linux:Bashpython3 -m venv venv
source venv/bin/activate
En Windows:Bashpython -m venv venv
venv\Scripts\activate
3. Instalar las DependenciasEl proyecto hace uso de librerías científicas y de análisis estándar en el ecosistema de Python. Instálalas con el siguiente comando:Bashpip install pandas numpy matplotlib seaborn scikit-learn
4. Ubicación del DatasetAsegúrate de colocar el archivo de origen spotify_tracks.csv en el mismo directorio raíz que el script ejecutable estudio_completo.py. El código está configurado para realizar la lectura de rutas relativas de manera automática.🚀 Ejecución del ScriptPara iniciar el análisis descriptivo completo, entrenar los modelos y validar el predictor final, ejecuta el script principal en tu consola:Bashpython estudio_completo.py
⚠️ Nota sobre la Visualización: El script utiliza la interfaz de Matplotlib/Seaborn para abrir de forma interactiva ventanas gráficas en alta definición (diagramas de distribución de popularidad, balanceo de géneros, mapas de calor de correlación y la matriz de confusión). Es necesario cerrar manualmente cada ventana gráfica para que el script continúe procesando las siguientes fases en la terminal.🏗️ Arquitectura y Fases del PipelineEl programa ejecuta de manera secuencial los siguientes módulos lógicos:FaseDescripción1 y 2Carga de Datos y Definición de Objetivos: Lectura del CSV con pandas y establecimiento de popularity (regresión) y track_genre (clasificación).AuditoríaAnálisis automático para identificar registros nulos/vacíos y eliminación de duplicados para garantizar la integridad.3Preprocesamiento y Limpieza Técnica: Filtrado de campos irrelevantes, binarización de booleanos y escalado (MinMaxScaler) al intervalo $[0, 1]$.4 y 6Visualización Gráfica (EDA): Generación de gráficos de densidad y mapas de calor (correlación de Pearson).5Partición Estratificada: División 80% entrenamiento / 20% test, utilizando técnicas para evitar sesgos distributivos.7 y 8Modelado de Regresión: Entrenamiento y comparación de Regresión Lineal (Simple/Múltiple) y Random Forest Regressor.9 y 10Modelado de Clasificación: Contraste de SVM (Kernel Lineal) y Random Forest Classifier con pesos balanceados.⚡ Implementación para Producción e Inferencia FinalEl pipeline integra un módulo de producción mediante la clase SpotifyPredictor:Inicialización y Entrenamiento: Encapsula el preprocesamiento, el guardado del escalador Min-Max y entrena los estimadores finales optimizados utilizando el paralelismo del procesador (n_jobs=-1).Inferencia en Tiempo Real: Cuenta con el método predecir_exito(datos_cancion) que recibe un diccionario de Python con los atributos de una canción y devuelve la predicción del género y su popularidad de 0 a 100.Ejemplo de Prueba Unitaria de InferenciaEl programa finaliza ejecutando un test de validación:Pythoncancion_prueba = { 
    'duration_ms': 215000, 'explicit': 0, 'danceability': 0.82, 'energy': 0.75, 
    'key': 5, 'loudness': -5.2, 'mode': 1, 'speechiness': 0.06, 'acousticness': 0.12, 
    'instrumentalness': 0.0, 'liveness': 0.08, 'valence': 0.88, 'tempo': 118.0, 
    'time_signature': 4 
}

# Ejecución de la inferencia
resultado = predictor.predecir_exito(cancion_prueba)
print(resultado)

📋 Guía de Instalación
Clonar: git clone [https://github.com/tu-usuario/spotify-ml-predictor.git](https://github.com/tu-usuario/spotify-ml-predictor.git)

Entorno Virtual:

Linux/macOS: python3 -m venv venv && source venv/bin/activate

Windows: python -m venv venv && venv\Scripts\activate

Dependencias: pip install pandas numpy matplotlib seaborn scikit-learn

Ejecución: Asegura el archivo spotify_tracks.csv en la raíz y corre python estudio_completo.py.

Nota: El script genera ventanas gráficas interactivas; es necesario cerrarlas manualmente para continuar con el procesamiento.
