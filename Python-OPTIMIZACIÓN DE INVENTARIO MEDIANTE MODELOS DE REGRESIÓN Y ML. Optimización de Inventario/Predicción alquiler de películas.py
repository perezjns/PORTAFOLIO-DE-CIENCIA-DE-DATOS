import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ==========================================
# 1. CARGA Y PREPROCESAMIENTO DE DATOS
# ==========================================
df = pd.read_csv('rental_info.csv')

# Crear la columna objetivo 'rental_length_days'
df['rental_date'] = pd.to_datetime(df['rental_date'])
df['return_date'] = pd.to_datetime(df['return_date'])
df['rental_length_days'] = (df['return_date'] - df['rental_date']).dt.total_seconds() / (24 * 3600)

# Crear columnas dummy a partir de 'special_features'
df['deleted_scenes'] = df['special_features'].str.contains('Deleted Scenes').astype(int)
df['behind_the_scenes'] = df['special_features'].str.contains('Behind the Scenes').astype(int)

# Definir características (X) y objetivo (y) evitando fugas de información
X = df.drop(columns=['rental_date', 'return_date', 'special_features', 'rental_length_days'])
y = df['rental_length_days']

# Dividir en conjuntos de entrenamiento y prueba (20% test, random_state=9)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9)


# ==========================================
# 2. ENTRENAMIENTO Y EVALUACIÓN DE MODELOS
# ==========================================
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(random_state=9),
    "Gradient Boosting": GradientBoostingRegressor(random_state=9),
    "Random Forest": RandomForestRegressor(random_state=9)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    results[name] = {"MSE": mse, "R2": r2}
    print(f"{name} -> MSE: {mse:.4f} | R²: {r2:.4f}")

# Seleccionar el mejor modelo según el MSE más bajo
best_model_name = min(results, key=lambda x: results[x]['MSE'])
best_model = models[best_model_name]
best_mse = results[best_model_name]['MSE']

print(f"\n[MEJOR MODELO] {best_model_name} con MSE: {best_mse:.4f}")


# ==========================================
# 3. GENERACIÓN DE GRÁFICOS ANALÍTICOS
# ==========================================
sns.set_theme(style="whitegrid")

# --- Gráfico 1: Comparativa de Modelos (MSE y R²) ---
model_names = list(results.keys())
mse_values = [results[m]["MSE"] for m in model_names]
r2_values = [results[m]["R2"] for m in model_names]

fig, ax1 = plt.subplots(figsize=(9, 5))

color = '#1f77b4'
ax1.set_ylabel('MSE (Menor es mejor)', color=color, fontweight='bold', fontsize=11)
bars1 = ax1.bar([x - 0.2 for x in range(len(model_names))], mse_values, width=0.4, color=color, label='MSE')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(range(len(model_names)))
ax1.set_xticklabels(model_names, rotation=15, ha='right', fontweight='bold')
ax1.axhline(3.0, color='crimson', linestyle='--', linewidth=1.8, label='Objetivo de Negocio (MSE ≤ 3.0)')

ax2 = ax1.twinx()  
color = '#ff7f0e'
ax2.set_ylabel('R² Score (Mayor es mejor)', color=color, fontweight='bold', fontsize=11)
bars2 = ax2.bar([x + 0.2 for x in range(len(model_names))], r2_values, width=0.4, color=color, alpha=0.85, label='R² Score')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 1.0)

plt.title('Comparativa de Rendimiento de Modelos de Regresión', fontsize=13, fontweight='bold', pad=15)
fig.tight_layout()
plt.savefig('model_comparison.png', dpi=300)
plt.close()
print("Gráfico 'model_comparison.png' generado con éxito.")


# --- Gráfico 2: Importancia de Variables (Random Forest) ---
rf_model = models["Random Forest"]
importances = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values()

plt.figure(figsize=(9, 6))
importances.plot(kind='barh', color='#2b6cb0', edgecolor='#1a365d')
plt.title('Importancia de Variables en el Modelo Random Forest', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Grado de Importancia', fontweight='bold', fontsize=11)
plt.ylabel('Variables del Dataset', fontweight='bold', fontsize=11)
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300)
plt.close()
print("Gráfico 'feature_importance.png' generado con éxito.")