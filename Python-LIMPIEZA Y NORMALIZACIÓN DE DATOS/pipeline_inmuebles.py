import os
import pandas as pd
import numpy as np
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Evitar advertencias de futuras versiones
warnings.filterwarnings("ignore", category=FutureWarning)

# =====================================================================
# 1. CARGA PORTABLE DEL DATASET
# =====================================================================
# Detecta la carpeta donde está este script independientemente de dónde se guarde
directorio_actual = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
archivo = os.path.join(directorio_actual, 'inmuebles.csv')

print(f"Buscando archivo en: {archivo}\n")

try:
    original = pd.read_csv(archivo)
except FileNotFoundError:
    raise FileNotFoundError(f"⚠️ ¡Error! No se encontró 'inmuebles.csv' en la carpeta: {directorio_actual}. "
                            f"Asegúrate de guardar el script y el CSV juntos en la misma ubicación.")

inmuebles = original.copy()
inmuebles_inicial = original.copy()
punto_control_0 = original.copy()

# 1.2 Mostrar las primeras 5 filas del dataset
print("1.2 Mostrar las primeras 5 filas del dataset")
print(inmuebles.head())

# 1.3 Mostrar las últimas 3 filas del dataset
print("\n1.3 Mostrar las últimas 3 filas")
print(inmuebles.tail(3))

# 1.4 Mostrar las dimensiones del dataset (Filas, Columnas)
print("\n1.4 Mostrar las dimensiones (Filas, Columnas)")
print(inmuebles.shape)

# 1.5 Listar los nombres de todas las columnas
print("\n1.5 Listar los nombres de todas las columnas")
print(inmuebles.columns.tolist())

# =====================================================================
# 2. INFORMACIÓN GENERAL
# =====================================================================
inmuebles_original = punto_control_0.copy()
inmuebles = punto_control_0.copy()

print("\n2.1 Información general del dataset (tipos, memoria, nulos)")
inmuebles.info()

print("\n2.2 Tipos de datos de todas las columnas")
print(inmuebles.dtypes)

punto_control_1 = inmuebles.copy()
print("\n>>> Punto de control 1 creado y listo para el siguiente bloque.")

# =====================================================================
# 3. ESTADÍSTICAS BÁSICAS
# =====================================================================
inmuebles_original = punto_control_1.copy()
inmuebles = punto_control_1.copy()

print("\n**3.1** Mostrar las estadísticas descriptivas básicas de todas las columnas numéricas.")
print(inmuebles.describe().round(1))

print("\n**3.2** Mostrar la distribución de frecuencias de `tipo_inmueble`.")
print(inmuebles['tipo_inmueble'].value_counts())

print("\n**3.3** Calcular y mostrar la media y la mediana de la columna `precio`.")
print(f"Media: {inmuebles['precio'].mean():.2f}")
print(f"Mediana: {inmuebles['precio'].median():.2f}")

print("\n**3.4** Calcular y mostrar la moda de la columna `ciudad`.")
ciudades_moda = inmuebles['ciudad'].mode().tolist()
print(f"Moda: {ciudades_moda}")

punto_control_2 = inmuebles.copy()
print("\n>>> Punto de control 2 creado y listo para el siguiente bloque.")

# =====================================================================
# 4. VALORES NULOS Y DUPLICADOS
# =====================================================================
inmuebles_original = punto_control_2.copy()
inmuebles = punto_control_2.copy()

print("\n**4.1** Contar el número absoluto de valores nulos por columna.")
nulos_absolutos = inmuebles.isnull().sum()
print(nulos_absolutos)

print("\n**4.2** Calcular el porcentaje de valores nulos por columna.")
nulos_porcentaje = (nulos_absolutos / len(inmuebles) * 100).sort_values(ascending=False)
print((nulos_porcentaje.round(2).astype(str) + '%'))

print("\n**4.3** Contar el número total de filas exactamente duplicadas.")
total_duplicados = inmuebles.duplicated().sum()
print(f"Duplicados: {total_duplicados}")

print("\n**4.4** Contar el número de filas duplicadas considerando únicamente `superficie_m2`.")
duplicados_superficie = inmuebles.duplicated(subset=['superficie_m2']).sum()
print(f"Duplicados considerando `superficie_m2`: {duplicados_superficie}")

punto_control_3 = inmuebles.copy()
print("\n>>> Punto de control 3 creado y listo para el siguiente bloque.")

# =====================================================================
# 5. ELIMINACIÓN DE REGISTROS
# =====================================================================
inmuebles_original = punto_control_3.copy()
inmuebles = punto_control_3.copy()

inmuebles = inmuebles.dropna(subset=['superficie_m2', 'habitaciones'], how='all')
inmuebles = inmuebles.dropna(subset=['precio'])
inmuebles = inmuebles.drop_duplicates(keep='last')

filas_finales = len(inmuebles)
filas_iniciales = len(inmuebles_original)
tasa_retencion = (filas_finales / filas_iniciales) * 100

print(f"\n--- RESUMEN DE LIMPIEZA ---")
print(f"Filas originales: {filas_iniciales}")
print(f"Filas tras limpieza: {filas_finales}")
print(f"Datos conservados: {tasa_retencion:.2f}%")
print(f"Filas eliminadas: {filas_iniciales - filas_finales}")

punto_control_4 = inmuebles.copy()
print("\n>>> Punto de control 4 creado y listo para el siguiente bloque.")

# =====================================================================
# 8. IMPUTACIÓN DE NULOS (SOLUCIONADO: Conversión numérica e historial reparado)
# =====================================================================
inmuebles_original = punto_control_4.copy()
inmuebles = punto_control_4.copy()

print("\nNulos antes de empezar el bloque 8:")
print(inmuebles[['ciudad', 'estado_mercado', 'tipo_inmueble', 'superficie_m2']].isnull().sum())

# CONVERSIÓN CRÍTICA: Previene el TypeError forzando la columna a numérico
inmuebles['superficie_m2'] = pd.to_numeric(inmuebles['superficie_m2'], errors='coerce')

#**8.1** Rellenar nulos de `ciudad` usando propagación hacia adelante (`ffill`).
inmuebles['ciudad'] = inmuebles['ciudad'].ffill()

#**8.2** Rellenar nulos de `estado_mercado` con el texto "Desconocido".
inmuebles['estado_mercado'] = inmuebles['estado_mercado'].fillna("Desconocido")

#**8.3** Rellenar nulos de `tipo_inmueble` con su moda.
inmuebles['tipo_inmueble'] = inmuebles['tipo_inmueble'].fillna(inmuebles['tipo_inmueble'].mode()[0])

# 8.4 Rellenar 'superficie_m2' con la media agrupada por 'habitaciones'
inmuebles['superficie_m2'] = inmuebles['superficie_m2'].fillna(inmuebles.groupby('habitaciones')['superficie_m2'].transform('mean'))

print("\nComprobación de nulos por columna post-bloque 8:")
print(inmuebles[['ciudad', 'estado_mercado', 'tipo_inmueble', 'superficie_m2']].isnull().sum())

# Gráfico comparativo de nulos
nulos_antes = inmuebles_original.isnull().sum()
nulos_despues = inmuebles.isnull().sum()
df_comparativa = pd.DataFrame({'Antes de Limpieza': nulos_antes, 'Después de Limpieza': nulos_despues})

df_comparativa.plot(kind='bar', figsize=(10, 6), color=['#ff9999','#66b3ff'])
plt.title('Comparación de valores nulos por columna', fontsize=14)
plt.ylabel('Cantidad de Nulos')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

punto_control_6 = inmuebles.copy()
print("\n>>> Punto de control 6 creado y listo para el siguiente bloque.")

# =====================================================================
# 10. TRATAMIENTO DE OUTLIERS (CAPPING)
# =====================================================================
inmuebles_original = punto_control_6.copy()
inmuebles = punto_control_6.copy()

inmuebles['precio_original'] = inmuebles['precio'].copy()

print("\nSe verifica el precio antes de outliners con un boxplot...")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 4))
sns.boxplot(x=inmuebles['precio_original'], color='salmon')
plt.title('Precios antes del Capping', fontsize=14)
plt.xlabel('Precio en Euros')
plt.show()

limite_inferior = inmuebles['precio'].quantile(0.01)
limite_superior = inmuebles['precio'].quantile(0.99)
inmuebles['precio'] = inmuebles['precio'].clip(lower=limite_inferior, upper=limite_superior)

print(f"\n**10.1 & 10.2** Capping completado.")
print(f"Límite inferior (P0.01): {limite_inferior:,.2f}€ | Límite superior (P0.99): {limite_superior:,.2f}€")

plt.figure(figsize=(10, 4))
sns.boxplot(x=inmuebles['precio'], color='salmon')
plt.title('Precios después del Capping', fontsize=14)
plt.xlabel('Precio en Euros')
plt.show()

punto_control_7 = inmuebles.copy()
print("\n>>> Punto de control 7 creado y listo para el siguiente bloque.")

# =====================================================================
# 11. ESCALADO Y NORMALIZACIÓN
# =====================================================================
inmuebles_original = punto_control_7.copy()
inmuebles = punto_control_7.copy()

variables_normalizadas = MinMaxScaler()
columnas_seleccionadas = ['precio', 'superficie_m2']
inmuebles[['precio_norm', 'superficie_norm']] = variables_normalizadas.fit_transform(inmuebles[columnas_seleccionadas])

print("\n**11.1** Muestra de datos normalizados:")
print(inmuebles[['precio_norm', 'superficie_norm']].head())

punto_control_8 = inmuebles.copy()
print("\n>>> Punto de control 8 creado y listo para el siguiente bloque.")

# =====================================================================
# 12. SEGMENTACIÓN Y CUANTILES
# =====================================================================
inmuebles_original = punto_control_8.copy()
inmuebles = punto_control_8.copy()

etiquetas_sup = ['Pequeño', 'Mediano', 'Grande', 'Muy Grande']
inmuebles['rango_superficie'] = pd.qcut(inmuebles['superficie_m2'], q=4, labels=etiquetas_sup)
inmuebles['habitaciones'] = inmuebles['habitaciones'].fillna(inmuebles.groupby('rango_superficie', observed=False)['habitaciones'].transform('median'))

inmuebles['categoria_precio'] = pd.cut(inmuebles['precio'], bins=3, labels=['Económico', 'Estándar', 'Premium'])

punto_control_9 = inmuebles.copy()
print("\n>>> Punto de control 9 creado y listo para el siguiente bloque.")

# =====================================================================
# GRAFICACIÓN DE VERIFICACIONES DEL BLOQUE 12
# =====================================================================
print("\nGenerando gráficos de verificación de datos del bloque 12...")
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

sns.boxplot(data=inmuebles, x='rango_superficie', y='superficie_m2', hue='rango_superficie', palette='viridis', legend=False, ax=axes[0])
axes[0].set_title('12.1: Distribución de Superficie', fontsize=13, fontweight='bold')

sns.barplot(data=inmuebles, x='rango_superficie', y='habitaciones', estimator='median', hue='rango_superficie', palette='magma', legend=False, ax=axes[1])
axes[1].set_title('12.2: Mediana de Habitaciones', fontsize=13, fontweight='bold')

sns.histplot(data=inmuebles, x='precio', hue='categoria_precio', multiple="stack", palette='coolwarm', bins=30, ax=axes[2])
axes[2].set_title('12.3: Segmentación de Precio', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.show()

punto_control_10 = inmuebles.copy()
print("\n>>> Punto de control 10 creado y listo para el siguiente bloque.")

# =====================================================================
# 13. LIMPIEZA DE TEXTO Y ESTANDARIZACIÓN
# =====================================================================
inmuebles_original = punto_control_10.copy()
inmuebles = punto_control_10.copy()

regex_castellano = r'[^a-záéíóúñ\s]'
inmuebles['descripcion'] = (inmuebles['descripcion'].astype(str).str.lower().str.replace(regex_castellano, '', regex=True).str.strip())
inmuebles['estado_mercado'] = inmuebles['estado_mercado'].astype(str).str.strip().str.title()

punto_control_11 = inmuebles.copy()
print("\n>>> Punto de control 11 creado y listo para el siguiente bloque.")

# =====================================================================
# 14. CODIFICACIÓN DE CATEGORÍAS
# =====================================================================
inmuebles_original = punto_control_11.copy()
inmuebles = punto_control_11.copy()

escala_precios = {'Económico': 1, 'Estándar': 2, 'Premium': 3}
inmuebles['categoria_precio_cod'] = inmuebles['categoria_precio'].map(escala_precios)

categorias_ordenadas = ['Pequeño', 'Mediano', 'Grande', 'Muy Grande']
inmuebles['rango_superficie'] = pd.Categorical(inmuebles['rango_superficie'], categories=categorias_ordenadas, ordered=True)
inmuebles['rango_superficie_cod'] = inmuebles['rango_superficie'].cat.codes

if 'tipo_inmueble' in inmuebles.columns:
    inmuebles = pd.get_dummies(inmuebles, columns=['tipo_inmueble'], drop_first=True, dtype=int)

punto_control_12 = inmuebles.copy()
print("\n>>> Processing secuencial listo.")

# =====================================================================
# PIPELINE INTEGRADO: CLASE AUTOMATIZADA (Estructura final limpia)
# =====================================================================
class LimpiadorInmuebles:
    def __init__(self, etiquetas_sup):
        self.etiquetas_sup = etiquetas_sup
        self.scaler = MinMaxScaler()
        self.escala_precios = {'Económico': 1, 'Estándar': 2, 'Premium': 3}

    def transformar(self, df_original):
        df = df_original.copy()
        
        # 1. Limpieza básica e imputación inicial de tipos
        df = df.dropna(subset=['superficie_m2', 'habitaciones'], how='all')
        df = df.dropna(subset=['precio'])
        df = df.drop_duplicates(keep='last')

        df['superficie_m2'] = pd.to_numeric(df['superficie_m2'], errors='coerce')
        df['ciudad'] = df['ciudad'].ffill()
        df['estado_mercado'] = df['estado_mercado'].fillna("Desconocido")
        df['tipo_inmueble'] = df['tipo_inmueble'].fillna(df['tipo_inmueble'].mode()[0])
        df['superficie_m2'] = df['superficie_m2'].fillna(df.groupby('habitaciones')['superficie_m2'].transform('mean'))
        
        # 2. Capping de Outliers
        limite_inf = df['precio'].quantile(0.01)
        limite_sup = df['precio'].quantile(0.99)
        df['precio'] = df['precio'].clip(lower=limite_inf, upper=limite_sup)

        # 3. Escalado Normalizado
        df[['precio_norm', 'superficie_norm']] = self.scaler.fit_transform(df[['precio', 'superficie_m2']])

        # 4. Segmentaciones y Cuantiles
        df['rango_superficie'] = pd.qcut(df['superficie_m2'], q=len(self.etiquetas_sup), labels=self.etiquetas_sup)
        df['habitaciones'] = df['habitaciones'].fillna(df.groupby('rango_superficie', observed=False)['habitaciones'].transform('median'))
        df['categoria_precio'] = pd.cut(df['precio'], bins=3, labels=['Económico', 'Estándar', 'Premium'])

        # 5. Tratamiento de texto
        regex = r'[^a-záéíóúñ\s]'
        df['descripcion'] = df['descripcion'].astype(str).str.lower().str.replace(regex, '', regex=True).str.strip()
        df['estado_mercado'] = df['estado_mercado'].astype(str).str.strip().str.title()

        # 6. Codificaciones numéricas finales
        df['categoria_precio_cod'] = df['categoria_precio'].map(self.escala_precios)
        df['rango_superficie'] = pd.Categorical(df['rango_superficie'], categories=self.etiquetas_sup, ordered=True)
        df['rango_superficie_cod'] = df['rango_superficie'].cat.codes

        if 'tipo_inmueble' in df.columns:
            df = pd.get_dummies(df, columns=['tipo_inmueble'], drop_first=True, dtype=int)

        return df

# EJECUCIÓN DEL PIPELINE FINAL
mis_etiquetas = ['Pequeño', 'Mediano', 'Grande', 'Muy Grande']
procesador = LimpiadorInmuebles(etiquetas_sup=mis_etiquetas)
inmuebles_final = procesador.transformar(inmuebles_inicial)

print("\n=====================================================================")
print("--- VERIFICACIÓN DE CONSISTENCIA FINAL ---")
print(f"Dimensión Dataset Inicial:             {inmuebles_inicial.shape}")
print(f"Dimensión Dataset tras Paso a Paso:    {punto_control_12.shape}")
print(f"Dimensión Dataset tras Pipeline Clase: {inmuebles_final.shape}")
print("=====================================================================")