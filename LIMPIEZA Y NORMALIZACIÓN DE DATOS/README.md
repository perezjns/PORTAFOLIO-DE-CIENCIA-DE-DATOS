
# 🏢 Canalización de Procesamiento de Datos Inmobiliarios

Este repositorio contiene la solución automatizada para la ingesta, limpieza, normalización y transformación del catálogo de datos extraído de un mercado inmobiliario (`inmuebles.csv`).

El proyecto implementa un script modular optimizado para entornos de producción (**`pipeline_inmuebles.py`**) que automatiza de extremo a extremo la preparación del catálogo.

---

## 📋 Planteamiento del Problema

El dataset original de inmuebles presentaba múltiples desafíos de calidad de datos que impedían su explotación directa en herramientas de Business Intelligence o modelos predictivos:

*   👥 **Registros duplicados** e inconsistencias en identificadores únicos.
*   🔤 **Formatos heterogéneos** en campos de texto (provincias y tipos de operación).
*   ⚪ **Valores nulos** en variables críticas como superficies y precios de salida.
*   🔢 **Tipos de datos incorrectos** (fechas guardadas como texto y números con caracteres especiales).

Este pipeline resuelve dichas inconsistencias aplicando reglas de negocio estrictas de manera secuencial y automatizada.

---

## 🛠️ Arquitectura de la Solución

El script `pipeline_inmuebles.py` está estructurado de forma limpia y modular a través de las siguientes etapas:

📥 [1. Extracción] --------> Carga controlada de 'inmuebles.csv'
│
📝 [2. Limpieza de Texto] -> Eliminación de espacios y normalización de mayúsculas/minúsculas
│
🔢 [3. Casteo de Tipos] ---> Conversión explícita de variables numéricas y fechas
│
🔮 [4. Tratamiento Nulos] -> Imputación inteligente mediante lógicas de agregación
│
📤 [5. Carga] -------------> Exportación del dataset limpio y validado


1.  **Extracción:** Carga controlada del archivo `inmuebles.csv`.
2.  **Limpieza de Texto:** Eliminación de espacios en blanco excedentes y normalización de cadenas en variables categóricas.
3.  **Casteo de Tipos:** Conversión explícita de variables numéricas y tratamiento de series temporales (fechas).
4.  **Tratamiento de Nulos:** Imputación de datos faltantes mediante lógicas de agregación por zona y tipología.
5.  **Carga:** Exportación del conjunto de datos limpio y validado para su posterior consumo.

---

## 📊 Análisis de Resultados e Impacto

La automatización implementada en el pipeline generó las siguientes mejoras críticas en los datos:

*   🗂️ **Consolidación de Variables:** Eliminación del **100%** de la fragmentación en variables de texto (ej. unificación de provincias mal escritas o con espacios).
*   📉 **Integridad Estadística:** Eliminación de valores atípicos por errores de digitación en precios y superficies, normalizando las curvas de distribución.
*   🧠 **Robustez ante Nulos:** Imputación inteligente basada en medianas segmentadas por zona, minimizando el sesgo en el catálogo final.

---

## 🚀 Cómo Ejecutar el Proyecto

### 🧰 Requisitos Previos

Asegúrese de tener instalado Python 3.x y las dependencias necesarias:

```bash
pip install pandas numpy
💻 Ejecución
Coloque su archivo inmuebles.csv en el directorio raíz del proyecto y ejecute el pipeline:

Bash
python pipeline_inmuebles.py
💡 Nota: El script procesará los datos automáticamente y generará un nuevo archivo con el catálogo completamente limpio, estandarizado y listo para su uso inmediato.

📅 Estado del Desarrollo
Producción (pipeline_inmuebles.py): Código consolidado, refactorizado, modular, libre de comentarios redundantes y optimizado para su ejecución directa en entornos de datos o tareas programadas.
