# 🎬 Predicción de Duración de Alquiler de DVDs (Machine Learning)

Proyecto de ciencia de datos desarrollado para optimizar la planificación de inventario de una empresa de alquiler de películas mediante modelos de regresión predictiva.

---

## 📋 Descripción del Proyecto
La compañía necesitaba predecir con precisión cuántos días un cliente mantendrá alquilado un DVD (`rental_length_days`) en función de las características financieras, físicas y categóricas de las películas. 

Para lograrlo, se procesó el conjunto de datos `rental_info.csv`, realizando ingeniería de características, codificación de variables categóricas y evaluación comparativa de múltiples algoritmos de Machine Learning hasta superar el objetivo de negocio establecido (**MSE ≤ 3.0**).

---

## 📂 Estructura del Dataset (`rental_info.csv`)
El conjunto de datos incluye las siguientes variables clave:
* **`rental_date` / `return_date`**: Fechas de inicio y devolución del alquiler (utilizadas para calcular la variable objetivo).
* **`amount` & `amount_2`**: Importe pagado por el cliente y su valor al cuadrado.
* **`rental_rate` & `rental_rate_2`**: Tarifa de alquiler y su valor al cuadrado.
* **`length` & `length_2`**: Duración de la película en minutos y su valor al cuadrado.
* **`release_year`**: Año de estreno de la película.
* **`replacement_cost`**: Coste de reemplazo para la empresa.
* **`special_features`**: Contenido adicional (tráilers, escenas eliminadas, detrás de cámaras), transformado en variables binarias (`deleted_scenes`, `behind_the_scenes`).
* **`NC-17`, `PG`, `PG-13`, `R`**: Variables ficticias (*dummies*) de clasificación por edades.

---

## 🛠️ Preprocesamiento de Datos
1. **Creación de la Variable Objetivo**: Conversión de `rental_date` y `return_date` a formato datetime para calcular la duración exacta en días:
   $$\text{rental\_length\_days} = \frac{\text{return\_date} - \text{rental\_date}}{\text{24 horas}}$$
2. **Ingeniería de Características en Texto**: Extracción de subcadenas desde `special_features` para generar indicadores binarios:
   * `deleted_scenes` (1 si incluye escenas eliminadas, 0 en caso contrario).
   * `behind_the_scenes` (1 si incluye detrás de cámaras, 0 en caso contrario).
3. **División de Datos**: Separación en conjuntos de entrenamiento y prueba (80% train, 20% test) fijando `random_state=9` para garantizar la reproducibilidad.

---

## 📊 Comparativa de Modelos y Resultados

Se evaluaron cuatro algoritmos de regresión para encontrar el que ofreciera el menor Error Cuadrático Medio (`MSE`):

| Modelo | MSE (Test Set) | $R^2$ Score | Cumple Objetivo (MSE ≤ 3.0) |
| :--- | :---: | :---: | :---: |
| **Linear Regression** | 2.7247 | 0.6002 | ✅ Sí |
| **Ridge Regression** | 2.7247 | 0.6002 | ✅ Sí |
| **Gradient Boosting** | 2.2215 | 0.6740 | ✅ Sí |
| **Random Forest Regressor** | **1.8147** | **0.7337** | **✅ Sí (Mejor Modelo)** |

---

## 🚀 Código de Implementación

Puedes ejecutar el flujo completo de preprocesamiento, modelado y evaluación con el siguiente script en Python:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Carga de datos
df = pd.read_csv('rental_info.csv')

# 2. Ingeniería de características (Variable objetivo y dummies)
df['rental_date'] = pd.to_datetime(df['rental_date'])
df['return_date'] = pd.to_datetime(df['return_date'])
df['rental_length_days'] = (df['return_date'] - df['rental_date']).dt.total_seconds() / (24 * 3600)

df['deleted_scenes'] = df['special_features'].str.contains('Deleted Scenes').astype(int)
df['behind_the_scenes'] = df['special_features'].str.contains('Behind the Scenes').astype(int)

# 3. Definición de Features (X) y Target (y)
X = df.drop(columns=['rental_date', 'return_date', 'special_features', 'rental_length_days'])
y = df['rental_length_days']

# 4. Train-Test Split (20% test, random_state=9)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9)

# 5. Entrenamiento del Mejor Modelo
best_model = RandomForestRegressor(random_state=9)
best_model.fit(X_train, y_train)

# 6. Evaluación de Resultados
y_pred = best_model.predict(X_test)
best_mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mejor Modelo: Random Forest")
print(f"MSE en Test Set: {best_mse:.4f}")
print(f"R² Score: {r2:.4f}")
