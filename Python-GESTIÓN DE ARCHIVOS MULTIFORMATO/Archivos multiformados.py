import os
import sqlite3
import pandas as pd
import numpy as np
import json
from datetime import datetime

# =====================================================================
# APARTADO 0. Carga y unión dinámica de ficheros
# =====================================================================
print("APARTADO 0. Carga y unión de ficheros")

# Detectar automáticamente la carpeta donde se encuentra este script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()

# Construir rutas relativas dinámicas
ruta_pedidos = os.path.join(DIRECTORIO_ACTUAL, "pedidos.csv")
ruta_productos = os.path.join(DIRECTORIO_ACTUAL, "productos.db")
ruta_clientes = os.path.join(DIRECTORIO_ACTUAL, "clientes.json")

# 1. Carga del archivo de Pedidos
pedidos = pd.read_csv(ruta_pedidos, sep="|", encoding="utf-16")
pedidos.columns = pedidos.columns.str.strip()

# 2. Carga del archivo de Productos (Base de Datos SQLite)
conexion = sqlite3.connect(ruta_productos)
productos = pd.read_sql_query("SELECT * FROM productos", conexion)
conexion.close()
productos.columns = productos.columns.str.strip()

# 3. Carga y aplanado correcto del archivo de Clientes (JSON Complejo)
with open(ruta_clientes, 'r', encoding='utf-8') as f:
    data_clientes_json = json.load(f)

# pd.json_normalize extrae las propiedades anidadas como 'direccion.pais' y 'direccion.ciudad'
clientes = pd.json_normalize(data_clientes_json)
clientes.columns = clientes.columns.str.strip()

# Renombrar columnas para mantener consistencia con los análisis posteriores del script original
clientes = clientes.rename(columns={
    'direccion.pais': 'País envío',  # O el mapeo que requiera tu lógica de negocio
    'direccion.ciudad': 'ciudad'
})

# Homologación estricta de tipos de datos para evitar desajustes en el merge
pedidos['id_cliente'] = pedidos['id_cliente'].astype(str).str.strip()
clientes['id_cliente'] = clientes['id_cliente'].astype(str).str.strip()

pedidos['id_producto'] = pedidos['id_producto'].astype(str).str.strip()
productos['id_producto'] = productos['id_producto'].astype(str).str.strip()

# Unión relacional robusta (Data Maestra completa)
pedidos_productos = pd.merge(pedidos, productos, how="left", on="id_producto")
pedidos_completo = pd.merge(pedidos_productos, clientes, how="left", on="id_cliente")

print(f"--> ¡Éxito! Cruce correcto garantizado. Coincidencias finales: {len(pedidos_completo)} registros.\n")

# =====================================================================
# APARTADO 1. Información básica del dataset
# =====================================================================
print("APARTADO 1. Información básica del dataset \n")
print("1.1 Mostrar las primeras 5 filas del dataset global\n", pedidos_completo.head())
print("\n1.2 Dimensiones del dataset:\n", pedidos_completo.shape)
print("\n1.3 Nombres de las columnas:\n", pedidos_completo.columns.tolist())
print("\n1.4 Información sobre los tipos de datos de las columnas:\n", pedidos_completo.dtypes)
print("\n1.5 Últimas 3 filas del dataset:\n", pedidos_completo.tail(3))
print()

# =====================================================================
# APARTADO 2: Tipos de datos y valores nulos
# =====================================================================
print("APARTADO 2: Tipos de datos y valores nulos\n")
print("2.1 Información detallada del DataFrame:")
print(pedidos_completo.info())
print("\n2.2 Contar valores nulos por columna:\n", pedidos_completo.isnull().sum())
print("\n2.3 Columnas que tienen valores nulos:\n", pedidos_completo.isnull().sum()[pedidos_completo.isnull().sum() > 0])
print("\n2.4 Porcentaje de valores nulos por columna:\n", (pedidos_completo.isnull().sum() / len(pedidos_completo) * 100).round(2))
print(f"\n2.5 Número de filas completamente vacías: {pedidos_completo.isnull().all(axis=1).sum()}\n")

# =====================================================================
# APARTADO 3: Estadísticas descriptivas y corrección de métricas
# =====================================================================
print("APARTADO 3: Estadísticas descriptivas\n")
columnas_a_float = ["cantidad", "precio_unitario", "total", "precio_base", "descuento", "stock"]
for col in columnas_a_float:
    if col in pedidos_completo.columns:
        pedidos_completo[col] = pd.to_numeric(pedidos_completo[col], errors="coerce").astype("float64")

print("Estadísticas descriptivas de columnas numéricas:\n", pedidos_completo.describe().round(2))
print("\nEstadísticas descriptivas de todas las columnas:\n", pedidos_completo.describe(include='all').round(2))

if 'total' in pedidos_completo.columns:
    print("\n3.3 Media, Mediana y Moda de 'total':")
    print("MEDIA:", round(pedidos_completo['total'].mean(), 2))
    print("MEDIANA:", round(pedidos_completo['total'].median(), 2))
    print("MODA:", pedidos_completo['total'].mode().values)

if 'cantidad' in pedidos_completo.columns:
    print("\n3.4 Rango de la columna 'cantidad':")
    print("MÍNIMO:", pedidos_completo['cantidad'].min())
    print("MÁXIMO:", pedidos_completo['cantidad'].max())
    print("RANGO:", pedidos_completo['cantidad'].max() - pedidos_completo['cantidad'].min())
    print("Cantidad de valores negativos en 'cantidad':", (pedidos_completo['cantidad'] < 0).sum())

print("\n3.5 Desviación estándar y Varianza de 'total':")
print("DESVIACIÓN ESTÁNDAR:", round(pedidos_completo['total'].std(), 2))
print("VARIANZA:", round(pedidos_completo['total'].var(), 2))

print("\n3.6 Conteo de valores únicos en columnas categóricas:")
columnas_categoricas = pedidos_completo.select_dtypes(include=['object', 'category']).columns
for col in columnas_categoricas:
    print(f"\nColumna '{col}' (Valores únicos: {pedidos_completo[col].nunique()}):")
    print(pedidos_completo[col].value_counts().head(10)) # Limitado a los 10 primeros para legibilidad

# =====================================================================
# APARTADO 4 y 5: Segmentación y Filtrados avanzados
# =====================================================================
print("\nAPARTADOS 4 y 5: Operaciones de Filtrado Avanzado\n")
print("4.1 Cantidad > 5 unidades:\n", pedidos_completo[pedidos_completo['cantidad'] > 5].head())
print("4.2 Total > 1000 euros:\n", pedidos_completo[pedidos_completo['total'] > 1000].head())
print("4.3 Precio unitario < 50 euros:\n", pedidos_completo[pedidos_completo['precio_unitario'] < 50].head())
print("4.4 Cantidad igual a 1:\n", pedidos_completo[pedidos_completo['cantidad'] == 1].head())

# Filtros combinados homologando la escritura imperfecta original ('Enviado'/'En', 'Tarjeta'/'Ta', etc.)
pedidos_enviados = pedidos_completo['estado_pedido'].str.strip().str.lower().isin(['enviado', 'en'])
pedidos_tarjeta_paypal = pedidos_completo['metodo_pago'].str.strip().str.lower().isin(['tarjeta', 'ta', 'paypal', 'pa'])
pedidos_criticos = pedidos_completo['estado_pedido'].str.strip().str.lower().isin(['pendiente', 'pe', 'cancelado', 'ca', 'cancelados'])
pedidos_devueltos = pedidos_completo['estado_pedido'].str.strip().str.lower().isin(['devuelto', 'de'])

print("\n5.1 Pedidos enviados con cantidad > 3:\n", pedidos_completo[pedidos_enviados & (pedidos_completo['cantidad'] > 3)].head())
print("5.2 Pedidos Tarjeta/PayPal con total > 500€ (Premium):\n", pedidos_completo[pedidos_tarjeta_paypal & (pedidos_completo['total'] > 500)].head())
print("5.3 Pedidos pendientes/cancelados con cantidad < 2:\n", pedidos_completo[pedidos_criticos & (pedidos_completo['cantidad'] < 2)].head())
print("5.4 Pedidos enviados/devueltos con precio unitario > 100:\n", pedidos_completo[(pedidos_enviados | pedidos_devueltos) & (pedidos_completo['precio_unitario'] > 100)].head())

# =====================================================================
# APARTADO 6: Tratamiento Temporal
# =====================================================================
print("\nAPARTADO 6: Filtrado temporal")
pedidos_completo['fecha_pedido'] = pd.to_datetime(pedidos_completo['fecha_pedido'], errors='coerce')

pedidos_2024 = pedidos_completo[pedidos_completo['fecha_pedido'].dt.year == 2024]
print(f"Número de pedidos en 2024: {len(pedidos_2024)}")
print("Enero 2024:\n", pedidos_completo[(pedidos_completo['fecha_pedido'].dt.year == 2024) & (pedidos_completo['fecha_pedido'].dt.month == 1)].head())
print("Primer Trimestre 2024:\n", pedidos_completo[(pedidos_completo['fecha_pedido'].dt.year == 2024) & (pedidos_completo['fecha_pedido'].dt.month.isin([1, 2, 3]))].head())
print("Pedidos realizados en lunes:\n", pedidos_completo[pedidos_completo['fecha_pedido'].dt.dayofweek == 0].head())

# =====================================================================
# APARTADOS 7, 8 y 9: Métricas agrupadas por Estado, Pago y Destino
# =====================================================================
print("\nAPARTADOS 7, 8 y 9: Agrupaciones Estratégicas")
print("\n7. Ventas y Cantidades por Estado de Pedido:\n", pedidos_completo.groupby('estado_pedido').agg({'total': 'sum', 'cantidad': 'sum'}).round(2))
print("\n8. Distribución por Método de Pago:\n", pedidos_completo.groupby('metodo_pago').agg({'Id Pedido': 'count', 'total': 'sum', 'cantidad': 'mean'}).round(2))

if 'País envío' in pedidos_completo.columns:
    print("\n9. Top 5 Países con mayor volumen de facturación:\n", pedidos_completo.groupby('País envío')['total'].sum().sort_values(ascending=False).head(5))

# =====================================================================
# APARTADOS 10, 11 y 12: Métricas demográficas corregidas de Clientes
# =====================================================================
print("\nAPARTADOS 10, 11 y 12: Análisis Demográfico de Clientes (Corregido)")
# Ahora que el JSON se cargó de manera plana, estas llamadas no fallarán
if 'genero' in pedidos_completo.columns:
    print("\n10. Distribución de clientes únicos por Género:\n", clientes['genero'].value_counts())
    print("\n10.5 Estadísticas de edad generales:\n", clientes['edad'].describe().round(2))
    print("\n10.6 Edad promedio por Género:\n", clientes.groupby('genero')['edad'].mean().round(2))

if 'País envío' in clientes.columns:
    print("\n11. Top 5 Países de residencia de clientes:\n", clientes['País envío'].value_counts().head(5))
if 'ciudad' in clientes.columns:
    print("\n12. Top 5 Ciudades con más clientes:\n", clientes['ciudad'].value_counts().head(5))

# =====================================================================
# APARTADOS 13 al 18: Catálogo, Inventario y Calidad de Datos
# =====================================================================
print("\nAPARTADOS 13 al 18: Análisis de Catálogo y Calidad")
# 13. Agrupaciones de Stock en el dataframe de productos original
productos['stock'] = pd.to_numeric(productos['stock'], errors='coerce')
cat_stock = productos.groupby('categoria')['stock'].sum()
print("\n13. Stock total disponible en almacén por categoría:\n", cat_stock)

# 14. Extremos del catálogo
print("\n14. Productos más caros y más baratos en la data maestra:")
id_max = pedidos_completo['precio_unitario'].idxmax()
id_min = pedidos_completo['precio_unitario'].idxmin()
if pd.notnull(id_max): print("MÁS CARO:\n", pedidos_completo.loc[id_max, ['id_producto', 'precio_unitario']])
if pd.notnull(id_min): print("MÁS BARATO:\n", pedidos_completo.loc[id_min, ['id_producto', 'precio_unitario']])

# 16. Análisis Temporal agrupado por períodos
pedidos_completo['mes'] = pedidos_completo['fecha_pedido'].dt.to_period('M')
print("\n16. Evolución de facturación mensual (€):\n", pedidos_completo.groupby('mes')['total'].sum().head(5))

# 17 & 18. Diagnóstico de Integridad
print(f"\n17. Filas duplicadas en pedidos.csv: {pedidos.duplicated().sum()}")
print(f"18. Porcentaje de valores faltantes por columna en Dataset Completo:\n", (pedidos_completo.isnull().sum() / len(pedidos_completo) * 100).round(2))

print("\n--> Proceso de ejecución finalizado con total integridad física de los datos.")