# Pipeline de ETL e Integración de Datos Dinámica

Este repositorio contiene un pipeline de ingeniería de datos en **Python** diseñado para unificar, limpiar y analizar fuentes de datos heterogéneas. El script automatiza la consolidación de un modelo relacional a partir de tres orígenes de datos con estructuras y formatos complejos.

---

## 🛠️ Arquitectura del Pipeline (Apartado 0)

El núcleo del desarrollo resuelve la ingesta y el acoplamiento de tres fuentes de información con formatos conflictivos:

*   **`pedidos.csv`**: Histórico de transacciones codificado en `UTF-16` con delimitador de tubería (`|`).
*   **`productos.db`**: Base de datos relacional en `SQLite` que contiene el catálogo maestro e inventarios.
*   **`clientes.json`**: Estructura de documentos con anidamiento multinivel para perfiles de usuarios.

### Flujo de Unificación
📥 pedidos.csv (UTF-16, '|') ──┐
📥 productos.db (SQLite)     ──┼─► [ Limpieza e Inyección de Tipos ] ─► 🛒 DataFrame Maestro
📥 clientes.json (Anidado)   ──┘


---

## 📁 Estructura del Proyecto

El script implementa detección dinámica de rutas relativas, por lo que basta con mantener los archivos en el mismo directorio raíz:

```text
📁 tu-repositorio/
├── 📄 main.py            # Pipeline principal y bloques analíticos (Apartados 0-18)
├── 📄 pedidos.csv        # Archivo de transacciones estructurado
├── 📄 productos.db       # Base de datos SQLite
└── 📄 clientes.json      # Estructura JSON anidada
🚀 Instalación y Ejecución
Clonar el repositorio e instalar dependencias:

Bash
pip install pandas
Ejecutar el pipeline analítico:

Bash
python main.py
🔬 Core Analítico e Integridad de Datos
El script ejecuta de forma secuencial 18 módulos de auditoría y análisis estadístico:

Fase 1: Consolidación y Limpieza (0 - 3): Normalización de JSON, control estricto de tipos de datos (Data Types), cálculo de métricas centrales (Media, Mediana, Moda) y mapeo de valores nulos.

Fase 2: Segmentación Avanzada (4 - 6): Máscaras booleanas complejas para la detección de pedidos críticos/Premium e ingeniería de variables temporales (dt.day_name, análisis trimestral).

Fase 3: Agrupaciones y KPIs (7 - 12): Agregaciones multidimensionales (.groupby().agg()) para analizar pasarelas de pago, métricas demográficas y comportamiento geográfico.

Fase 4: Diagnóstico de Calidad (13 - 18): Control de rotación de stock, análisis de dispersión física y auditoría de registros duplicados.

💻 Implementación Clave: Ingesta Dinámica y Merge
Fragmento de código del Apartado 0 centrado en el aplanamiento del JSON jerárquico y la homologación estricta de llaves foráneas (Foreign Keys) para evitar pérdidas de registros en el cruce:

Python
import json
import pandas as pd

# 1. Carga y aplanado nativo de estructuras anidadas
with open('clientes.json', 'r', encoding='utf-8') as f:
    data_clientes = json.load(f)

clientes = pd.json_normalize(data_clientes)
clientes = clientes.rename(columns={
    'direccion.pais': 'País envío',
    'direccion.ciudad': 'ciudad'
})

# 2. Homologación de tipos para evitar fallos de coincidencia por espacios o formatos
pedidos['id_producto'] = pedidos['id_producto'].astype(str).str.strip()
productos['id_producto'] = productos['id_producto'].astype(str).str.strip()

# 3. Construcción del DataFrame Maestro mediante Left Joins
pedidos_productos = pd.merge(pedidos, productos, how="left", on="id_producto")
df_maestro = pd.merge(pedidos_productos, clientes, how="left", on="id_cliente")
📊 Reporte de Salida en Consola
Al ejecutar main.py, la terminal genera un reporte estructurado y limpio dividido por secciones:

Plaintext
======================================================================
[APARTADO 0] Proceso de normalización e ingesta relacional completado.
======================================================================
-> Registros unificados correctamente en DataFrame Maestro.

[APARTADO 1 & 2] Auditoría de Integridad Física:
- Dimensiones del Dataset: (XXXX, XX)
- Porcentaje de valores nulos detectados:
  id_pedido     0.0%
  total         1.2%
  ...

[APARTADO 3] Análisis Descriptivo Central:
- Media de facturación: XXX.XX
- Mediana de transacciones: XXX.XX

--> Ejecución finalizada con éxito. Datos listos para capas de BI o Modelado.

***

### ¿Qué ha cambiado en este rediseño?
1. **Adiós al apelotonamiento:** Se agregaron saltos de línea estratégicos (`\n`) y triples acentos graves (```) cerrados correctamente para forzar a GitHub a interpretar el código y el texto por separado.
2. **Tono Profesional:** Se eliminó el relleno genérico y se orientó a terminología real de ingeniería de datos (*Left Joins, Aplanamiento nativo, Inyección de tipos, Dataframe Maestro*).
3. **Mapeo Claro:** La tabla redundante se cambió por un desglose de fases mucho más limpio de los 18 apartados de tu script.
