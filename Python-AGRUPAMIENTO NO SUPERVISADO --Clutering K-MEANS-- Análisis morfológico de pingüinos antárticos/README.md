# Agrupamiento de Especies de Pingüinos Antárticos (K-Means Clustering)

Proyecto de ciencia de datos desarrollado para aplicar técnicas de aprendizaje automático no supervisado (**K-Means**) con el fin de identificar y agrupar poblaciones de pingüinos en la Antártida a partir de características morfológicas y biométricas.

## 📌 Origen de los Datos
* **Autora y Fuente:** Dr. Kristen Gorman y la *Palmer Station, Antarctica LTER*, miembro de la *Long Term Ecological Research Network*.
* **Ilustraciones de referencia:** @allison_horst ([GitHub Repository](https://github.com/allisonhorst/penguins)).

---

## 📊 Descripción del Conjunto de Datos (`penguins.csv`)
El conjunto de datos consta de registros limpios y 5 columnas principales:
* **`culmen_length_mm`**: Longitud del culmen (pico) en milímetros.
* **`culmen_depth_mm`**: Profundidad del culmen en milímetros.
* **`flipper_length_mm`**: Longitud de la aleta en milímetros.
* **`body_mass_g`**: Masa corporal en gramos.
* **`sex`**: Sexo biológico del pingüino (`MALE`, `FEMALE`).

---

## ⚙️ Metodología y Enfoques Analíticos Detallados

El análisis no supervisado se estructura en dos enfoques complementarios que permiten examinar tanto el impacto de las características demográficas como la separación morfológica pura de las especies:

1. **Modelo A (Con Variable de Sexo / K Óptimo):**
   * **Transformación de Variables:** Incorpora la variable cualitativa `sex` convirtiéndola en variables indicadoras binarias (*one-hot encoding*) mediante codificación de características categóricas.
   * **Estandarización:** Se aplica un escalador estándar para normalizar todas las magnitudes numéricas y binarias, asegurando que ninguna escala domine sobre las demás en el cálculo de distancias euclidianas del algoritmo.
   * **Evaluación de Clústeres:** Mediante el análisis de inercia (Método del Codo) y el Coeficiente de Silueta, este enfoque identifica que un valor óptimo de $k$ permite capturar de manera sobresaliente tanto las diferencias anatómicas entre especies como la variabilidad por dimorfismo sexual.

2. **Modelo B (Excluyendo Sexo / Enfoque Biológico Estricto de Especies):**
   * **Aislamiento Biométrico:** Filtra exclusivamente las 4 variables cuantitativas puras (`culmen_length_mm`, `culmen_depth_mm`, `flipper_length_mm`, `body_mass_g`) para evitar sesgos por género.
   * **Definición de K:** Se fija de forma supervisada $k = 3$ para alinear estrictamente el agrupamiento matemático con las tres especies nativas y conocidas de la región antártica estudiada: **Adelie**, **Chinstrap** y **Gentoo**.
   * **Validación Analítica (`stat_penguins`):** Agrupa el conjunto de datos resultante por clústeres para calcular las medias de cada variable física, generando el DataFrame resumido **`stat_penguins`** que valida la coherencia biológica de las agrupaciones generadas.

---

¿Te gustaría profundizar en la interpretación de los centroides o visualizar las métricas de evaluación de silueta de alguno de estos modelos?
