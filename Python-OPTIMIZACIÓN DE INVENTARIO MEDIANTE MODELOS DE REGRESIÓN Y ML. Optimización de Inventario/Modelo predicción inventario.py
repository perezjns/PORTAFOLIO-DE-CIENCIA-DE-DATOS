# ============================================
# 1. IMPORTAR LAS LIBRERÍAS
# ============================================

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# ============================================
# 2. LEER EL ARCHIVO CSV (Ruta Dinámica Robusta)
# ============================================

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "rental_info.csv")

rental_df = pd.read_csv(csv_path)


# ============================================
# 3. CREAR LA VARIABLE OBJETIVO
# ============================================

rental_df["rental_date"] = pd.to_datetime(rental_df["rental_date"])
rental_df["return_date"] = pd.to_datetime(rental_df["return_date"])

rental_df["rental_length_days"] = (
    rental_df["return_date"] - rental_df["rental_date"]
).dt.days


# ============================================
# 4. CREAR LAS VARIABLES DUMMY
# ============================================

rental_df["deleted_scenes"] = (
    rental_df["special_features"]
    .str.contains("Deleted Scenes", regex=False)
    .astype(int)
)

rental_df["behind_the_scenes"] = (
    rental_df["special_features"]
    .str.contains("Behind the Scenes", regex=False)
    .astype(int)
)


# ============================================
# 5. DEFINIR VARIABLES PREDICTORAS (X) Y OBJETIVO (y)
# ============================================

features = [
    "amount",
    "amount_2",
    "rental_rate",
    "rental_rate_2",
    "release_year",
    "length",
    "length_2",
    "replacement_cost",
    "NC-17",
    "PG",
    "PG-13",
    "R",
    "deleted_scenes",
    "behind_the_scenes"
]

X = rental_df[features]
y = rental_df["rental_length_days"]


# ============================================
# 6. DIVIDIR EN ENTRENAMIENTO Y PRUEBA
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=9
)


# ============================================
# 7. COMPARAR MÚLTIPLES MODELOS AUTOMÁTICAMENTE
# ============================================

models = {
    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        min_samples_leaf=2,
        random_state=9,
        n_jobs=-1
    ),
    "Extra Trees": ExtraTreesRegressor(
        n_estimators=300,
        min_samples_leaf=2,
        random_state=9,
        n_jobs=-1
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=3,
        random_state=9
    ),
    "Hist Gradient Boosting": HistGradientBoostingRegressor(
        max_iter=300,
        learning_rate=0.08,
        max_leaf_nodes=31,
        random_state=9
    ),
    "Linear Regression": LinearRegression()
}

results = {}
trained_models = {}

print("=== ENTRENANDO Y EVALUANDO MODELOS ===")
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    results[name] = mse
    trained_models[name] = model
    print(f"{name}: MSE = {mse:.4f}")


# ============================================
# 8. SELECCIONAR AUTOMÁTICAMENTE EL MEJOR MODELO
# ============================================

best_name = min(results, key=results.get)
best_model = trained_models[best_name]
best_mse = results[best_name]

print("\n" + "="*45)
print(f"🏆 MEJOR MODELO SELECCIONADO: {best_name}")
print("="*45)

# Validación de control de calidad requerida
assert best_mse < 3, "El MSE debe ser inferior a 3"


# ============================================
# 9. EVALUACIÓN PROFUNDA Y MÉTRICAS DE NEGOCIO
# ============================================

y_pred = best_model.predict(X_test)

rmse = np.sqrt(best_mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {best_mse:.4f}")
print(f"RMSE (Error promedio en días): {rmse:.4f}")
print(f"MAE (Desviación absoluta media): {mae:.4f}")
print(f"R² (Varianza explicada): {r2:.4f}")

# Mostrar comparativa visual de las primeras 5 predicciones
print("\n--- Comparativa: Primeras 5 Predicciones vs Valores Reales ---")
resultados_df = pd.DataFrame({
    'Real (Días)': y_test.values[:5],
    'Predicción (Días)': y_pred[:5]
})
print(resultados_df.to_string(index=False))