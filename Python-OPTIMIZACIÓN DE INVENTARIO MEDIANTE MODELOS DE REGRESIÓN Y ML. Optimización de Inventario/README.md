# 🎬 Predicción de la duración del alquiler de DVD

## 📌 Descripción del proyecto

Este proyecto utiliza técnicas de **Machine Learning supervisado** y modelos de regresión para predecir cuántos días mantendrá un cliente un DVD alquilado.

El objetivo es ayudar a una empresa de alquiler de películas a optimizar la gestión de su inventario y planificar la rotación del stock de forma más eficiente mediante el análisis de datos históricos.

El proyecto se desarrolla en Python utilizando las librerías **pandas** y **scikit-learn**.

## 🎯 Objetivos

- Preprocesar y transformar los datos para utilizarlos en modelos predictivos.
- Calcular la duración del alquiler a partir de las fechas de alquiler y devolución.
- Crear variables dummy a partir de los contenidos especiales de las películas.
- Evitar la fuga de información (*data leakage*).
- Entrenar y comparar diferentes algoritmos de regresión.
- Seleccionar el modelo con menor error cuadrático medio (MSE).
- Alcanzar un MSE inferior a 3 en el conjunto de prueba.

## 📂 Dataset

El proyecto utiliza el archivo `rental_info.csv`, que contiene información sobre los alquileres de DVD.

La base de datos contiene **15.861 registros y 15 columnas originales**.

### Variables principales

| Variable | Descripción |
|---|---|
| `rental_date` | Fecha y hora del alquiler. |
| `return_date` | Fecha y hora de devolución. |
| `amount` | Importe pagado por el alquiler. |
| `amount_2` | Cuadrado del importe. |
| `rental_rate` | Tarifa del alquiler. |
| `rental_rate_2` | Cuadrado de la tarifa. |
| `release_year` | Año de estreno de la película. |
| `length` | Duración de la película en minutos. |
| `length_2` | Cuadrado de la duración. |
| `replacement_cost` | Coste de reemplazo del DVD. |
| `special_features` | Contenidos especiales incluidos en el DVD. |
| `NC-17`, `PG`, `PG-13`, `R` | Variables dummy de clasificación por edades. |

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Pandas:** manipulación y análisis de datos.
- **Scikit-learn:** entrenamiento y evaluación de modelos de Machine Learning.
- **Jupyter Notebook / Google Colab:** entornos de desarrollo.

## ⚙️ Metodología

### 1. Preprocesamiento de los datos

Se cargó el archivo CSV utilizando pandas y se convirtieron las columnas `rental_date` y `return_date` al formato de fecha y hora.

### 2. Ingeniería de características (*Feature Engineering*)

Se creó la variable objetivo `rental_length_days`, calculando la diferencia en días entre la fecha de devolución y la fecha de alquiler.

También se generaron dos variables dummy:

- `deleted_scenes`: toma el valor 1 cuando el DVD incluye *Deleted Scenes* y 0 en caso contrario.
- `behind_the_scenes`: toma el valor 1 cuando el DVD incluye *Behind the Scenes* y 0 en caso contrario.

### 3. Selección de variables

Se definieron las variables predictoras en el DataFrame `X` y la variable objetivo en la Serie `y`.

Se excluyeron `return_date` y `rental_length_days` de las variables predictoras para evitar la fuga de información, ya que permitirían conocer directamente la duración real del alquiler.

También se excluyeron las columnas originales `rental_date` y `special_features` de la selección final de predictores.

### 4. División de los datos

Los datos se dividieron en:

- **80 % para entrenamiento.**
- **20 % para prueba.**

Se utilizó `random_state=9` para garantizar la reproducibilidad de la división.

### 5. Entrenamiento y comparación de modelos

Se evaluaron los siguientes algoritmos:

- Linear Regression
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- Hist Gradient Boosting Regressor

### 6. Evaluación del rendimiento

Se utilizó el **Mean Squared Error (MSE)** o error cuadrático medio.

Esta métrica calcula el promedio de los errores de predicción elevados al cuadrado. Cuanto menor sea su valor, mejores serán las predicciones en el conjunto evaluado.

El objetivo del proyecto es obtener un **MSE inferior a 3**.

## 📊 Resultados

Los resultados de referencia obtenidos durante el desarrollo fueron los siguientes:

| Modelo | MSE de referencia |
|---|---:|
| Hist Gradient Boosting Regressor | **1,9006** |
| Extra Trees Regressor | 2,0382 |
| Random Forest Regressor | 2,0467 |
| Gradient Boosting Regressor | 2,3637 |
| Linear Regression | 2,9417 |

Según esta comparación, **Hist Gradient Boosting Regressor** obtuvo el menor MSE de referencia, cumpliendo el objetivo establecido.

> **Nota:** estos resultados deben confirmarse ejecutando el código completo en el entorno definitivo. El rendimiento puede variar según la configuración y la versión de las librerías utilizadas.

## 💡 Conclusiones

Este proyecto demuestra cómo las técnicas de aprendizaje supervisado pueden aplicarse a un problema empresarial relacionado con la gestión del inventario.

A través del preprocesamiento, la ingeniería de características y la comparación de modelos, se construyó un flujo de trabajo para predecir la duración de los alquileres y evaluar el rendimiento de distintos algoritmos.

La solución podría contribuir a mejorar la planificación de la disponibilidad de películas y la rotación del stock. Su utilidad real deberá validarse con nuevos datos y con las necesidades operativas de la empresa.

## 🚀 Competencias desarrolladas

- Análisis y limpieza de datos con pandas.
- Ingeniería de características.
- Preparación de datos para Machine Learning.
- Aprendizaje supervisado.
- Modelos de regresión.
- Entrenamiento y evaluación con scikit-learn.
- Comparación de modelos mediante MSE.
- Prevención de fuga de información (*data leakage*).
- Aplicación del análisis predictivo a problemas empresariales.


`Python` · `Pandas` · `Scikit-learn` · `Machine Learning` · `Data Science` · `Data Analytics` · `Regression` · `Feature Engineering`
