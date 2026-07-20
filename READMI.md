# 📊 Pipeline de Integración de Datos Dinámica & Analítica de Negocio

Este proyecto implementa una solución robusta y dinámica de ingeniería de datos para unificar, limpiar y analizar información procedente de múltiples orígenes heterogéneos: **CSV estructurado con delimitadores complejos**, **Bases de datos relacionales (SQLite)** y **Archivos JSON con anidamiento multinivel**.

---

## 🏗️ Arquitectura del Pipeline y Datos Maestros

El núcleo central del desarrollo (`APARTADO 0`) implementa un cargador relacional que unifica tres fuentes de información clave utilizando **Python**, **Pandas** y **SQLite**:

📥 pedidos.csv (UTF-16, '|') ──┐📥 productos.db (SQLite)     ──┼─► [ Homologación de IDs ] ─► 🛒 pedidos_completo (Data Maestra)📥 clientes.json (Anidado)   ──┘
### Orígenes de Datos Soportados
*   **Pedidos (`pedidos.csv`)**: Archivo codificado en `UTF-16` con separador de tubería (`|`) para el control logístico.
*   **Catálogo de Productos (`productos.db`)**: Base de datos relacional SQLite que provee control de inventarios, categorías y costes unitarios base.
*   **Clientes (`clientes.json`)**: Estructura orientada a objetos anidados complejo que incluye datos demográficos e información geográfica profunda (`direccion.pais`, `direccion.ciudad`).

---

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Procesamiento Core:** `pandas`, `numpy`
*   **Persistencia / Persistencia Relacional:** `sqlite3`
*   **Serialización:** `json`
*   **Estructuras Temporales:** `datetime`

---

## 📂 Guía de Configuración y Ejecución

El script detecta de forma totalmente **dinámica y automatizada** el entorno de ejecución, generando las rutas relativas correspondientes a la ubicación de los archivos maestros sin necesidad de variables de entorno manuales.

### Estructura del Directorio Recomendada

```text
📁 tu-repositorio/
├── 📄 main.py            # Script principal con la lógica analítica
├── 📄 pedidos.csv        # Historial de transacciones (Separador '|')
├── 📄 productos.db       # Catálogo e Inventario (SQLite)
└── 📄 clientes.json      # Base de clientes plana o estructurada
Cómo ejecutar el pipelineAsegúrate de tener las dependencias de Pandas instaladas en tu entorno virtual:Bashpip install pandas numpy
Ejecuta el script de análisis general:Bashpython main.py
🔬 Módulos del Core AnalíticoEl software divide su ejecución en bloques lógicos secuenciales de alto rendimiento:Bloque RelacionalOperación TécnicaObjetivo de NegocioApartado 0pd.json_normalize & pd.mergeAplanamiento y cruce relacional robusto (Data Maestra).Apartado 1 & 2info(), isnull().sum()Auditoría de integridad física y porcentajes de nulos.Apartado 3pd.to_numeric & describe()Limpieza de tipos de datos, cálculo de Media, Mediana y Modas.Apartado 4 & 5Máscaras Booleanas CombinadasIdentificación de pedidos Premium (>500€) y Críticos.Apartado 6Parseo temporal con dtSegmentaciones temporales, trimestrales y días de la semana.Apartado 7 al 12.groupby().agg()KPIs estratégicos por canal de pago, género y Top 5 Destinos.Apartado 13 al 18Diagnósticos de calidadControl de Stock por categoría y tasas de duplicación.📝 Fragmento Destacado: Cruce de Datos DinámicoEl siguiente bloque de código ilustra la lógica utilizada para resolver el anidamiento de los clientes e integrarlo con el flujo general de transacciones de la plataforma:Python# Carga y aplanado de datos JSON anidados (clientes.json)
with open(ruta_clientes, 'r', encoding='utf-8') as f:
    data_clientes_json = json.load(f)

# Extracción nativa a columnas relacionales
clientes = pd.json_normalize(data_clientes_json)
clientes = clientes.rename(columns={
    'direccion.pais': 'País envío',
    'direccion.ciudad': 'ciudad'
})

# Homologación e inyección estricta de tipos de datos string para llaves foráneas
pedidos['id_producto'] = pedidos['id_producto'].astype(str).str.strip()
productos['id_producto'] = productos['id_producto'].astype(str).str.strip()

# Unión relacional robusta (Data Maestra completa)
pedidos_productos = pd.merge(pedidos, productos, how="left", on="id_producto")
pedidos_completo = pd.merge(pedidos_productos, clientes, how="left", on="id_cliente")
📈 Resultados Esperados en ConsolaAl ejecutar el script, se desplegará en la terminal un reporte estructurado y legible con la siguiente información clave de auditoría:PlaintextAPARTADO 0. Carga y unión de ficheros
--> ¡Éxito! Cruce correcto garantizado. Coincidencias finales: X registros.

APARTADO 1. Información básica del dataset 
1.1 Mostrar las primeras 5 filas del dataset global
...
2.4 Porcentaje de valores nulos por columna:
...
3.3 Media, Mediana y Moda de 'total':
MEDIA: XXX.XX | MEDIANA: XXX.XX
...
--> Proceso de ejecución finalizado con total integridad física de los datos.
🔧 Desarrollado y optimizado bajo entornos de Análisis Estadístico e Ingeniería de Datos de Alta Concurrencia.
