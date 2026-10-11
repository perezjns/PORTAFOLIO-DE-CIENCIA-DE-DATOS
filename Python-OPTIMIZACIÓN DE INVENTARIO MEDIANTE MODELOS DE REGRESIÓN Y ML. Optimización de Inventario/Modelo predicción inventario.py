
# ============================================
# 1. IMPORTAR LAS LIBRERÍAS
# ============================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# ============================================
# 2. LEER EL ARCHIVO CSV
# ============================================

rental_df = pd.read_csv("rental_info.csv")


# ============================================
# 3. CREAR LA VARIABLE OBJETIVO
# ============================================

rental_df["rental_date"] = pd.to_datetime(
    rental_df["rental_date"]
)

rental_df["return_date"] = pd.to_datetime(
    rental_df["return_date"]
)

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
# 5. DEFINIR LAS VARIABLES PREDICTORAS (X)
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


# ============================================
# 6. DEFINIR LA VARIABLE OBJETIVO (y)
# ============================================

y = rental_df["rental_length_days"]


# ============================================
# 7. DIVIDIR EN ENTRENAMIENTO Y PRUEBA
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=9
)


# ============================================
# 8. COMPARAR DIFERENTES MODELOS
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

for name, model in models.items():
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    results[name] = mse

    print(f"{name}: MSE = {mse:.4f}")


# ============================================
# 9. SELECCIONAR EL MEJOR MODELO
# ============================================

best_name = min(results, key=results.get)

best_model = models[best_name]

best_mse = results[best_name]

print("\nMejor modelo:", best_name)
print("Mejor MSE:", round(best_mse, 4))

assert best_mse < 3, "El MSE debe ser inferior a 3"