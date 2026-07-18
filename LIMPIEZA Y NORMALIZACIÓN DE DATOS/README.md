# Pipeline de Procesamiento de Datos Inmobiliarios

Este repositorio contiene la solución automatizada para la ingesta, limpieza, normalización y transformación del catálogo de datos extraído de un mercado inmobiliario (`inmuebles.csv`).

El proyecto documenta la transición desde un análisis exploratorio e inicial con planteamientos analíticos (**Archivo 301**) hacia un script modular optimizado para entornos de producción (**pipeline_inmuebles.py**).

## 📋Planteamiento del Problema

El dataset original de inmuebles presentaba múltiples desafíos de calidad de datos que impedían su explotación directa en herramientas de Business Intelligence o modelos predictivos:
- Registros duplicados e inconsistencias en identificadores únicos.
- Formatos heterogéneos en campos de texto (provincias y tipos de operación).
- Valores nulos en variables críticas como superficies y precios de salida.
- Tipos de datos incorrectos (fechas guardadas como texto y números con caracteres especiales).

Este pipeline resuelve dichas inconsistencias aplicando reglas de negocio estrictas de manera secuencial y automatizada.

## 🛠️Arquitectura de la Solución

El script final `pipeline_inmuebles.py` elimina los comentarios del proceso de desarrollo y se estructura en las siguientes etapas limpias:

1. **Extracción:** Carga controlada del archivo `inmuebles.csv`.
2. **Limpieza de Texto:** Eliminación de espacios en blanco excedentes y normalización de mayúsculas/minúsculas en variables categóricas.
3. **Casteo de Tipos:** Conversión explícita de variables numéricas y tratamiento de series temporales (fechas).
4. **Tratamiento de Nulos:** Imputación de datos faltantes mediante lógicas de agregación por zona y tipología.
5. **Carga:** Exportación del conjunto de datos limpio y validado para su posterior consumo.

## 📊 Análisis de Resultados e Impacto

La transición del análisis exploratorio (301) al pipeline automatizado (`pipeline_inmuebles.py`) generó las siguientes mejoras en el conjunto de datos:
- **Consolidación de Variables:** Eliminación del 100% de la fragmentación en variables de texto (ej. unificación de provincias mal escritas o con espacios).
- **Integridad Estadística:** Eliminación de valores atípicos por errores de digitación en precios y superficies, normalizando las curvas de distribución.
- **Robustez ante Nulos:** Imputación inteligente basada en medianas segmentadas por zona, minimizando el sesgo en el catálogo final.

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos
Asegúrese de tener instalado Python 3.xy las dependencias necesarias:

```bash
pip install pandas numpy
Ejecución
Coloca tu archivo inmuebles.csv en el directorio raíz del proyecto y ejecuta el pipeline:

Intento
python pipeline_inmuebles.py
El script procesará los datos y generará un nuevo archivo con el catálogo completamente limpio y estandarizado listo para su uso.

📊 Historial del Desarrollo
Fase 1 (Archivo 301): Notas de análisis, pruebas de hipótesis de imputación, planteamiento del problema y código inicial con anotaciones detalladas de cada anomalía encontrada.

Fase 2 (pipeline_inmuebles.py): Código consolidado, refactorizado, modular, libre de comentarios de desarrollo y optimizado para su ejecución directa.
