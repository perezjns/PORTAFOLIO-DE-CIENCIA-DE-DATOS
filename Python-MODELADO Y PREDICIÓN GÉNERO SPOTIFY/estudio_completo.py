import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Algoritmos de Modelado
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVC

# Métricas de Evaluación
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, ConfusionMatrixDisplay
)

# Desactivar advertencias innecesarias en consola
warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")

# ==========================================
# FASE 1 & 2: EXTRACCIÓN Y SEPARACIÓN DE VARIABLES
# ==========================================

def cargar_y_analizar_datos(data_path):
    print("=== FASE 1: INFORMACIÓN BÁSICA DEL DATASET ===")
    df = pd.read_csv(data_path)
    print(f"Dimensiones del dataset: {df.shape[0]} filas, {df.shape[1]} columnas.")
    print(f"Nombres de las columnas:\n{list(df.columns)}\n")
    
    print("=== FASE 2: DEFINICIÓN DE VARIABLES ===")
    X = df.copy()
    y_regression = df['popularity']
    y_classification = df['track_genre']
    
    columnas_numericas = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    columnas_booleanas = X.select_dtypes(include=['bool']).columns.tolist()
    
    print(f"Columnas Numéricas: {len(columnas_numericas)} columnas.")
    print(f"Columnas Booleanas: {columnas_booleanas}\n")
    return df, X, y_regression, y_classification, columnas_numericas, columnas_booleanas

# ==========================================
# FASE 3: LIMPIEZA Y PREPROCESAMIENTO
# ==========================================

def preprocesar_datos(df, columnas_booleanas):
    print("=== FASE 3: PREPROCESAMIENTO ===")
    X_limpio = df.drop(columns=['track_id', 'artists', 'album_name', 'track_name', 'popularity', 'track_genre'])
    X_limpio[columnas_booleanas] = X_limpio[columnas_booleanas].astype(int)
    
    scaler = MinMaxScaler()
    X_escalado = pd.DataFrame(scaler.fit_transform(X_limpio), columns=X_limpio.columns)
    
    print("Muestra de datos normalizados:")
    print(X_escalado.head(2))
    print()
    return X_escalado, scaler

# ==========================================
# FASE 4: ANÁLISIS ESTADÍSTICO EXPLORATORIO (EDA)
# ==========================================

def realizar_eda(df, y_regression, y_classification):
    print("=== FASE 4: ANÁLISIS ESTADÍSTICO (EDA) ===")
    print("Estadísticas descriptivas de la Popularidad:")
    print(y_regression.describe())
    
    print("\nDistribución de las clases en el género musical:")
    print(y_classification.value_counts())
    print()
    
    # 🖼️ MOSTRAR GRÁFICOS INTERACTIVOS (Ventanas emergentes)
    print("[INFO] Abriendo ventanas gráficas de alta definición... Cierra la ventana del gráfico para continuar.")
    
    # 1. Distribución de Popularidad (HD)
    plt.figure(figsize=(9, 5))
    sns.histplot(y_regression, bins=30, kde=True, color='skyblue')
    plt.title('Distribución de la Popularidad Comercial')
    plt.xlabel('Popularidad (0-100)')
    plt.ylabel('Frecuencia')
    plt.show()  # Abre la interfaz visual y pausa el script hasta que la cierres

    # 2. Distribución de Géneros (HD)
    plt.figure(figsize=(10, 5))
    y_classification.value_counts().plot(kind='bar', color='salmon')
    plt.title('Distribución de Géneros Musicales')
    plt.xlabel('Género')
    plt.ylabel('Cantidad de canciones')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Abre la interfaz visual y pausa el script hasta que la cierres

# ==========================================
# FASE 5 & 6: ANÁLISIS DE CORRELACIÓN
# ==========================================

def analizar_correlacion(X_escalado, y_regression):
    print("=== FASE 6: ANÁLISIS DE CORRELACIÓN ===")
    datos_corr = X_escalado.copy()
    datos_corr['popularity'] = y_regression.values
    
    correlaciones = datos_corr.corr()['popularity'].abs().sort_values(ascending=False)
    print("Top de variables correlacionadas con la Popularidad (Valor Absoluto):")
    print(correlaciones)
    print()
    
    print("[INFO] Mostrando mapa de calor de correlaciones en HD. Cierra la ventana para continuar...")
    plt.figure(figsize=(11, 9))
    sns.heatmap(X_escalado.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Matriz de Correlación de Variables Acústicas')
    plt.tight_layout()
    plt.show()  # Abre la interfaz visual y pausa el script hasta que la cierres

# ==========================================
# FASE 7 & 8: EXPERIMENTACIÓN DE REGRESIÓN
# ==========================================

def entrenar_evaluar_regresores(X_train, X_test, y_train, y_test):
    print("=== FASES 7 & 8: EXPERIMENTACIÓN Y EVALUACIÓN DE REGRESORES ===")
    
    # 1. Regresión Lineal Simple
    print("[Regresor 1] Ajustando Regresión Lineal Simple (instrumentalness)...")
    X_train_simple = X_train[['instrumentalness']]
    X_test_simple = X_test[['instrumentalness']]
    
    reg_simple = LinearRegression()
    reg_simple.fit(X_train_simple, y_train)
    y_pred_simple = reg_simple.predict(X_test_simple)
    
    # 2. Regresión Lineal Múltiple
    print("[Regresor 2] Ajustando Regresión Lineal Múltiple...")
    reg_multiple = LinearRegression()
    reg_multiple.fit(X_train, y_train)
    y_pred_multiple = reg_multiple.predict(X_test)
    
    # 3. Random Forest Regressor
    print("[Regresor 3] Entrenando Random Forest Regressor (n_estimators=10)...")
    reg_rf = RandomForestRegressor(n_estimators=10, random_state=74, n_jobs=-1)
    reg_rf.fit(X_train, y_train)
    y_pred_rf = reg_rf.predict(X_test)
    
    modelos = {
        "Regresión Lineal Simple": y_pred_simple,
        "Regresión Lineal Múltiple": y_pred_multiple,
        "Random Forest Regressor": y_pred_rf
    }
    
    for nombre, predicciones in modelos.items():
        mae = mean_absolute_error(y_test, predicciones)
        mse = mean_squared_error(y_test, predicciones)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, predicciones)
        print(f"\nMétricas para: {nombre}")
        print(f" -> MAE: {mae:.2f} | MSE: {mse:.2f} | RMSE: {rmse:.2f} | R² Score: {r2:.4f}")
    print()

# ==========================================
# FASE 9 & 10: EXPERIMENTACIÓN DE CLASIFICACIÓN
# ==========================================

def entrenar_evaluar_clasificadores(X_train_cls, X_test_cls, y_train_cls, y_test_cls):
    print("=== FASES 9 & 10: EXPERIMENTACIÓN Y EVALUACIÓN DE CLASIFICADORES ===")
    
    # 1. SVM Lineal
    print("[Clasificador 1] Ajustando SVM Lineal (C=1.0)...")
    modelo_svm = SVC(kernel='linear', C=1.0, random_state=74)
    modelo_svm.fit(X_train_cls, y_train_cls)
    y_pred_svm = modelo_svm.predict(X_test_cls)
    
    # 2. Random Forest Classifier
    print("[Clasificador 2] Entrenando Random Forest Classifier...")
    modelo_rf = RandomForestClassifier(n_estimators=100, random_state=74, class_weight='balanced', n_jobs=-1)
    modelo_rf.fit(X_train_cls, y_train_cls)
    y_pred_rf = modelo_rf.predict(X_test_cls)
    
    print(f"\nAccuracy SVM: {accuracy_score(y_test_cls, y_pred_svm):.4%}")
    print(f"Accuracy Random Forest: {accuracy_score(y_test_cls, y_pred_rf):.4%}\n")
    
    print("Reporte detallado de clasificación (Random Forest):")
    print(classification_report(y_test_cls, y_pred_rf))
    
    # Matriz de Confusión Emergente (RF)
    print("[INFO] Mostrando la matriz de confusión del clasificador final en HD...")
    cm_rf = confusion_matrix(y_test_cls, y_pred_rf)
    disp_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=sorted(y_test_cls.unique()))
    disp_rf.plot(cmap='Blues')
    plt.title('Matriz de Confusión: Random Forest Classifier')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Abre la interfaz visual y pausa el script hasta que la cierres

# ==========================================
# AUDITORÍA DE CALIDAD DE DATOS
# ==========================================

def auditar_calidad_datos(df):
    print("=== AUDITORÍA DE CALIDAD DE DATOS ===")
    nulos = df.isnull().sum()
    total_nulos = nulos.sum()
    print(f"Valores nulos totales detectados: {total_nulos}")
    if total_nulos > 0:
        print(nulos[nulos > 0])
        
    duplicados = df.duplicated().sum()
    print(f"Registros completamente duplicados: {duplicados}\n")

# ==========================================
# CLASE DE PRODUCCIÓN INTEGRADORA (SpotifyPredictor)
# ==========================================

class SpotifyPredictor:
    def __init__(self, dataframe):
        self.features = [
            'duration_ms', 'explicit', 'danceability', 'energy', 'key',
            'loudness', 'mode', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature'
        ]
        df = dataframe.copy().dropna(subset=self.features + ['track_genre', 'popularity'])
        df['explicit'] = df['explicit'].astype(int)

        X = df[self.features]
        y_genero = df['track_genre']
        y_popularidad = df['popularity']

        self.scaler = MinMaxScaler()
        X_scaled = self.scaler.fit_transform(X)

        self.model_genre = RandomForestClassifier(
            n_estimators=100, random_state=74, class_weight='balanced', n_jobs=-1
        )
        self.model_popularity = RandomForestRegressor(
            n_estimators=100, random_state=74, n_jobs=-1
        )

        print("[PREDICTOR] Ajustando clasificadores de producción finales...")
        self.model_genre.fit(X_scaled, y_genero)
        self.model_popularity.fit(X_scaled, y_popularidad)
        print("[PREDICTOR] Modelos finales listos para inferencias de producción.\n")

    def predecir_exito(self, datos_cancion):
        df_input = pd.DataFrame([datos_cancion])
        if 'explicit' in df_input.columns:
            df_input['explicit'] = df_input['explicit'].astype(int)
        X_scaled = self.scaler.transform(df_input[self.features])
        return {
            "genero_predicho": self.model_genre.predict(X_scaled)[0],
            "popularidad_estimada": round(float(self.model_popularity.predict(X_scaled)[0]), 2)
        }

# ==========================================
# FLUJO PRINCIPAL E INTEGRACIÓN
# ==========================================

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    data_path = os.path.join(base_dir, 'spotify_tracks.csv')
    
    if not os.path.exists(data_path):
        data_path = 'spotify_tracks.csv'
        
    try:
        df, X, y_regression, y_classification, columnas_numericas, columnas_booleanas = cargar_y_analizar_datos(data_path)
        
        auditar_calidad_datos(df)
        X_escalado, scaler = preprocesar_datos(df, columnas_booleanas)
        
        # El EDA abrirá las ventanas gráficas interactivas del sistema una por una
        realizar_eda(df, y_regression, y_classification)
        analizar_correlacion(X_escalado, y_regression)
        
        print("=== FASE 5: DIVISIÓN DE MUESTRAS (ESTRATIFICACIÓN DE POPULARIDAD) ===")
        X_train, X_test, y_train, y_test = train_test_split(
            X_escalado, y_regression, test_size=0.20, random_state=74,
            stratify=pd.cut(y_regression, bins=20, labels=False)
        )
        print(f"Datos de Entrenamiento: {X_train.shape[0]} muestras | Datos de Test: {X_test.shape[0]} muestras\n")
        
        entrenar_evaluar_regresores(X_train, X_test, y_train, y_test)
        
        X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
            X_escalado, y_classification, test_size=0.20, random_state=74, stratify=y_classification
        )
        
        entrenar_evaluar_clasificadores(X_train_cls, X_test_cls, y_train_cls, y_test_cls)
        
        # Integración de Validación Final
        print("=== VALIDACIÓN DE LA CLASE PRODUCTIVA FINAL ===")
        predictor = SpotifyPredictor(df)
        cancion_prueba = {
            'duration_ms': 215000, 'explicit': 0, 'danceability': 0.82, 'energy': 0.75, 'key': 5,
            'loudness': -5.2, 'mode': 1, 'speechiness': 0.06, 'acousticness': 0.12,
            'instrumentalness': 0.0, 'liveness': 0.08, 'valence': 0.88, 'tempo': 118.0, 'time_signature': 4
        }
        resultado = predictor.predecir_exito(cancion_prueba)
        print("REPORTING INDEPENDIENTE:")
        print(f" -> Género Sugerido: {resultado['genero_predicho']}")
        print(f" -> Popularidad comercial estimada: {resultado['popularidad_estimada']} / 100")
        print("==============================================")
        
    except FileNotFoundError:
        print(f"[ERROR] No se pudo localizar '{data_path}' en {base_dir}. Por favor, coloca allí el CSV.")