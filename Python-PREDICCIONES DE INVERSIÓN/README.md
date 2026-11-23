# Modelo Cuantitativo Técnico + Macro (Horizonte 7 Días)

Script cuantitativo en Python (`PREDICCIONES INVERSION.py`) que combina **ingeniería de características técnicas**, **variables macroeconómicas globales** y **aprendizaje automático supervisado (*Random Forest*)** sobre datos históricos gratuitos de Yahoo Finance para proyectar escenarios a **5 sesiones bursátiles (7 días naturales)** y generar filtros tácticos de *trading*.

---

## 1. Arquitectura y Flujo de Ejecución

Cada vez que ejecutas el script, se realiza el siguiente proceso secuencial para cada activo configurado:

1. **Descarga macroeconómica (`descargar_macro`):** Obtiene 5 años de cierres diarios ajustados de 4 indicadores macro globales (`DX-Y.NYB`, `^TNX`, `^VIX`, `TIP`) con `timeout=15` segundos para evitar bloqueos de red.
2. **Descarga del activo (`preparar_dataset`):** Descarga 5 años de precios diarios ajustados (`Close`, `High`, `Low`) con `auto_adjust=True` (corrigiendo dividendos y *splits*) y verifica un mínimo de 260 sesiones válidas.
3. **Cálculo de variables técnicas (`calcular_indicadores_tecnicos`):** Transforma los precios diarios en **14 indicadores técnicos adimensionales** que miden momentum, tendencia, sobrecompra/sobreventa, impulso y volatilidad.
4. **Alineación macroeconómica:** Cruza por fecha las series macro con el calendario de cada activo aplicando `ffill()` (arrastre del último valor conocido en festivos o fines de semana de Bitcoin, sin fuga de datos futuros) y calcula sus variaciones porcentuales a 5 y 20 sesiones (**12 variables macro**).
5. **Etiquetado futuro (`HORIZONTE_DIAS = 5`):** Asocia cada fila histórica *t* con el retorno porcentual real ocurrido 5 sesiones después:
   - `target_ret = (Close[t+5] / Close[t]) - 1`
   - `target_dir = 1` si `target_ret > 0`, en caso contrario `0`.
6. **Validación temporal *Out-of-Sample* (80 % / 20 %):** Entrena los modelos sobre el **80 % más antiguo** (~4 años) y los evalúa sobre el **20 % más reciente** (~1 año nunca visto) para medir el porcentaje real de acierto direccional (`accuracy_score`) y el error medio absoluto (`MAE`).
7. **Reentrenamiento final y pronóstico:** Reentrena ambos bosques aleatorios con el **100 % de los datos etiquetados** hasta el último cierre disponible y predice sobre el vector actual (`X_hoy`).
8. **Reglas de decisión táctica (`senal_trading_7d`):** Aplica filtros de calidad estadística (`acierto ≥ 52 %` y `|retorno_esperado| > MAE`) antes de recomendar `COMPRAR`, `VENDER / NO COMPRAR` o `ESPERAR`, calculando un *stop loss* dinámico basado en `1,5 × ATR`.

---

## 2. Desglose de las 26 Variables Predictoras (`features`)

### A. Indicadores Técnicos (14 variables)

| Variable | Fórmula Matemática | Qué mide y cómo se interpreta |
| :--- | :--- | :--- |
| **`ret_1d`** | `(C_t - C_{t-1}) / C_{t-1}` | Retorno porcentual de la última sesión (impulso inmediato). |
| **`ret_5d`** | `(C_t - C_{t-5}) / C_{t-5}` | Retorno acumulado en las últimas 5 sesiones (1 semana). |
| **`ret_10d`** | `(C_t - C_{t-10}) / C_{t-10}` | Retorno acumulado en las últimas 10 sesiones (~2 semanas). |
| **`ret_20d`** | `(C_t - C_{t-20}) / C_{t-20}` | Retorno acumulado en las últimas 20 sesiones (~1 mes bursátil). |
| **`dist_sma10`** | `(C_t - SMA_10) / SMA_10` | Distancia relativa (%) respecto a la media móvil simple de 10 días. |
| **`dist_sma20`** | `(C_t - SMA_20) / SMA_20` | Distancia relativa (%) respecto a la media mensual de 20 días. |
| **`dist_sma50`** | `(C_t - SMA_50) / SMA_50` | Distancia relativa (%) respecto a la media intermedia de 50 días. |
| **`dist_sma200`** | `(C_t - SMA_200) / SMA_200` | Distancia relativa (%) respecto a la media de largo plazo de 200 días. |
| **`cruce_20_50`** | `(SMA_20 - SMA_50) / SMA_50` | Diferencial porcentual entre la media rápida (20d) y la intermedia (50d). |
| **`RSI_14`** | `100 - [100 / (1 + Ganancia_14 / Pérdida_14)]` | Oscilador (0–100) de fuerza relativa. `< 30` indica sobreventa; `> 70` sobrecompra. |
| **`MACD_hist`** | `(EMA_12 - EMA_26 - EMA_9(MACD)) / C_t` | Histograma MACD normalizado por el precio; mide aceleración de tendencia. |
| **`BB_pos`** | `(C_t - SMA_20) / (2 * std_20)` | Posición dentro de las Bandas de Bollinger (`+1` banda superior, `-1` banda inferior). |
| **`ATR_pct`** | `Media_14(TR_t) / C_t` | Rango Verdadero Medio de 14 días en %; mide la amplitud diaria del activo. |
| **`volatilidad_20d`** | `DesvTip_20(ret_1d)` | Desviación estándar de los retornos diarios de las últimas 20 sesiones. |

### B. Variables Macroeconómicas (12 variables)

| Factor Base (Ticker) | Variables Generadas | Significado Financiero |
| :--- | :--- | :--- |
| **Índice Dólar (`DX-Y.NYB`)** | `DXY`, `DXY_ret5d`, `DXY_ret20d` | Fortaleza del USD. Un dólar alcista presiona a la baja a materias primas (oro, plata, petróleo) y Bitcoin. |
| **Bono EE. UU. 10Y (`^TNX`)** | `US10Y`, `US10Y_ret5d`, `US10Y_ret20d` | Tipo de interés libre de riesgo global. Subidas encarecen la deuda de infraestructuras y penalizan activos sin cupón. |
| **Índice de Miedo (`^VIX`)** | `VIX`, `VIX_ret5d`, `VIX_ret20d` | Volatilidad implícita del S&P 500. Picos altos indican estrés financiero y ventas por liquidez. |
| **Bonos Inflación (`TIP`)** | `TIPS`, `TIPS_ret5d`, `TIPS_ret20d` | Proxy inverso de los tipos de interés reales; mantiene fuerte correlación positiva con el oro y la plata. |

---

## 3. Modelos de Machine Learning y Cálculos de Salida

El script utiliza dos modelos de `scikit-learn` configurados con **`n_estimators=80`**, **`max_depth=5`** (para evitar sobreajuste), **`random_state=42`** y **`n_jobs=1`** (para máxima estabilidad en Windows):

1. **`RandomForestRegressor` (Pronóstico de precio):**
   - Promedia la estimación de 80 árboles de regresión para obtener `retorno_esperado`.
   - **Precio proyectado:** `precio_estimado = precio_actual × (1 + retorno_esperado)`.
2. **`RandomForestClassifier` (Probabilidad direccional):**
   - Calcula la proporción media de votos positivos en los 80 árboles (`predict_proba`) para obtener `Prob. de subida` (`0 % – 100 %`).
3. **Rango Probable (68 %):**
   - Proyecta la volatilidad diaria de 20 días a 5 sesiones (`vol_semanal = volatilidad_20d × √5`) y construye el intervalo `[precio_estimado × (1 - vol_semanal), precio_estimado × (1 + vol_semanal)]`, equivalente a ±1 desviación típica semanal.

---

## 4. Reglas de Decisión Táctica (`Acción trading (7d)`)

El programa evalúa las siguientes condiciones en orden estricto:

1. **Filtro de Fiabilidad Histórica:** Si `acierto_test < 52.0 %` → **`ESPERAR / FILTRADO (acierto histórico < 52%)`**.
2. **Filtro de Ruido Estadístico:** Si `|retorno_esperado| <= (mae_test / 100)` → **`ESPERAR / FILTRADO (pronóstico dentro del error ±MAE)`**.
3. **Señal de Compra:** Si `prob_subida >= 58 %`, `retorno_esperado > +1.5 %` y `RSI_14 < 72` → **`COMPRAR (táctico 7d)`** con *stop loss* en `precio_actual × (1 - max(ATR_pct × 1.5, 0.01))`.
4. **Señal de Venta:** Si `prob_subida <= 42 %` y `retorno_esperado < -1.5 %` → **`VENDER / NO COMPRAR (táctico 7d)`** con nivel de invalidez alcista en `precio_actual × (1 + max(ATR_pct × 1.5, 0.01))`.
5. **Zona Neutra:** En cualquier otro caso → **`MANTENER / ESPERAR (señal sin ventaja clara a 7d)`**.

---

## 5. Instalación y Ejecución

### Requisitos
```bash
pip install yfinance pandas numpy scikit-learn
```

### Ejecución
```bash
python -u "PREDICCIONES INVERSION.py"
```

### Activos incluidos por defecto (`ACTIVOS`)
* **Materias Primas y Cripto:** Plata Futuro (`SI=F`), Oro Futuro (`GC=F`), Petróleo WTI (`CL=F`), Bitcoin (`BTC-USD`).
* **ETCs de Oro Físico (EUR):** Invesco Physical Gold (`SGLD.MI`), Xtrackers IE Physical Gold (`XGDU.DE`).
* **Acciones Españolas (EUR):** Aena (`AENA.MC`), Ferrovial (`FER.MC`), ACS (`ACS.MC`), Sacyr (`SCYR.MC`).

---

## 6. Ejemplo de Salida Comentada

```text
Activo: Sacyr (EUR) (SCYR.MC) | Último cierre: 2026-11-20
  Precio actual:        4.06
  Pronóstico 7 días:    4.15 (+2.34 %)
  Rango probable (68%): 4.01  <--->  4.29
  Prob. de subida:      66.5 %  |  RSI(14): 43.3  |  Sesgo: ALCISTA MODERADO
  Fiabilidad histórica: Acierto dirección 48.4% | Error medio ±3.08%
  Acción trading (7d):  ESPERAR / FILTRADO (acierto histórico 48.4% < 52%)
```

En este ejemplo, aunque el regresor estima un rebote a `4,15 €` (`+2,34 %`) con `66,5 %` de probabilidad direccional, el sistema **filtra la entrada** porque en el último año de prueba el acierto direccional fue del `48,4 %` (inferior al umbral mínimo del `52 %`) y el retorno proyectado (`+2,34 %`) es menor que el error medio histórico (`±3,08 %`).

---

## Aviso Legal
Software desarrollado con fines exclusivamente educativos, estadísticos y de investigación cuantitativa. No constituye asesoramiento financiero ni recomendación de compra o venta. Opera siempre aplicando gestión del riesgo adecuada y verificando comisiones y fiscalidad aplicable.
