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

## 🔬 Profundización Analítica: Centroides y Métricas de Evaluación

### 1. Interpretación de Centroides en el Modelo B ($k = 3$ / Especies Biológicas)
Al fijar $k = 3$ y aislar las variables biométricas, el algoritmo K-Means agrupa a las observaciones buscando los centros de gravedad (centroides) en un espacio de 4 dimensiones. El DataFrame resultante **`stat_penguins`** resume las medias físicas de cada clúster, permitiendo trazar un perfil biológico claro:
* **Clúster de mayor envergadura (Gentoo):** Representado por centroides con los valores más altos en longitud de aleta (`flipper_length_mm`) y masa corporal (`body_mass_g`), diferenciándose claramente por su gran tamaño y aletas alargadas.
* **Clúster de pico pronunciado y alargado (Chinstrap):** Se caracteriza por presentar los valores máximos en la longitud del culmen (`culmen_length_mm`) en proporción a su cuerpo, junto con una profundidad de pico intermedia.
* **Clúster compacto y de menor tamaño (Adelie):** Agrupa a los pingüinos con las menores dimensiones corporales y de aletas, destacando por una profundidad de culmen (`culmen_depth_mm`) proporcionalmente alta respecto a su longitud corta de pico.

### 2. Evaluación de Rendimiento y Coeficiente de Silueta
Para validar qué tan bien definidos y separados están los clústeres, se utiliza el **Coeficiente de Silueta** (cuyo valor oscila entre -1 y +1):
* **Modelo A ($k = 4$ con Sexo):** Al incorporar el dimorfismo sexual, las especies se subdividen sutilmente (por ejemplo, machos y hembras de una misma especie pueden formar subgrupos o desplazar los límites del clúster). El coeficiente de silueta en este modelo ayuda a comprobar si los 4 grupos mantienen una cohesión interna aceptable sin solapamientos excesivos, reflejando cómo el género influye en la variabilidad morfológica.
* **Modelo B ($k = 3$ sin Sexo):** Al eliminar el factor sexual, las siluetas tienden a reflejar de forma más pura la separación natural entre las tres especies de la Estación Palmer. Un puntaje de silueta cercano o superior al promedio general indica que los centroides representan fronteras naturales bien delimitadas entre **Adelie**, **Chinstrap** y **Gentoo**.
