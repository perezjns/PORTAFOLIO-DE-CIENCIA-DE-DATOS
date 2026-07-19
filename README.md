# 📊 Portafolio de Ciencia de Datos

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
</p>

---

## 🔍 Sobre este Portafolio

¡Bienvenido/a a mi espacio de Ciencia de Datos! En este repositorio comparto proyectos prácticos centrados en extraer valor de los datos, diseñar pipelines automatizados, construir modelos predictivos y resolver problemas de negocio utilizando análisis estadístico y aprendizaje automático (*Machine Learning*).

---

## 📁 Estructura del Repositorio

A continuación se detallan los bloques principales de este portafolio. Puedes navegar directamente a cada sección haciendo clic en los enlaces:

| Carpeta / Proyecto | Descripción | Tecnologías Clave |
| :--- | :--- | :--- |
| [📁 ANÁLISIS EXPLORATORIO DE DATOS CON PYTHON](./ANÁLISIS%20EXPLORATORIO%20DE%20DATOS%20CON%20PYT...) | Diagnóstico estadístico, limpieza transaccional y visualización avanzada de series de ventas globales. | `Python`, `Seaborn`, `Estadística` |
| [📁 LIMPIEZA Y NORMALIZACIÓN DE DATOS](./LIMPIEZA%20Y%20NORMALIZACIÓN%20DE%20DATOS) | Automatización del tratamiento de datos mediante pipelines ETL robustos para catálogos inmobiliarios. | `Python`, `Pandas`, `ETL` |
| [📁 MODELADO Y PREDICIÓN CON PYTHON](./MODELADO%20Y%20PREDICIÓN%20CON%20PYTHON) | Modelos predictivos de clasificación/regresión y análisis de variables avanzadas. | `Scikit-Learn`, `Pandas`, `Métricas` |

---

## 🚀 Proyectos Destacados

### 📉 1. Análisis Exploratorio de Datos (Histórico Global de Ventas)
Esta sección aborda un estudio analítico profundo enfocado en la depuración transaccional y la evaluación de tendencias estacionales del negocio.
* **Depuración y Calidad del Dato:** Filtrado de registros corruptos (`###ERROR###`, `-99999`) y aislamiento de duplicados basados en cambios lógicos de estado.
* **Análisis de Series Temporales:** Modelado cronológico de ingresos mensuales consolidados, identificando valles de mercado y picos de facturación históricos.
* **Evaluación de Dispersión:** Análisis estadístico de correlaciones empleando escalas logarítmicas para corregir la alta variabilidad en precios unitarios y volúmenes de pedido.

### 🏢 2. Limpieza y Normalización de Datos (Pipeline Inmobiliario)
Esta sección se enfoca en la ingeniería y preparación de datos (*Data Preparation*), transformando conjuntos de datos brutos e inconsistentes en activos de información fiables y listos para producción.
* **Automatización:** Diseño de un pipeline modular (`pipeline_inmuebles.py`) bajo arquitectura limpia.
* **Sanitización:** Tratamiento inteligente de valores nulos mediante lógicas de agregación por zonas y eliminación de *outliers*.

### 🤖 3. Modelado y Predicción con Python
Desarrollo de modelos predictivos de extremo a extremo (*End-to-End*), aplicando metodologías rigurosas para garantizar la precisión y la interpretabilidad de los resultados.
* **Ingeniería de Características (*Feature Engineering*):** Normalización, escalado y codificación de variables categóricas.
* **Modelado y Evaluación:** Implementación de algoritmos supervisados evaluados con métricas robustas como $R^2$, RMSE, precisión y curvas ROC-AUC.

---

## 🛠️ Tecnologías & Herramientas

* **Lenguajes & Librerías:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn)
* **Entornos:** Jupyter Notebooks, VS Code
* **Control de Versiones:** Git & GitHub

---

## ⚙️ Cómo Ejecutar los Proyectos Localmente

Si deseas replicar los análisis y ejecutar los scripts o notebooks en tu máquina local, sigue estos sencillos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git](https://github.com/perezjsn/PORTAFOLIO-DE-CIENCIA-DE-DATOS.git)
   cd PORTAFOLIO-DE-CIENCIA-DE-DATOS
Crear y activar un entorno virtual (Recomendado):

Bash
python -m venv env
# En Windows:
env\Scripts\activate
# En macOS/Linux:
source env/bin/activate
Instalar las dependencias necesarias:

Bash
pip install -r requirements.txt
(Nota: Asegúrate de que el archivo requirements.txt contenga las librerías necesarias como pandas, numpy, scikit-learn, matplotlib y seaborn).

✉️ Contacto
¿Te interesa mi trabajo o te gustaría colaborar en algún proyecto? ¡Hablemos!

GitHub: perezjsn

LinkedIn: Jeanette Pérez Carnota

Email: jpcarnota@yahoo.es
