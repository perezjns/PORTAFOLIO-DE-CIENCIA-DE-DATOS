# 🌾 Sembrar con Éxito: Machine Learning para Selección de Cultivos

Este proyecto aplica técnicas de **Machine Learning** y **Ciencia de Datos** en Python para resolver un problema estratégico en la agricultura: la selección optima de cultivos en función de las propiedades químico-físicas del suelo.

El objetivo central es identificar la característica individual del suelo que posee el mayor poder predictivo para clasificar correctamente el tipo de cultivo, optimizando así los costes de análisis agronómicos para los agricultores.

---

## 📋 Tabla de Contenidos
- [Contexto del Problema](#-contexto-del-problema)
- [Estructura del Dataset](#-estructura-del-dataset)
- [Metodología de Machine Learning](#-metodología-de-machine-learning)
- [Resultados y Conclusiones](#-resultados-y-conclusiones)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Cómo Ejecutar el Código](#-cómo-ejecutar-el-código)

---

## 🎯 Contexto del Problema

Medir los nutrientes del suelo (Nitrógeno, Fósforo, Potasio y pH) es imprescindible para maximizar el rendimiento agrícola. Sin embargo, realizar pruebas de laboratorio completas puede ser costoso y lento. 

A través de este análisis, evaluamos de forma univariable cada nutriente mediante modelos de clasificación multiclase, determinando cuál de ellos aporta mayor precisión predictiva ($F1\text{-}Score$) para la toma de decisiones agrícolas.

---

## 📊 Estructura del Dataset (`soil_measures.csv`)

El conjunto de datos contiene mediciones de campo organizadas en las siguientes variables:

| Variable | Descripción | Tipo de Dato |
| :--- | :--- | :--- |
| **`N`** | Proporción de contenido de Nitrógeno en el suelo | Numérico (float) |
| **`P`** | Proporción de contenido de Fósforo en el suelo | Numérico (float) |
| **`K`** | Proporción de contenido de Potasio en el suelo | Numérico (float) |
| **`ph`** | Valor del pH del suelo | Numérico (float) |
| **`crop`** | Tipo de cultivo recomendado (Variable Objetivo) | Categórico (string) |

---

## ⚙️ Metodología de Machine Learning

El flujo de trabajo sigue las siguientes etapas:

1. **Preprocesamiento y Limpieza:** Eliminación de espacios invisibles en los nombres de las columnas y separación de características ($X$) y etiqueta objetivo ($y$).
2. **División de Datos:** Partición en conjunto de entrenamiento ($70\%$) y prueba ($30\%$) fijando `random_state=42` para garantizar reproducibilidad.
3. **Modelado Univariable:** Entrenamiento independiente de un modelo de **Regresión Logística Multinomial** (`multi_class="multinomial"`, `max_iter=1000`) para cada una de las variables ($N$, $P$, $K$, $pH$).
4. **Evaluación:** Medición del desempeño predictivo utilizando la métrica **$F1\text{-}Score$ Ponderado** (`average="weighted"`).
5. **Visualización:** Generación de gráficos comparativos con `Seaborn` y `Matplotlib` destacando la variable óptima y los requerimientos promedio por cultivo.

---

## 📈 Resultados y Conclusiones

* **Variable con mayor poder predictivo:** **Potasio ($K$)**, alcanzando el $F1\text{-}Score$ más alto entre las métricas evaluadas univariablemente.
* **Aplicación práctica:** Un agricultor con presupuesto limitado puede priorizar el análisis de niveles de Potasio ($K$) en el suelo como el indicador individual más fiable para determinar el cultivo adecuado.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Manipulación de Datos:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (`LogisticRegression`, `f1_score`, `train_test_split`)
* **Visualización de Datos:** `matplotlib`, `seaborn`

---

## 🚀 Cómo Ejecutar el Código

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/perezjns/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git](https://github.com/perezjns/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git)
