# 📊 Portafolio de Ciencia de Datos & Ingeniería de Datos

## 🔍 Sobre este Portafolio

¡Bienvenido a mi espacio de Ciencia de Datos e Ingeniería de Datos! En este repositorio comparto proyectos prácticos enfocados en extraer valor real de los datos, diseñar pipelines automatizados de extremo a extremo (End-to-End), construir modelos predictivos, desarrollar dashboards de Business Intelligence y resolver problemas de negocio complejos mediante análisis estadístico y aprendizaje automático (Machine Learning).

---

## 📁 Estructura del Repositorio

A continuación se detallan los módulos y carpetas principales que componen este portafolio:

| Carpeta / Proyecto | Descripción | Tecnologías Clave |
| :--- | :--- | :--- |
| 📁 `Power Bi-ANÁLISIS DE CANCELACIÓN DE CLI...` | Dashboard interactivo enfocado en el análisis de abandono/churn de clientes, métricas de retención y comportamiento de usuarios. | Power BI, DAX, Power Query |
| 📁 `Power Bi-CUADRO DE MANDOS CASO Adven...` | Cuadro de mandos corporativo analizando transacciones, rendimiento de productos por género/canal, volumen por categoría y rentabilidad financiera (Año 2021). | Power BI, DAX, Power Query, Star Schema |
| 📁 `Power Bi-GESTION DE ARCHIVOS MULTIFOR...` | Modelado dimensional y visualización analítica a partir del cruce relacional de fuentes heterogéneas. | Power BI, DAX, Data Modeling |
| 📁 `Python-ANÁLISIS EXPLORATORIO DE DATOS` | Diagnóstico estadístico, limpieza transaccional y visualización avanzada de series de ventas globales. | Python, Seaborn, Pandas, Estadística |
| 📁 `Python-GESTIÓN DE ARCHIVOS MULTIFORMATO` | Ingesta, normalización y cruce relacional dinámico de fuentes heterogéneas (CSV, SQLite, JSON anidados). | Python, Pandas, SQLite, JSON |
| 📁 `Python-LIMPIEZA Y NORMALIZACIÓN DE DATOS` | Automatización del tratamiento y curación de datos mediante pipelines ETL robustos para catálogos inmobiliarios. | Python, Pandas, ETL, Sanitización |
| 📁 `Python-MODELADO Y PREDICCIÓN` | Construcción de modelos predictivos de clasificación/regresión y optimización de hiperparámetros. | Scikit-Learn, Pandas, Métricas ML |

---

## 🚀 Proyectos Destacados

### 📉 1. Análisis Exploratorio de Datos (`Python-ANÁLISIS EXPLORATORIO DE DATOS`)
Aborda un estudio analítico profundo enfocado en la depuración transaccional y la evaluación de tendencias estacionales del negocio.
* **Depuración y Calidad del Dato:** Filtrado sistemático de registros corruptos (`###ERROR###`, `-99999`) y aislamiento de duplicados basados en lógica de estados.
* **Análisis de Series Temporales:** Modelado cronológico de ingresos mensuales consolidados, identificando valles de mercado y picos de facturación históricos.
* **Evaluación de Dispersión:** Análisis estadístico de correlaciones empleando escalas logarítmicas para corregir la alta variabilidad en precios unitarios y volúmenes de pedido.

### ⚙️ 2. Gestión de Archivos Multiformato (`Python-GESTIÓN DE ARCHIVOS MULTIFORMATO`)
Implementación de un cargador relacional dinámico capaz de unificar y normalizar orígenes de datos con estructuras conflictivas.
* **Ingesta Heterogénea:** Procesamiento simultáneo de archivos logísticos en CSV (UTF-16, separador `|`), bases de datos relacionales SQLite y archivos JSON con anidamiento multinivel.
* **Robustez Relacional:** Aplanamiento de datos demográficos y geográficos mediante `pd.json_normalize` junto con homologación estricta de tipos de datos en llaves foráneas para evitar la pérdida de registros.

### 🏢 3. Limpieza y Normalización de Datos (`Python-LIMPIEZA Y NORMALIZACIÓN DE DATOS`)
Ingeniería y preparación de datos (*Data Preparation*) avanzada, transformando conjuntos de datos brutos e inconsistentes en activos de información confiables listos para producción.
* **Automatización:** Diseño de un pipeline modular (`pipeline_inmuebles.py`) bajo una arquitectura limpia y reutilizable.
* **Sanitización Inteligente:** Imputación avanzada de valores nulos mediante lógicas de agregación por zonas geográficas y eliminación controlada de valores atípicos (*outliers*).

### 🤖 4. Modelado y Predicción con Python (`Python-MODELADO Y PREDICCIÓN`)
Desarrollo de modelos predictivos con metodologías rigurosas para garantizar tanto la precisión matemática como la interpretabilidad de los resultados.
* **Ingeniería de Características (*Feature Engineering*):** Normalización, escalado estadístico y codificación avanzada de variables categóricas.
* **Modelado y Evaluación:** Implementación de algoritmos supervisados evaluados mediante métricas robustas de rendimiento ($R^2$, RMSE, precisión y curvas ROC-AUC).

### 📊 5. Business Intelligence & Dashboards (`Power Bi-*`)
Diseño e implementación de modelos de datos analíticos y cuadros de mando interactivos en Power BI.
* **Análisis de Cancelación de Clientes (*Churn Analysis*):** Visualización de indicadores clave (KPIs) para la retención y pérdida de clientes.
* **Cuadro de Mandos Adventure Works Cycles:** Solución corporativa estructurada en un esquema en estrella (*Star Schema*) para auditar transacciones, evaluar rendimiento comercial por género/canal, analizar la demanda mediante *Small Multiples* y controlar métricas financieras y de márgenes (`Profit`, `Profit_Margin`) en **2021**.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguajes:** Python, SQL, DAX
* **Librerías de Ciencia de Datos:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, SQLite3
* **Business Intelligence:** Microsoft Power BI, Power Query, Modelado Dimensional (*Star Schema*)
* **Entornos de Trabajo:** Jupyter Notebooks, VS Code
* **Control de Versiones:** Git y GitHub

---

## ⚙️ Cómo Ejecutar los Proyectos Localmente

Si deseas replicar los análisis y ejecutar los scripts o notebooks en tu entorno local, sigue estos pasos:

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git](https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git)
   cd PORTAFOLIO-DE-CIENCIA-DE-DATOS
