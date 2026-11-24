# 📊 Análisis de Utilidad, Márgenes y Desempeño Global — Appol (2025–2027)

Dashboard ejecutivo desarrollado en **Microsoft Power BI** para evaluar la rentabilidad financiera, evolución interanual y trimestral, desempeño por línea de negocio y distribución geográfica de **Appol** durante el trienio **2025–2027**.

---

## 🎯 Objetivo del Proyecto

Proporcionar una visión integral del rendimiento operativo y financiero de la compañía mediante un modelo relacional limpio, permitiendo identificar brechas entre volumen de facturación y rentabilidad neta a través de segmentaciones dinámicas por año, categoría y tipo de producto.

---

## 📁 Estructura del Repositorio

* **`Reporte Appol.pbix`**: Archivo principal del informe en Power BI Desktop.
* **`Appol Datos.xlsx`**: Fuente de datos maestra (`Tabla Datos` y `Tabla Productos`).
* **`Appol logo.png`**: Logotipo corporativo.
* **`Fondo.png`**: Plantilla de fondo y distribución visual del lienzo.
* **`inmuebles.csv`**: Archivo auxiliar adjunto (no vinculado al modelo actual).
* **`analisis_calculos_appol.png`**: Gráfico resumen de hallazgos y auditoría.
* **`README.md`**: Documentación técnica y analítica del proyecto.

---

## 🗄️ Arquitectura y Modelo de Datos (ETL)

El modelo conecta una tabla de hechos con una dimensión de catálogo y una tabla dedicada exclusivamente a métricas calculadas:

* **`Tabla Datos` (Hechos — 4.704 registros):** Cobertura completa sin valores nulos ni duplicados para la clave compuesta `(Periodo, Tipo Producto, Region)`. Abarca **12 trimestres** (`Q1 2025` – `Q4 2027`), **7 tipos de producto** y **56 países** (`12 × 7 × 56 = 4.704` combinaciones).
* **`Tabla Productos` (Dimensión — 7 registros):** Catálogo maestro que clasifica los 7 productos en **2 categorías** (`Digital` y `Dispositivos`).
* **Transformaciones aplicadas en Power Query:**
  * Extracción de `Trimestre` (`Q1`–`Q4`) y `Año` (`2025`–`2027`) a partir de `Periodo`.
  * Separación de `Region` (ej. `"USA - América/Estados Unidos"`) mediante delimitadores (`" - "` y `"/"`) en código ISO, `Continente` (5 continentes) y `País` (56 países).

---

## 📐 Medidas DAX y KPIs Globales (2025–2027)

Todas las métricas se centralizan en la tabla `Medidas`:

| Medida | Expresión DAX | Resultado Global (2025–2027) |
| :--- | :--- | :---: |
| **`Total Ingresos`** | `SUM(Datos[Ingresos])` | **USD 3.363.434.207,20** |
| **`Total Gastos`** | `SUM(Datos[Gastos])` | **USD 2.692.324.707,87** |
| **`Utilidad`** | `[Total Ingresos] - [Total Gastos]` | **USD 671.109.499,34** |
| **`Margen`** | `DIVIDE([Utilidad], [Total Ingresos])` | **19,95 %** |

> **Nota técnica:** El margen se evalúa como una razón ponderada dinámica para mantener la exactitud matemática ante cualquier filtro aplicado en los segmentadores.

---

## 🔍 Principales Hallazgos Analíticos

1. **Expansión sostenida de rentabilidad:** La utilidad neta crece un **+10,87 %** entre 2025 (USD 212,07 M) y 2027 (USD 235,13 M), superando el crecimiento de los ingresos (+7,15 %) gracias a una mejora de **+68 puntos básicos** en el margen anual (de 19,59 % a 20,27 %).
2. **Asimetría entre volumen y margen por categoría:**
   * **Dispositivos** *(PC, Celulares, Tablets, Accesorios)* aporta el **75,71 %** de los ingresos (USD 2.546,5 M), pero opera con un margen estrecho del **13,91 %**.
   * **Digital** *(Música, Aplicaciones, TV)* representa el **24,29 %** de los ingresos (USD 816,9 M), pero genera el **47,23 %** de la utilidad total (USD 316,9 M) con un margen promedio del **38,80 %**.
3. **Liderazgo y aceleración regional:**
   * **América** lidera en utilidad neta (USD 262,70 M; 39,14 % del total; margen 22,49 %), seguida de **Asia** (USD 236,20 M; margen 17,14 %).
   * **Europa** es el principal motor de expansión con un crecimiento acumulado del **+71,87 %** en utilidad entre 2025 y 2027.
4. **Concentración geográfica (Pareto):** Los **5 principales países** (Estados Unidos, China, Alemania, India y Canadá) concentran el **68,83 %** de la utilidad global. A nivel granular existen **105 registros trimestrales deficitarios** (`Gastos > Ingresos`), todos concentrados en la categoría *Dispositivos*.

---

## 🖥️ Componentes e Interactividad del Tablero

* **Tarjeta KPI (2 × 2):** Resumen ejecutivo de Ingresos, Gastos, Utilidad y Margen.
* **Evolución Temporal:** Gráfico de barras apiladas por `Año` y `Continente`, acompañado de un gráfico de líneas trimestral (`Año` + `Trimestre`).
* **Distribución Geográfica:** Gráfico de anillo por `Continente`, mapa de burbujas por `País` y tabla ranking de los 56 países con barras de datos en `Utilidad` y formato condicional de gradiente (rojo a verde) en `Margen`.
* **Segmentadores y Marcadores:** Filtros interactivos por `Año`, `Categoria Producto` y `Tipo Producto`, junto con un botón de acción superior derecho vinculado a un marcador (*Bookmark*) para restablecer todos los filtros con un clic.

---

## 🚀 Requisitos y Uso

1. Abrir **`Reporte Appol.pbix`** en **Power BI Desktop** (versión Octubre 2024 o superior).
2. Si deseas actualizar la fuente de datos, asegúrate de apuntar la ruta de origen en *Transformar datos > Configuración de origen de datos* hacia la ubicación local de **`Appol Datos.xlsx`**.
