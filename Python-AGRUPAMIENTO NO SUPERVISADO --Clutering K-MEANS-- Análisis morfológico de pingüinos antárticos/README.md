# Agrupamiento de Especies de Pingüinos Antárticos (K-Means Clustering)

Proyecto de ciencia de datos desarrollado para aplicar técnicas de aprendizaje automático no supervisado (**K-Means**) con el fin de identificar y agrupar poblaciones de pingüinos en la Antártida a partir de características morfológicas y biométricas.

## 📌 Origen de los Datos
* **Autora y Fuente:** Dr. Kristen Gorman y la *Palmer Station, Antarctica LTER*, miembro de la *Long Term Ecological Research Network*.
* **Ilustraciones de referencia:** @allison_horst ([GitHub Repository](https://github.com/allisonhorst/penguins)).

---

## 📊 Descripción del Conjunto de Datos (`penguins.csv`)
El conjunto de datos consta de 332 registros limpios y 5 columnas principales:
* **`culmen_length_mm`**: Longitud del culmen (pico) en milímetros.
* **`culmen_depth_mm`**: Profundidad del culmen en milímetros.
* **`flipper_length_mm`**: Longitud de la aleta en milímetros.
* **`body_mass_g`**: Masa corporal en gramos.
* **`sex`**: Sexo biológico del pingüino (`MALE`, `FEMALE`).

---

## ⚙️ Metodología y Enfoques Analíticos

El repositorio evalúa dos enfoques analíticos complementarios para entender la estructura de los datos:

1. **Modelo A (Con Variable de Sexo / K Óptimo):**
   * Codifica la variable categórica `sex` mediante codificación *one-hot* (`pd.get_dummies`).
   * Aplica estandarización con `StandardScaler`.
   * Evalúa la inercia (Método del Codo) y el **Coeficiente de Silueta**, encontrando que particiones de $k = 4$ capturan tanto las diferencias morfológicas entre especies como el dimorfismo sexual intrínseco.

2. **Modelo B (Excluyendo Sexo / Enfoque Biológico Estricto de Especies):**
   * Aisla exclusivamente las 4 variables físicas cuantitativas.
   * Fija $k = 3$ para alinear el modelo con las tres especies nativas conocidas de la región: **Adelie**, **Chinstrap** y **Gentoo**.
   * Genera el DataFrame resumido de medias **`stat_penguins`** requerido para la validación analítica.

---

## 🚀 Código de Implementación en Python

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Carga del conjunto de datos
penguins_df = pd.read_csv("penguins.csv")

# ==========================================
# MODELO A: Con todas las variables (incluyendo 'sex')
# ==========================================
df_encoded_A = pd.get_dummies(penguins_df, columns=['sex'], drop_first=True)
scaler_A = StandardScaler()
df_scaled_A = scaler_A.fit_transform(df_encoded_A)

kmeans_A = KMeans(n_clusters=4, random_state=42, n_init=10)
penguins_df['cluster_modelo_A'] = kmeans_A.fit_predict(df_scaled_A)

# ==========================================
# MODELO B: Excluyendo 'sex' (k = 3 para Especies)
# ==========================================
numeric_cols = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
df_numeric_B = penguins_df[numeric_cols]

scaler_B = StandardScaler()
df_scaled_B = scaler_B.fit_transform(df_numeric_B)

kmeans_B = KMeans(n_clusters=3, random_state=42, n_init=10)
penguins_df['cluster_modelo_B'] = kmeans_B.fit_predict(df_scaled_B)

# Creación del DataFrame de estadísticas promedio por clúster
stat_penguins = penguins_df.groupby('cluster_modelo_B')[numeric_cols].mean()
print("--- DataFrame stat_penguins ---")
print(stat_penguins)
