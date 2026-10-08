# 📊 Portafolio de Ciencia de Datos & Ingeniería de Datos

## 🔍 Sobre este Portafolio

¡Bienvenido a mi espacio de Ciencia de Datos e Ingeniería de Datos! En este repositorio comparto proyectos prácticos enfocados en extraer valor real de los datos, diseñar pipelines automatizados de extremo a extremo (*End-to-End*), construir modelos predictivos, desarrollar dashboards de Business Intelligence y resolver problemas de negocio complejos mediante análisis estadístico y aprendizaje automático (*Machine Learning*).

---

## 📁 Estructura del Repositorio

A continuación se detallan los módulos y carpetas principales que componen este portafolio:

| Carpeta / Proyecto | Descripción | Tecnologías Clave |
| :--- | :--- | :--- |
| **📁 Power Bi-ANÁLISIS DE CANCELACIÓN DE CLI...** | Dashboard interactivo enfocado en el análisis de abandono/churn de clientes, métricas de retención y comportamiento de usuarios. | Power BI, DAX, Power Query |
| **📁 Power Bi-CUADRO DE MANDOS CASO Adven...** | Cuadro de mandos corporativo analizando transacciones, rendimiento de productos por género/canal, volumen por categoría y rentabilidad financiera (Año 2021). | Power BI, DAX, Power Query, Star Schema |
| **📁 Power Bi-GESTION DE ARCHIVOS MULTIFOR...** | Modelado dimensional y visualización analítica a partir del cruce relacional de fuentes heterogéneas. | Power BI, DAX, Data Modeling |
| **📁 Power Bi-HR ANALYTICS** | Cuadro de mandos enfocado en la analítica de recursos humanos, gestión de talento, métricas de personal y rotación de empleados. | Power BI, DAX, HR Metrics |
| **📁 Python-ANÁLISIS EXPLORATORIO DE DATOS** | Diagnóstico estadístico, limpieza transaccional y visualización avanzada de series de ventas globales. | Python, Seaborn, Pandas, Estadística |
| **📁 Python-GESTIÓN DE ARCHIVOS MULTIFORMATO** | Ingesta, normalización y cruce relacional dinámico de fuentes heterogéneas (CSV, SQLite, JSON anidados). | Python, Pandas, SQLite, JSON |
| **📁 Python-LIMPIEZA Y NORMALIZACIÓN DE DATOS** | Automatización del tratamiento y curación de datos mediante pipelines ETL robustos para catálogos inmobiliarios. | Python, Pandas, ETL, Sanitización |
| **📁 Python-MODELADO Y PREDICCIÓN** | Construcción de modelos predictivos de clasificación/regresión y optimización de hiperparámetros. | Scikit-Learn, Pandas, Métricas ML |
| **📁 Python-SEMBRAR CON ÉXITO-MACHINE LEARNING PARA ELEGIR CULTIVO** | Selección óptima de cultivos agrícolas analizando nutrientes del suelo ($N, P, K, pH$) mediante evaluación univariable con Regresión Logística y métricas $F1\text{-}Score$. | Python, Scikit-Learn, Pandas, Seaborn |

---

## 🚀 Proyectos Destacados

### 🌾 1. Selección Óptima de Cultivos (Python-SEMBRAR CON ÉXITO-MACHINE LEARNING PARA ELEGIR CULTIVO)
Solución agrotecnológica orientada a minimizar costes de laboratorio agronómico optimizando la elección de cultivos mediante aprendizaje automático.
* **Evaluación Univariable:** Entrenamiento de modelos de Regresión Logística Multinomial independientes para cada nutriente ($N$, $P$, $K$, $pH$).
* **Optimización de Métricas:** Determinación de la variable crítica utilizando $F1\text{-}Score$ Ponderado, identificando al **Potasio ($K$)** como la característica individual con mayor poder predictivo.
* **Visualización Específica:** Generación de diagnósticos de rendimiento por nutriente y análisis del promedio de requerimientos requeridos por tipo de cultivo.

### 📉 2. Análisis Exploratorio de Datos (Python-ANÁLISIS EXPLORATORIO DE DATOS)
Aborda un estudio analítico profundo enfocado en la depuración transaccional y la evaluación de tendencias estacionales del negocio.
* **Depuración y Calidad del Dato:** Filtrado sistemático de registros corruptos (`###ERROR###`, `-99999`) y aislamiento de duplicados basados en lógica de estados.
* **Análisis de Series Temporales:** Modelado cronológico de ingresos mensuales consolidados, identificando valles de mercado y picos de facturación históricos.
* **Evaluación de Dispersión:** Análisis estadístico de correlaciones empleando escalas logarítmicas para corregir la alta variabilidad en precios unitarios y volúmenes de pedido.

### ⚙️ 3. Gestión de Archivos Multiformato (Python-GESTIÓN DE ARCHIVOS MULTIFORMATO)
Implementación de un cargador relacional dinámico capaz de unificar y normalizar orígenes de datos con estructuras conflictivas.
* **Ingesta Heterogénea:** Procesamiento simultáneo de archivos logísticos en CSV (UTF-16, separador `|`), bases de datos relacionales SQLite y archivos JSON con anidamiento multinivel.
* **Robustez Relacional:** Aplanamiento de datos demográficos y geográficos mediante `pd.json_normalize` junto con homologación estricta de tipos de datos en llaves foráneas para evitar la pérdida de registros.

### 🏢 4. Limpieza y Normalización de Datos (Python-LIMPIEZA Y NORMALIZACIÓN DE DATOS)
Ingeniería y preparación de datos (*Data Preparation*) avanzada, transformando conjuntos de datos brutos e inconsistentes en activos de información confiables listos para producción.
* **Automatización:** Diseño de un pipeline modular (`pipeline_inmuebles.py`) bajo una arquitectura limpia y reutilizable.
* **Sanitización Inteligente:** Imputación avanzada de valores nulos mediante lógicas de agregación por zonas geográficas y eliminación controlada de valores atípicos (*outliers*).

### 🤖 5. Modelado y Predicción con Python
