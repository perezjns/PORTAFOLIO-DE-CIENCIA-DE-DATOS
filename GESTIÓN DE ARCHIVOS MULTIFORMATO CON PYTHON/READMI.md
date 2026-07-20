
# 📊 Pipeline de ETL e Integración de Datos

Este repositorio contiene una solución automatizada en **Python** y **Pandas** para unificar, auditar y analizar fuentes de datos heterogéneas procedentes de múltiples orígenes de negocio.

---

## 🏗️ Arquitectura de Integración (Apartado 0)

El pipeline consolida un **DataFrame Maestro** unificado a partir de tres orígenes de datos con estructuras y formatos complejos:

*   **`pedidos.csv`**: Histórico transaccional codificado en `UTF-16` con delimitador de tubería (`|`).
*   **`productos.db`**: Catálogo relacional administrado en `SQLite` con información de inventario y costes.
*   **`clientes.json`**: Registro de usuarios estructurado mediante objetos anidados multinivel.

📥 pedidos.csv (UTF-16, '|') ──┐
📥 productos.db (SQLite)     ──┼─► [ Limpieza e Ingesta Relacional ] ─► 🛒 DataFrame Maestro
📥 clientes.json (Anidado)   ──┘


---

## 📁 Estructura del Repositorio

El script implementa rutas relativas dinámicas, por lo que detecta automáticamente los archivos maestros siempre que se mantenga la siguiente estructura en la raíz:

```text
📁 tu-repositorio/
├── 📄 main.py            # Pipeline principal y ejecución de bloques analíticos
├── 📄 pedidos.csv        # Historial de transacciones
├── 📄 productos.db       # Base de datos SQLite
└── 📄 clientes.json      # Archivo JSON anidado

🚀 Guía de Uso Rápido
Instalar dependencias necesarias:

Bash
pip install pandas
Ejecutar el análisis global:

Bash
python main.py
🔬 Módulos Analíticos del Script (Apartados 1 al 18)
El software procesa de forma secuencial la información a través de 18 bloques lógicos estructurados en cuatro fases clave:

1. Control de Calidad e Integridad (Apartados 1 - 3)
Aplanamiento dinámico de datos anidados (pd.json_normalize).

Auditoría de consistencia física y cálculo de porcentajes de valores nulos.

Homologación estricta de tipos de datos (Data Types) y métricas centrales (Media, Mediana, Moda).

2. Segmentación Avanzada (Apartados 4 - 6)
Filtrado mediante máscaras booleanas compuestas para aislar transacciones críticas.

Ingeniería de variables temporales para análisis estacionales por día y trimestre.

3. Agregaciones y KPIs (Apartados 7 - 12)
Cálculo de métricas de negocio agrupadas por canales de pago y datos demográficos.

Extracción automatizada de clasificaciones (Top 5 destinos principales).

4. Diagnóstico de Inventario (Apartados 13 - 18)
Control de rotación de stock por categorías y auditoría de registros duplicados.

📊 Reporte de Salida
Al completarse la ejecución, la consola despliega un informe limpio detallando las dimensiones detectadas, el estado de la ingesta relacional y el resumen analítico de cada apartado.


***

### ¿Qué mejoras incluye este diseño?
*   **Cero código redundante:** Eliminados por completo los bloques de Python que sobrecargaban la lectura.
*   **Enfoque funcional:** Explica detalladamente *qué hace* tu script en cada una de sus fases (del Apartado 1 al 18) en lugar de mostrar cómo está programado.
*   **Formateo a prueba de fallos:** Se añadieron separadores estrictos y espaciados limpios para garantiza
