# 📊 Estudio de Caso: Análisis de Cancelación de Clientes (*Customer Churn*) en Power BI

## 📌 **Descripción del Proyecto**

> 🎯 **Objetivo Principal:** Reducir la tasa de abandono (*churn*) en la empresa de telecomunicaciones **Databel** mediante el análisis predictivo y descriptivo en **Power BI**.

Para las empresas basadas en suscripciones, la retención de clientes es una prioridad estratégica. En este proyecto investigamos los factores clave detrás de la cancelación de contratos mediante la creación de **medidas DAX**, **columnas calculadas** y un **dashboard interactivo** de alta fidelidad.

---

## 🔍 **Fase 1: Análisis Exploratorio de Datos (EDA)**

* **🛡️ Verificación de Integridad:** Se confirmó la validez del dataset evaluando la duplicidad de registros mediante las medidas:
  * `Number of Customers = COUNT('Databel - Data'[Customer ID])`
  * `Number of Unique Customers = DISTINCTCOUNT('Databel - Data'[Customer ID])`
* **📉 Binarización y Tasa de Churn:** Se transformó el campo `Churn Label` ("Yes"/"No") a una variable binomial `Churned = IF('Databel - Data'[Churn Label] = "Yes", 1, 0)` para calcular la tasa global mediante:
  * `Churn_rate = DIVIDE([Number of Churned Customers], [Number of Customers])`
* **⚠️ Top 3 Razones de Cancelación:**
  1. 🥊 **Competencia:** Mejores ofertas comerciales.
  2. 📱 **Tecnología:** Dispositivos y hardware de mayor gama en competidores.
  3. 🎧 **Atención al Cliente:** Experiencias insatisfactorias con el soporte técnico.
* **🏷️ Categorías Prevalentes:** La categoría con mayor impacto fue **Competitor** (agrupando factores de precio y oferta rival).
* **🗺️ Análisis Geográfico:** Mediante cartografía interactiva se identificó a **California (CA)** como el estado con mayor tasa de churn (**63.24%**).

---

## 🎯 **Fase 2: Investigación de Patrones y Hallazgos Clave**

* **👴 Impacto Demográfico:** Se segmentó la población por edad usando la columna:
  * `Demographics = IF('Databel - Data'[Senior] = "Yes", "Senior", IF('Databel - Data'[Under 30] = "Yes", "Under 30", "Other"))`
  * 🚨 **Hallazgo:** La tasa de churn en adultos mayores (*Senior Citizens*) escala al **38.46%** (muy por encima del promedio).
* **📈 Correlación por Rangos Etarios:** El análisis por agrupaciones de edad (*age bins*) confirmó que la tasa de cancelación se incrementa de forma directamente proporcional a la edad del cliente.
* **👥 Planes Grupales vs. Individuales:** Los clientes contratados en grupos de 2 o más personas disfrutan de una factura mensual (`Monthly Charge`) sustancialmente menor y registran menor probabilidad de abandono.
* **📜 Tipos de Contrato:** Se simplificó la modalidad contractual con la fórmula:
  * `Contract Category = SWITCH('Databel - Data'[Contract Type], "One Year", "Yearly", "Two Year", "Yearly", "Monthly")`
  * ⚠️ **Hallazgo:** Los contratos **mensuales** presentan una fuga de clientes drásticamente superior a los planes **anuales**.
* **💡 La Paradoja de los Datos Ilimitados:** 
  * Se creó la segmentación de consumo: `Grouped Consumption = IF('Databel - Data'[Avg Monthly GB Download] < 5, "Light Data User", IF('Databel - Data'[Avg Monthly GB Download] > 10, "Heavy User", "Medium User"))`.
  * 🚨 **Hallazgo inesperado:** Los usuarios con bajo consumo de datos (*Light Data Users*) que pagan un **plan ilimitado** muestran la mayor tasa de cancelación.
* **🌐 Consumo Internacional:** Se detectó un riesgo extremo de fuga en clientes que pagan una tarifa plana internacional pero **no realizan llamadas internacionales**.

---

## 💡 **Recomendación Estratégica de Negocio**

> 📢 **Acción Preventiva:** Contactar de forma proactiva a los clientes con tarifa plana internacional que no realizan llamadas internacionales y **ofrecerles una optimización de tarifa (*downgrade*)** antes de que cancelen el servicio por percepción de sobrecosto.
