# 📊 Portafolio de Ciencia de Datos & Ingeniería de Datos

## 🔍 Sobre este Portafolio

¡Bienvenido a mi espacio de Ciencia de Datos e Ingeniería de Datos! En este repositorio comparto proyectos prácticos enfocados en extraer valor real de los datos, diseñar pipelines automatizados de extremo a extremo (End-to-End), construir modelos predictivos y resolver problemas de negocio complejos mediante análisis estadístico y aprendizaje automático (*Machine Learning*).

---

## 📁 Estructura del Repositorio

A continuación se detallan los bloques principales que componen este portafolio. Puedes acceder directamente a cada sección explorando las carpetas del repositorio:

| Carpeta / Proyecto | Descripción | Tecnologías Clave |
| :--- | :--- | :--- |
| **📁 ANÁLISIS EXPLORATORIO DE DATOS CON PYTHON** | Diagnóstico estadístico, limpieza transaccional y visualización avanzada de series de ventas globales. | Python, Seaborn, Estadística |
| **📁 GESTIÓN DE ARCHIVOS MULTIFORMATO CON PYTHON** | Ingesta, normalización y cruce relacional dinámico de fuentes heterogéneas (CSV, SQLite, JSON anidados). | Python, Pandas, SQLite, JSON |
| **📁 LIMPIEZA Y NORMALIZACIÓN DE DATOS** | Automatización del tratamiento y curación de datos mediante pipelines ETL robustos para catálogos inmobiliarios. | Python, Pandas, ETL |
| **📁 MODELADO Y PREDICCIÓN CON PYTHON** | Construcción de modelos predictivos de clasificación/regresión y optimización de hiperparámetros. | Scikit-Learn, Pandas, Métricas |

---

## 🚀 Proyectos Destacados

### 📉 1. Análisis Exploratorio de Datos (Histórico Global de Ventas)
Este módulo aborda un estudio analítico profundo enfocado en la depuración transaccional y la evaluación de tendencias estacionales del negocio.
*   **Depuración y Calidad del Dato:** Filtrado sistemático de registros corruptos (`###ERROR###`, `-99999`) y aislamiento de duplicados basados en lógica de estados.
*   **Análisis de Series Temporales:** Modelado cronológico de ingresos mensuales consolidados, identificando valles de mercado y picos de facturación históricos.
*   **Evaluación de Dispersión:** Análisis estadístico de correlaciones empleando escalas logarítmicas para corregir la alta variabilidad en precios unitarios y volúmenes de pedido.

### ⚙️ 2. Gestión de Archivos Multiformato
Implementación de un cargador relacional dinámico capaz de unificar y normalizar orígenes de datos con estructuras conflictivas.
*   **Ingesta Heterogénea:** Procesamiento simultáneo de archivos logísticos en CSV (`UTF-16`, separador `|`), bases de datos relacionales SQLite y archivos JSON con anidamiento multinivel.
*   **Robustez Relacional:** Aplanamiento de datos demográficos y geográficos mediante `pd.json_normalize` junto con homologación estricta de tipos de datos en llaves foráneas para evitar la pérdida de registros.

### 🏢 3. Limpieza y Normalización de Datos (Pipeline Inmobiliario)
Ingeniería y preparación de datos (*Data Preparation*) avanzada, transformando conjuntos de datos brutos e inconsistentes en activos de información confiables listos para producción.
*   **Automatización:** Diseño de un pipeline modular (`pipeline_inmuebles.py`) bajo una arquitectura limpia y reutilizable.
*   **Sanitización Inteligente:** Imputación avanzada de valores nulos mediante lógicas de agregación por zonas geográficas y eliminación controlada de valores atípicos (*outliers*).

### 🤖 4. Modelado y Predicción con Python
Desarrollo de modelos predictivos con metodologías rigurosas para garantizar tanto la precisión matemática como la interpretabilidad de los resultados.
*   **Ingeniería de Características (*Feature Engineering*):** Normalización, escalado estadístico y codificación avanzada de variables categóricas.
*   **Modelado y Evaluación:** Implementación de algoritmos supervisados evaluados mediante métricas robustas de rendimiento ($R^2$, RMSE, precisión y curvas ROC-AUC).

---

## 🛠️ Tecnologías y Herramientas

*   **Lenguajes y Librerías:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, SQLite3)
*   **Entornos de Trabajo:** Jupyter Notebooks, VS Code
*   **Control de Versiones:** Git y GitHub

---

## ⚙️ Cómo Ejecutar los Proyectos Localmente

Si deseas replicar los análisis y ejecutar los scripts o notebooks en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git](https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git)
   cd PORTAFOLIO-DE-CIENCIA-DE-DATOS
