import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

# 1. Cargar datos
crops = pd.read_csv("soil_measures.csv")

# Eliminar posibles espacios en blanco invisibles en las columnas
crops.columns = crops.columns.str.strip()

# 2. Separar X e y
X = crops.drop(columns=["crop"])
y = crops["crop"]

# 3. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Modelado y evaluación univariable
features = X.columns
feature_performance = {}

for feature in features:
    model = LogisticRegression(multi_class="multinomial", max_iter=1000)
    model.fit(X_train[[feature]], y_train)
    y_pred = model.predict(X_test[[feature]])

    score = f1_score(y_test, y_pred, average="weighted")
    feature_performance[feature] = score

# 5. Obtener la mejor característica y calcular promedios
best_feature = max(feature_performance, key=feature_performance.get)
best_predictive_feature = {best_feature: feature_performance[best_feature]}

mejor_variable = list(best_predictive_feature.keys())[0]
promedio_por_cultivo = (
    crops.groupby("crop")[mejor_variable].mean().sort_values(ascending=False)
)

# =========================================================
# GENERACIÓN DE GRÁFICOS
# =========================================================
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(18, 9))

# --- Gráfico 1: Evaluación por Variable (F1-Score) ---
df_eval = pd.DataFrame(
    list(feature_performance.items()), columns=["Variable", "F1_Score"]
)

barplot1 = sns.barplot(
    data=df_eval,
    x="Variable",
    y="F1_Score",
    ax=axes[0],
    palette="Blues_d",
    hue="Variable",
    legend=False,
)

# Añadir valores numéricos sobre cada barra y destacar la mejor variable
for p, var in zip(barplot1.patches, df_eval["Variable"]):
    height = p.get_height()
    barplot1.annotate(
        f"{height:.3f}",
        (p.get_x() + p.get_width() / 2.0, height),
        ha="center",
        va="center",
        xytext=(0, 8),
        textcoords="offset points",
        fontsize=10,
        fontweight="bold",
    )
    if var == mejor_variable:
        p.set_edgecolor("black")
        p.set_linewidth(2)

axes[0].set_title(
    "Rendimiento Predictivo por Variable del Suelo (F1-Score Weighted)",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
axes[0].set_xlabel("Variable del Suelo", fontsize=11)
axes[0].set_ylabel("F1-Score", fontsize=11)
axes[0].set_ylim(0, max(feature_performance.values()) * 1.25)

# --- Gráfico 2: Promedio de K (o mejor variable) por Cultivo ---
df_prom = promedio_por_cultivo.reset_index()
df_prom.columns = ["Cultivo", "Promedio"]

barplot2 = sns.barplot(
    data=df_prom,
    x="Promedio",
    y="Cultivo",
    ax=axes[1],
    palette="viridis",
    hue="Cultivo",
    legend=False,
)

# Añadir etiquetas de valor a la derecha de cada barra
for p in barplot2.patches:
    width = p.get_width()
    barplot2.annotate(
        f"{width:.1f}",
        (width, p.get_y() + p.get_height() / 2.0),
        ha="left",
        va="center",
        xytext=(5, 0),
        textcoords="offset points",
        fontsize=9,
    )

axes[1].set_title(
    f"Promedio de {mejor_variable} Requerido por Cultivo",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
axes[1].set_xlabel(f"Promedio de {mejor_variable}", fontsize=11)
axes[1].set_ylabel("Cultivo", fontsize=11)
axes[1].set_xlim(0, df_prom["Promedio"].max() * 1.15)

plt.tight_layout()
plt.show()