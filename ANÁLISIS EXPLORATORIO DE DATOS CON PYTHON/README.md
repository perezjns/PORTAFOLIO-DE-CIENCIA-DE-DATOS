📊 E-Commerce Global Sales Analytics

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-indigo.svg?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-orange.svg?style=flat-square)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-blueviolet.svg?style=flat-square)](https://seaborn.pydata.org/)

Un pipeline integral de **Ciencia de Datos** y **Análisis Estadístico** diseñado para procesar, depurar y extraer conocimiento de históricos transaccionales globales. El proyecto transforma registros en bruto en métricas financieras y patrones demográficos listos para la toma de decisiones gerenciales de alto impacto.

---

## 🎯 Objetivos del Proyecto

*   **Limpieza de Datos Avanzada:** Identificación y aislamiento de anomalías, valores vacíos, duplicados lógicos (múltiples estados para un solo pedido) y registros con valores de prueba (`###ERROR###`, `-99999`).
*   **Análisis Temporal y Estacional:** Evaluación de ciclos macroeconómicos y picos de facturación consolidados a nivel mensual durante un rango de 25 observaciones continuas.
*   **Segmentación Demográfica y de Comportamiento:** Estudio detallado de la distribución por edad, género, métodos de pago predilectos y su relación con los niveles de fidelización (*Bronce, Plata, Oro, Platino*).
*   **Análisis de Correlación y Dispersión:** Demostración estadística de la correlación de variables numéricas con transformaciones logarítmicas frente a datos de alta dispersión.

---

## 📂 Arquitectura del Pipeline y Scripting

El core del desarrollo está implementado en un script automatizado que procesa el flujo en fases modulares autónomas e independientes del entorno (`os.path` dinámico):

```
├── README.md                 <- Este documento con el resumen ejecutivo.
├── main_analytics.py         <- Script principal de procesamiento y visualización.
└── dataset_global_limpio.csv <- Dataset central estructurado con el histórico transaccional.
```

### Flujo Crítico de Ejecución:
1.  **Ingesta Desacoplada y Tipado Eficiente:** Lectura optimizada del archivo CSV controlando advertencias de tipos mixtos mediante coerciones explícitas (`pd.to_numeric`, `pd.to_datetime`).
2.  **Depuración y Validación Estadística:** Exclusión estructurada de outliers mediante métodos avanzados de agregación (`.groupby().tail(1)`) para conservar únicamente el último estado válido de una transacción.
3.  **Generación de Ventanas Emergentes (Visualizaciones):**
    *   *Tendencias:* Gráficos de líneas con marcadores cronológicos para la evolución mensual de ingresos por categoría.
    *   *Distribuciones:* Histogramas con curvas de estimación de densidad kernel (KDE) para edades por género.
    *   *Dispersión:* Análisis mediante diagramas de cajas (`Boxplot` / `Boxenplot`) y gráficos de regresión (`sns.regplot`) en escala logarítmica.

---

## 📈 Hallazgos Clave e Insights Estadísticos

A partir del procesamiento unificado, se extrajeron métricas de alto impacto financiero:

*   **Volumen Consolidado de Facturación:** `$121,251,793.19` a lo largo del periodo analizado.
*   **Rendimiento Promedio Mensual:** `$4,850,071.73` con una desviación estándar de `$1,062,574.45`, denotando la naturaleza cíclica del negocio.
*   **Comportamiento Estacional:** Se evidencia un incremento sistemático de la actividad hacia el último trimestre del año impulsado por campañas comerciales, alcanzando el **máximo histórico absoluto en Noviembre 2024 (`$6,466,503.12`)**.
*   **Conclusión de Correlación:** Tras remover valores negativos anómalos, el coeficiente de correlación cantidad-total mejoró notablemente. No obstante, el uso de escalas logarítmicas demostró que una regresión lineal tradicional no es adecuada debido a la **alta dispersión inherente** al comportamiento de los precios unitarios.

---

## 🛠️ Tecnologías y Requisitos

El proyecto requiere un entorno con Python 3.8 o superior y las siguientes librerías de análisis de datos:

```bash
pip install pandas numpy matplotlib seaborn
```

### Ejecución instantánea:
Coloca el script y el archivo `dataset_global_limpio.csv` en la misma carpeta y ejecuta:
```bash
python main_analytics.py
```

---

*Desarrollado con rigor metodológico para la optimización de canales comerciales y la inteligencia de negocio.*
