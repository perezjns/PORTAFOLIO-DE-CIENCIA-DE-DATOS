# 📊 Cuadro de Mandos Corporativo — Adventure Works Cycles

Documentación analítica, arquitectónica y funcional del modelo de Power BI desarrollado para **Adventure Works Cycles**, procesando catálogos y registros de transacciones en Norteamérica y Europa para el ejercicio **2021**.

---

## 🛠️ Tecnologías y Herramientas
* **Power BI Desktop:** Modelado semántico, diseño de visualizaciones y paneles interactivos.
* **Power Query (M):** Transformación, limpieza y estructuración de datos.
* **DAX:** Implementación de medidas financieras y de rendimiento.
* **Git & GitHub:** Control de versiones y despliegue.

---

## 📑 Estructura y Desglose Analítico por Páginas

### 1. Detalle de Transacciones, Dispersión de Ventas y Catálogo
* **Propósito:** Auditar transacciones individuales (`Order_ID`, `Product_SKU`, `Order_Quantity`, `Sales_Amount`) y evaluar correlaciones entre coste, precio y volumen.
* **Componentes:** Tabla detallada de transacciones, gráfico de dispersión superior (*COGS* vs *Sales Amount*) y gráfico de dispersión inferior por nombre de producto.
* **Filtros Clave:** `Year` (2021), `Product_Name` (selección múltiple) y `Product_Category` (*Tank Tops*).

### 2. Análisis de Ventas por Género, Canal y Rendimiento (Women)
* **Propósito:** Evaluar el rendimiento comercial de la línea femenina (`Women`) segmentado por género y canal de distribución.
* **Componentes:** Gráfico de barras horizontales con ranking de ingresos por producto (destacando *Hera Pullover Hoodie* con más de £10,000 y *Typhon Performance Fleece*) con líneas de referencia de rendimiento medio.
* **Filtros Clave:** `Gender` (*Women*), `Channel` (*Franchise*, *Local store*, etc.) y filtro de página `Order_Date - Year` (2021).

### 3. Distribución del Volumen de Pedidos por Canal y Categoría
* **Propósito:** Comparar el volumen total de pedidos (`Total Order Quantity`) canalizado por los diferentes tipos de distribución comercial y su desglose por categoría.
* **Componentes:** Gráfico de barras horizontales apiladas por canales (*Franchise*, *Local store*, *Supermarket*, *Small chain store*) segmentadas por categorías de producto (*Bras & Tops*, *Hoodies & Sweatshirts*, *Jackets*, etc.).

### 4. Análisis Multidimensional de Demanda (Small Multiples)
* **Propósito:** Analizar la cantidad de pedidos (`Order_Quantity`) de manera cruzada empleando múltiplos pequeños (*Small Multiples*).
* **Componentes:** Matriz de gráficos de columnas organizada por colores del catálogo (*Black, Blue, Gray, Red*, etc.) contrastando volúmenes entre géneros (*Men* vs *Women*).
* **Filtros Clave:** `Product_Category` (*Hoodies & Sweatshirts*) y `Retailer_Channel` (*Franchise*).

### 5. Cuadro de Mando Financiero (Ingresos, Costes, Beneficios y Márgenes)
* **Propósito:** Ofrecer una perspectiva macroeconómica de rentabilidad temporal, cruzando ventas netas frente a costes de producción y márgenes por categoría.
* **Componentes:** 
  * Gráfico de líneas superior: Evolución mensual de Ingresos (`Sales_Amount`), COGS y Beneficio neto (`Profit`).
  * Gráfico combinado inferior: Beneficio absoluto y margen porcentual promedio (`Average of Profit_Margin` oscilando entre 50% y 54%).
  * Gráfico de tornado lateral: Comparativa simétrica de ingresos frente a costes por categoría.

---

## 📐 Arquitectura del Modelo de Datos y Medidas DAX

El modelo implementa un **Esquema en Estrella (*Star Schema*)** optimizado en el motor VertiPaq:
* **Tabla de Hechos (`Fact_Sales`):** Almacena métricas transaccionales aditivas y claves foráneas.
* **Tablas de Dimensión:** `Dim_Product`, `Dim_Channel` y `Dim_Calendar`.

### Medidas DAX Principales:

* **Beneficio Absoluto (`Profit`):**
  ```dax
  Profit = 
  SUM(Fact_Sales[Sales_Amount]) - SUM(Fact_Sales[Cost_of_Goods_Sold])
