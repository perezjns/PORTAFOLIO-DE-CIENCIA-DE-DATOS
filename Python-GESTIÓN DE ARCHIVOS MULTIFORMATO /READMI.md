
# 📊 Pipeline de ETL e Integración de Datos

Este repositorio contiene una solución automatizada en **Python** y **Pandas** para unificar, auditar y analizar fuentes de datos heterogéneas procedentes de múltiples orígenes de negocio.

---

## 🏗️ Arquitectura de Integración (Apartado 0)

El pipeline consolida un **DataFrame Maestro** unificado a partir de tres orígenes de datos con estructuras y formatos complejos:

*   **`pedidos.csv`**
    *   *Tipo:* Histórico transaccional estructurado.
    *   *Formato:* Codificación `UTF-16` con delimitador de tubería (`|`).
*   **`productos.db`**
    *   *Tipo:* Catálogo relacional maestro.
    *   *Formato:* Base de datos administrada en `SQLite` con información de costes.
*   **`clientes.json`**
    *   *Tipo:* Registro demográfico de usuarios.
    *   *Formato:* Estructura JSON con objetos anidados multinivel.

📥 pedidos.csv (UTF-16, '|') ──┐
📥 productos.db (SQLite)     ──┼─► [ Limpieza e Ingesta Relacional ] ─► 🛒 DataFrame Maestro
📥 clientes.json (Anidado)   ──┘


---

## 📁 Estructura del Repositorio

El script implementa detección dinámica de rutas, por lo que localiza automáticamente los recursos siempre que se mantenga la siguiente disposición en la raíz:

```text
📁 tu-repositorio/
├── 📄 main.py            # Pipeline principal y bloques analíticos
├── 📄 pedidos.csv        # Historial de transacciones
├── 📄 productos.db       # Base de datos SQLite
└── 📄 clientes.json      # Archivo JSON anidada

🚀 Guía de Uso Rápido
Instalar dependencias necesarias:

Bash
pip install pandas
Ejecutar el análisis global:

Bash
python main.py
🔬 Módulos Analíticos del Script (Apartados 1 al 18)
El core del software procesa la información de manera secuencial a través de 18 bloques lógicos estructurados con la siguiente jerarquía analítica:

Control de Calidad e Integridad (Apartados 1 - 3)

   Aplanamiento dinámico de estructuras anidadas mediante pd.json_normalize.

   Auditoría de consistencia física con cálculo automatizado de porcentajes de nulos.

   Homologación estricta de tipos de datos (Data Types) y cálculo de métricas centrales (Media, Mediana, Moda).

Segmentación Avanzada (Apartados 4 - 6)

   Filtrado avanzado con máscaras booleanas compuestas para aislar transacciones críticas.

   Ingeniería de variables temporales para análisis estacionales (dt.day_name y trimestres).

Agregaciones y KPIs de Negocio (Apartados 7 - 12)

   Cálculo de métricas de rendimiento agrupadas por canales de pago y datos demográficos.

   Extracción y ordenación automatizada de clasificaciones geográficas (Top 5 destinos principales).

Diagnóstico de Inventario y Calidad (Apartados 13 - 18)

   Control de rotación de stock y disponibilidad física por categorías de producto.

   Auditoría final de la base de datos para la detección y depuración de registros duplicados.

📊 Reporte de Salida en Consola

💡 Nota de ejecución: Al completarse el proceso, la terminal despliega de forma limpia un informe detallado con las dimensiones detectadas, el estado de las uniones relacionales y el resumen analítico estructurado de cada apartado listo para su consumo.
