# 🎬 Predicción de Duración de Alquiler de DVDs
*Optimización de Inventario mediante Modelos de Regresión y Machine Learning*

---

## 📋 1. Objetivo del Proyecto
La empresa de alquiler de DVDs necesitaba anticipar con precisión cuántos días un cliente mantendrá un título alquilado (`rental_length_days`). El objetivo principal de negocio fue construir un modelo predictivo capaz de superar un **Error Cuadrático Medio (MSE) menor o igual a 3.0** en el conjunto de prueba, permitiendo así una planificación de inventario y rotación de stock mucho más eficiente.

---

## 📊 2. Descripción del Conjunto de Datos (`rental_info.csv`)
El análisis se basó en el procesamiento de características cuantitativas y categóricas clave de las películas y transacciones:
* **Variables Temporales**: `rental_date` y `return_date` (utilizadas para calcular la duración real del alquiler).
* **Variables Financieras**: Importe pagado (`amount`), su transformación cuadrática (`amount_2`), la tarifa de alquiler (`rental_rate`, `rental_rate_2`) y el coste de reemplazo (`replacement_cost`).
* **Características Fílmicas**: Duración de la película en minutos (`length`, `length_2`) y año de estreno (`release_year`).
* **Variables Categóricas y Dummy**: Clasificación por edades (`NC-17`, `PG`, `PG-13`, `R`) y características especiales de los DVDs (`special_features`).

---

## ⚙️ 3. Procedimiento y Metodología

El desarrollo del proyecto se estructuró en cuatro fases clave:

1. **Ingeniería de la Variable Objetivo**: 
   Se convirtieron las fechas de alquiler y devolución a formato `datetime` para calcular la duración exacta de cada transacción en días:
   $$\text{rental\_length\_days} = \frac{\text{return\_date} - \text{rental\_date}}{\text{24 horas}}$$

2. **Ingeniería de Características en Texto**: 
   A partir de la columna categórica `special_features`, se aplicó procesamiento de texto para extraer subcadenas específicas, generando dos variables indicadoras binarias (dummies):
   * `deleted_scenes`: Toma el valor `1` si el DVD incluye escenas eliminadas (y `0` en caso contrario).
   * `behind_the_scenes`: Toma el valor `1` si el DVD incluye contenido detrás de cámaras (y `0` en caso contrario).

3. **Prevención de Fuga de Data (*Data Leakage*)**: 
   Se eliminaron de la matriz de características (`X`) todas aquellas columnas que filtraban información directa sobre el objetivo (como las fechas originales y la variable objetivo), garantizando un aprendizaje robusto y realista.

4. **Partición y Validación**: 
   Los datos se dividieron en conjuntos de entrenamiento (80%) y prueba (20%), fijando una semilla de aleatoriedad (`random_state=9`) para asegurar la total reproducibilidad del experimento.

---

## 📈 4. Análisis de Resultados

Se evaluaron e intercompararon cuatro algoritmos de regresión para determinar cuál minimizaba de manera óptima el error de predicción:

| Modelo Evaluado | MSE (Test Set) | $R^2$ Score | ¿Cumple el Objetivo de Negocio? (MSE ≤ 3.0) |
| :--- | :---: | :---: | :---: |
| **Linear Regression** | 2.7247 | 0.6002 | ✅ Sí |
| **Ridge Regression** | 2.7247 | 0.6002 | ✅ Sí |
| **Gradient Boosting** | 2.2215 | 0.6740 | ✅ Sí |
| **Random Forest Regressor** | **1.8147** | **0.7337** | **🏆 Sí (Modelo Óptimo Seleccionado)** |

### 💡 Conclusiones Clave y Valor de Negocio:
* **Superación de la Meta**: Todos los modelos evaluados cumplieron satisfactoriamente con el umbral requerido por la empresa (MSE < 3.0). Sin embargo, **Random Forest** demostró ser ampliamente superior, reduciendo el MSE a **1.8147** y explicando el **73.37% de la variabilidad** de los datos ($R^2 = 0.7337$).
* **Importancia de Variables**: El análisis de importancia del modelo reveló que los factores económicos asociados al alquiler (`amount`, `amount_2`, `rental_rate` y `rental_rate_2`) poseen el peso más determinante a la hora de predecir el comportamiento de retención del cliente, por encima de la duración o categoría de la película.
* **Impacto Operativo**: Gracias a este modelo predictivo, la compañía cuenta con una herramienta cuantitativa sólida para anticipar la devolución de los ejemplares, evitar roturas de stock y optimizar la logística de inventario.
