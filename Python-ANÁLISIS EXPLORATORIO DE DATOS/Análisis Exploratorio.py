import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================================================================
# DETECCIÓN DINÁMICA DE LA CARPETA ACTUAL (Permite abrirse en cualquier carpeta)
# ==============================================================================
try:
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Fallback por si se ejecuta en entornos interactivos de terminal
    directorio_actual = os.getcwd()

nombre_archivo = "dataset_global_limpio.csv"
ruta = os.path.join(directorio_actual, nombre_archivo)

print(f"=== Buscando archivo de datos en: {ruta} ===")

if not os.path.exists(ruta):
    print(f"⚠️ Error: No se encontró '{nombre_archivo}' en la misma carpeta que este script.")
    print(f"Asegúrate de copiar el CSV en: {directorio_actual}")
    exit()

# Carga de datos local
ventas = pd.read_csv(ruta, sep=",", encoding="utf-8", low_memory=False)

print()
# 2.1 Se visualiza la cabecera de cada columna para identificar que informacion contiene
print("2.1 Se visualiza la cabecera de cada columna para identificar que informacion contiene")
print(ventas.columns.tolist())
print()

# Todas los datos contenidos en las columnas de fecha se transforman a tipo de dato "fecha"
ventas['fecha_pedido'] = pd.to_datetime(ventas['fecha_pedido'], errors='coerce')
ventas['fecha_registro'] = pd.to_datetime(ventas['fecha_registro'], errors='coerce')
ventas['fecha_alta'] = pd.to_datetime(ventas['fecha_alta'], errors='coerce')

# Los datos contenidos en la columna total se transforman a tipo de dato "numérico"
ventas['total'] = pd.to_numeric(ventas['total'], errors='coerce')

# Los datos se agrupan por mes
ventas['mes'] = ventas['fecha_pedido'].dt.to_period('M')
print()

# 2.2 Agrupar por mes y sumar los totales
print ("2.2 Agrupar por mes y sumar los totales\n")
ventas_mensuales = ventas.groupby('mes')['total'].sum().reset_index()
ventas_mensuales['mes'] = ventas_mensuales['mes'].dt.to_timestamp()
print(ventas_mensuales)
print()

# 2.3 Gráfico de líneas con marcadores
print("2.3 Gráfico de líneas con marcadores")
plt.figure(figsize=(14,8))
plt.plot(ventas_mensuales['mes'],ventas_mensuales['total'],marker='o',linestyle='-')
plt.title('Ventas por mes')
plt.xlabel('Meses')
plt.ylabel('Total Ventas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show() # Ventana emergente 1

# Los datos contenidos en la columna edad se transforman a tipo de dato "numérico"
ventas['edad'] = pd.to_numeric(ventas['edad'], errors='coerce')

print ("4.1 Agrupar por edad y contar clientes para comparar resultados con la gráfica\n")
ventas_edad = ventas.groupby('edad')['edad'].count()
print(ventas_edad)
print()

# Crear gráfico distribución edad
plt.figure(figsize=(10,6))
intervalos = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

sns.histplot(ventas['edad'],bins=intervalos,color='skyblue',edgecolor='white',kde=True)
#kde es para dibujar línea de tendencia

plt.title('Distribución de edad de los clientes', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Número de clientes', fontsize=14)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # Ventana emergente 2


# Comparación de precio unitario por categoría de producto
print("5.1 Comparación de precio unitario por categoría de producto")
comparacion_precio_categoria = ventas.groupby('categoria')['precio_unitario'].describe()
print(comparacion_precio_categoria)
print()

plt.figure(figsize=(10,6))
categorias = ventas['categoria'].unique()
palette_custom = dict(zip(categorias, sns.color_palette("Set3", len(categorias))))

sns.boxenplot(data=ventas, x='categoria', y='precio_unitario', hue='categoria', palette=palette_custom)
plt.title('Distribución de precio unitario por categoría de producto')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() # Ventana emergente 3


# Relación entre Cantidad y Total
print("7.1 Relación entre Cantidad y Total")
ventas_estadisticas_cantidad_total=ventas[['cantidad','total']].describe().round(2)
print(ventas_estadisticas_cantidad_total)
print()

# Se ordenan los valores
ventas[['cantidad','total']].sort_values('total', ascending=False)

# Se ordenan los valores
print("7.2 Cálculo de la correlación antes de graficar para anticiparse al resultado")
coeficiente_de_correlacion = ventas[['cantidad','total']].corr()
print(coeficiente_de_correlacion)
print()

print("el valor de 1 (no en diagonal) sería una correlación perfecta y 0 sin correlación, por lo que en este caso se sabe antes")
print("de crear el gráfico que no hay ninguna relación entre ambas variables. Esto se traduce desde el punto de vista estadístico")
print("como datos con ALTA DISPERSIÓN")
print()

plt.figure(figsize=(10,6))
plt.scatter(ventas['cantidad'], ventas['total'], color='skyblue', alpha=0.7, label='Pedidos')
plt.title('Relación entre cantidad y total de pedidos', fontsize=16)
plt.xlabel('Cantidad', fontsize=14)
plt.ylabel('Total', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # Ventana emergente 4

# Filtrado de valores negativos
print("7.3 Filtrado de valores negativos")
ventas_filtradas_1 = ventas[ventas['total'] >= 0]
print("7.2 Cálculo de la correlación antes de graficar para anticiparse al resultado")
coeficiente_de_correlacion_1 = ventas_filtradas_1[['cantidad','total']].corr()
print(coeficiente_de_correlacion_1)
print()

print("Quitando los valores negativos el valor de la correlación mejora signifivamente, posicionándose más cercana a 1")
print("aunque la dispersión sigue siendo alta, se obtienen valores más lógicos")
print()

plt.figure(figsize=(10,6))
plt.scatter(ventas_filtradas_1['cantidad'], ventas_filtradas_1['total'], color='skyblue', alpha=0.7)
plt.title('Relación entre cantidad y total de pedidos', fontsize=16)
plt.xlabel('Cantidad', fontsize=14)
plt.ylabel('Total', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # Ventana emergente 5
print()

print("Análisis: por ejemplo, para cantidad = 1, los totales van desde 0 hasta 20.000, esto indica gran variabilidad")
print("en los totales para la misma cantidad. Esto es consistente con lo obtenido anteriormente con el coeficiente de ")
print("correlación el cual indica alta dispersión")
print ("En este caso, quizás, sea más útil un Boxplot por Cantidad")
print()

plt.figure(figsize=(10,6))
ventas_filtradas_1.boxplot(column='total',by='cantidad', grid=False)
plt.title('Distribución de total según cantidad de pedido', fontsize=16)
plt.xlabel('Cantidad', fontsize=14)
plt.ylabel('Total', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # Ventana emergente 6

plt.figure(figsize=(10,6))
# Scatter plot con línea de regresión
sns.regplot(x='precio_unitario', y='total', data=ventas, scatter_kws={'color':'blue', 'alpha':0.6}, line_kws={'color':'red'})
plt.title('Relación entre precio unitario y total')
plt.xlabel('Precio Unitario')
plt.ylabel('Total')
plt.grid(True)
plt.tight_layout()
print()
plt.show() # Ventana emergente 7

print("Igual que en el apartado anterior el gráfico se ve afectado por los valores de los datos por lo tanto, se")
print("utilizá el análisis de datos ya efectuado de exclusión de datos, el cual ya ha sido detallado en el apartado 7")
print()

print("CONSIDERANDO EL COMPORTAMIENTO DE CRECIMIENTO DE LOS DATOS, SE UTILIZÓ ESCALA LOGARÍTMICA EN EL EJE X -PRECIO-")
print("Y EN EL EJE Y -TOTAL- PARA MEJORAR SU VISUALIZACIÓN, DE LA CUAL SE CONCLUYE QUE LA DISPERSIÓN DE LOS DATOS ES")
print("MUY ALTA, POR LO QUE UNA REGRESIÓN LINEAL NO ES LA MÁS ADECUADA PARA ESTE CONJUNTO DE DATOS EN PARTICULAR")
print()

plt.figure(figsize=(14,8))
sns.regplot(x='precio_unitario', y='total', data=ventas_filtradas_1, scatter_kws={'color':'blue', 'alpha':0.6}, line_kws={'color':'red'})
plt.xscale('log')
plt.yscale('log')
plt.title('Relación entre precio unitario y total (Escala Logarítmica)', fontsize=18)
plt.xlabel('Precio Unitario', fontsize=14)
plt.ylabel('Total', fontsize=14)
plt.grid(True, which="both", linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() # Ventana emergente 8


print ("Determinar si hay pedidos repetidos o vacios \n")

print("10.1 Conteo de pedidos repetidos (más de un estado distinto por Id Pedido):\n")
estados_distintos_por_pedido = ventas.groupby("Id Pedido")["estado_pedido"].nunique()
pedidos_repetidos = estados_distintos_por_pedido[estados_distintos_por_pedido > 1]
print(pedidos_repetidos)
print()

print("10.2 Limpieza de la base de datos(valores vacíos y duplicados):\n")
ventas_limpias = ventas.dropna(subset=["Id Pedido", "estado_pedido"])
ventas_limpias = ventas_limpias.sort_values(by=["Id Pedido", "fecha_pedido"])
ventas_limpias = ventas_limpias.groupby("Id Pedido").tail(1)

# Filtro de anomalías o textos no deseados en los estados del pedido
valores_invalidos = [-99999.0, 3.0, "###ERROR###", "-", -99999]
ventas_limpias = ventas_limpias[~ventas_limpias['estado_pedido'].isin(valores_invalidos)]

print("Resumen de la data definitiva vs. data original\n")
print(f"Registros originales: {len(ventas)}")
print(f"Registros después de limpieza: {len(ventas_limpias)}")
print(f"Pedidos eliminados: {len(ventas) - len(ventas_limpias)}")
print()

estados_distintos_por_pedido_2 = ventas_limpias.groupby("Id Pedido")["estado_pedido"].nunique()
pedidos_repetidos_2 = estados_distintos_por_pedido_2[estados_distintos_por_pedido_2 > 1]
print(pedidos_repetidos_2)  
print()

conteo_estado = ventas_limpias['estado_pedido'].value_counts()

plt.figure(figsize=(10,6))
plt.bar(conteo_estado.index.astype(str), conteo_estado.values, color="violet")
plt.xlabel("Estado del Pedido")
plt.ylabel("Cantidad de Pedidos")
plt.title("Cantidad de pedidos por estado (datos depurados)")
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show() # Ventana emergente 9


print("NOTA: Para este ejercicio se utiliza la data depurada en el ejercicio anterior")
print()

plt.figure(figsize=(12,6))
sns.countplot(data=ventas_limpias, x="estado_pedido", hue="metodo_pago", palette="pastel")
plt.title("Cantidad de pedidos por estatus de envio y segmentados por método de pago")
plt.xlabel("Estado del Pedido")
plt.ylabel("Cantidad de Pedidos")
plt.xticks(rotation=45)  
plt.legend(title="Método de pago", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.tight_layout()
plt.show() # Ventana emergente 10

columnas_numericas = ventas_limpias.select_dtypes(include=[np.number]).columns
matriz_correlacion = ventas_limpias[columnas_numericas].corr()

print("13.1 Se obtiene la matriz de correlación (todas aquellas columnas con datos numéricos)")
print(matriz_correlacion)
print()

plt.figure(figsize=(8, 6))
sns.heatmap(matriz_correlacion, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
plt.title("Matriz de correlación de variables numéricas")
plt.tight_layout()
plt.show() # Ventana emergente 11

print("14.1 Verificación de formato fecha en columna fecha_pedido:")
formato_fecha = ventas_limpias['fecha_pedido'].dtype
print(formato_fecha)

ventas_limpias['mes'] = ventas_limpias['fecha_pedido'].dt.to_period('M')
ventas_mensuales = ventas_limpias.groupby(['mes', 'categoria'])['total'].sum().reset_index()
ventas_mensuales['mes'] = ventas_mensuales['mes'].dt.to_timestamp()

sns.set_theme(style="whitegrid", palette="tab10")
plt.figure(figsize=(14,8))

categorias = ventas_mensuales['categoria'].unique()
markers = ['o', 's', '^', 'D', 'v', 'P', '*']

for i, categoria in enumerate(categorias):
    datos = ventas_mensuales[ventas_mensuales['categoria'] == categoria]
    plt.plot(datos['mes'], datos['total'], marker=markers[i % len(markers)], linestyle='-', label=categoria)

plt.title("Evolución mensual del total de ventas por categoría (data depurada)", fontsize=16)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Total ventas", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Categoría", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show() # Ventana emergente 12

print("15.1 Determinación de la edad mínima y máxima")
edad_min = ventas_limpias['edad'].min()
edad_max = ventas_limpias['edad'].max()
print(f"Edad mínima: {edad_min} | Edad máxima: {edad_max}")

bins = np.arange(25, 91, 5)

plt.figure(figsize=(10,6))
sns.histplot(data=ventas_limpias, x='edad', hue='genero', bins=bins, kde=True, multiple="stack")
plt.title("Distribución de edad por género")
plt.xlabel("Edad")
plt.ylabel("Cantidad / Densidad")
plt.tight_layout()
plt.show() # Ventana emergente 13

print("16.1 Verificación niveles fidelización...")
plt.figure(figsize=(10,6))
orden_niveles = ['Bronce', 'Plata', 'Oro', 'Platino']

sns.boxplot(data=ventas_limpias, x='nivel_fidelizacion', y='precio_unitario', order=orden_niveles, hue='nivel_fidelizacion', palette="pastel")
plt.title("Comparación de Precio Unitario según nivel de fidelización", fontsize=16)
plt.xlabel("Nivel de Fidelización")
plt.ylabel("Precio Unitario")
plt.xticks(rotation=30)
plt.legend(title="Fidelización", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show() # Ventana emergente 14

# Top 5 categorías
top5_categorias = ventas_limpias["categoria"].value_counts().head(5)
plt.figure(figsize=(8, 5))
sns.countplot(data=ventas_limpias, y="categoria", order=top5_categorias.index, hue="categoria", palette="pastel", legend=False)
plt.title("Top 5 categorías de productos más frecuentes (data depurada)", fontsize=14)
plt.xlabel("Número de productos")
plt.ylabel("Categoría")
plt.tight_layout()
plt.show() # Ventana emergente 15

print("=== Proceso finalizado por completo ===")