import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Carga del conjunto de datos
penguins_df = pd.read_csv("penguins.csv")
print("--- Primeras filas del dataset original ---")
print(penguins_df.head())

# ==========================================
# MODELO A: Con todas las variables (incluyendo 'sex' y evaluando k)
# ==========================================
print("\n=== MODELO A: Con Variable 'Sex' ===")
df_encoded_A = pd.get_dummies(penguins_df, columns=['sex'], drop_first=True)
scaler_A = StandardScaler()
df_scaled_A = scaler_A.fit_transform(df_encoded_A)

for k in range(2, 8):
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_temp = kmeans_temp.fit_predict(df_scaled_A)
    score = silhouette_score(df_scaled_A, labels_temp)
    print(f"Modelo A - k={k}: Coeficiente de Silueta = {score:.4f}")

kmeans_A = KMeans(n_clusters=4, random_state=42, n_init=10)
penguins_df['cluster_modelo_A'] = kmeans_A.fit_predict(df_scaled_A)

# ==========================================
# MODELO B: Excluyendo 'sex' y enfocado estrictamente en k = 3 (Especies)
# ==========================================
print("\n=== MODELO B: Excluyendo 'Sex' (k = 3 estricto) ===")
numeric_cols = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
df_numeric_B = penguins_df[numeric_cols]

scaler_B = StandardScaler()
df_scaled_B = scaler_B.fit_transform(df_numeric_B)

for k in range(2, 8):
    kmeans_temp_B = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_temp_B = kmeans_temp_B.fit_predict(df_scaled_B)
    score_B = silhouette_score(df_scaled_B, labels_temp_B)
    print(f"Modelo B (sin sex) - k={k}: Coeficiente de Silueta = {score_B:.4f}")

# Nota: Si tu ejercicio específico de DataCamp utiliza k=4 para el DataFrame final, 
# puedes ajustar n_clusters aquí según la validación del reto.
optimal_clusters = 4 
kmeans_B = KMeans(n_clusters=optimal_clusters, random_state=42, n_init=10)
penguins_df['cluster_modelo_B'] = kmeans_B.fit_predict(df_scaled_B)

# ==========================================
# CREACIÓN DEL DATAFRAME REQUERIDO POR DATACAMP
# ==========================================
# stat_penguins: media de las variables numéricas originales por clúster (sin columnas no numéricas)
stat_penguins = penguins_df.groupby('cluster_modelo_B')[numeric_cols].mean()
print("\n--- DataFrame stat_penguins requerido por DataCamp ---")
print(stat_penguins)

# 2. Resumen estadístico comparativo
print("\n--- Promedios por Clúster detallados ---")
print(stat_penguins)

# 3. Visualización comparativa mediante gráficos lado a lado
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].scatter(
    penguins_df['culmen_length_mm'], 
    penguins_df['body_mass_g'], 
    c=penguins_df['cluster_modelo_A'], 
    cmap='viridis', 
    alpha=0.8, 
    edgecolors='k'
)
axes[0].set_title('Modelo A: k=4 (Incluyendo Sexo)')
axes[0].set_xlabel('Longitud del Culmen (mm)')
axes[0].set_ylabel('Masa Corporal (g)')
axes[0].grid(True)

axes[1].scatter(
    penguins_df['culmen_length_mm'], 
    penguins_df['body_mass_g'], 
    c=penguins_df['cluster_modelo_B'], 
    cmap='plasma', 
    alpha=0.8, 
    edgecolors='k'
)
axes[1].set_title('Modelo B: Agrupamiento con Clústeres Numéricos')
axes[1].set_xlabel('Longitud del Culmen (mm)')
axes[1].set_ylabel('Masa Corporal (g)')
axes[1].grid(True)

plt.tight_layout()
plt.show()