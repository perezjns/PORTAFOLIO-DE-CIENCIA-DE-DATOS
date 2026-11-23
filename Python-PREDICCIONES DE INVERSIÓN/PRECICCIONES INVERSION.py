import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score

# ==============================================================================
# CONFIGURACIÓN DE ACTIVOS (Puedes añadir o quitar tickers de Yahoo Finance)
# ==============================================================================
ACTIVOS = {
    "Plata Futuro (USD/oz)": "SI=F",
    "Bitcoin (USD)": "BTC-USD",
    "Aena (EUR)": "AENA.MC",
    "Invesco Physical Gold ETC (EUR)": "SGLD.MI",
    "Xtrackers IE Physical Gold ETC (EUR)": "XGDU.DE",
    "Oro Futuro (USD/oz)": "GC=F",
    "Petróleo WTI (USD/bbl)": "CL=F",
    "Ferrovial (EUR)": "FER.MC",
    "ACS (EUR)": "ACS.MC",
    "Sacyr (EUR)": "SCYR.MC",
}

# Factores macroeconómicos y de sentimiento gratuitos desde Yahoo Finance
FACTORES_MACRO = {
    "DXY": "DX-Y.NYB",     # Índice Dólar (clave para materias primas y cripto)
    "US10Y": "^TNX",       # Bono Tesoro EE.UU. 10 años (tipos de interés)
    "VIX": "^VIX",         # Índice de volatilidad / miedo del mercado
    "TIPS": "TIP",         # ETF bonos ligados a inflación (proxy de tipos reales)
}

HORIZONTE_DIAS = 5       # 5 sesiones bursátiles = 1 semana (7 días naturales)
TIMEOUT_RED = 15         # Segundos máximos de espera por descarga
N_ARBOLES = 80           # Balance entre rapidez en Python 3.14 y estabilidad
MIN_ACIERTO_HIST = 52.0  # Umbral mínimo de acierto direccional en test (%)


def descargar_serie_cierre(ticker, period="5y"):
    """Descarga la serie de cierre de forma robusta sin quedarse colgada."""
    try:
        datos = yf.download(
            ticker,
            period=period,
            progress=False,
            auto_adjust=True,
            timeout=TIMEOUT_RED,
        )
        if datos is None or datos.empty:
            return None
        serie = datos["Close"]
        if isinstance(serie, pd.DataFrame):
            serie = serie.iloc[:, 0]
        return serie.dropna()
    except Exception as e:
        print(f"  [Aviso] Error descargando {ticker}: {e}", flush=True)
        return None


def descargar_macro(period="5y"):
    """Descarga y alinea variables macroeconómicas gratuitas."""
    print("Descargando variables macroeconómicas...", flush=True)
    df_macro = pd.DataFrame()
    for nombre, ticker in FACTORES_MACRO.items():
        print(f"  -> {nombre} ({ticker})", flush=True)
        serie = descargar_serie_cierre(ticker, period=period)
        if serie is not None and not serie.empty:
            df_macro[nombre] = serie
    if not df_macro.empty:
        df_macro = df_macro.ffill().dropna(how="all")
    return df_macro


def calcular_indicadores_tecnicos(df):
    """Calcula indicadores técnicos clásicos sobre el precio."""
    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    feat = pd.DataFrame(index=df.index)
    feat["Close"] = close

    # 1. Retornos recientes (momentum)
    feat["ret_1d"] = close.pct_change(1)
    feat["ret_5d"] = close.pct_change(5)
    feat["ret_10d"] = close.pct_change(10)
    feat["ret_20d"] = close.pct_change(20)

    # 2. Medias móviles y distancia relativa (tendencia)
    sma10 = close.rolling(10).mean()
    sma20 = close.rolling(20).mean()
    sma50 = close.rolling(50).mean()
    sma200 = close.rolling(200).mean()

    feat["dist_sma10"] = (close - sma10) / sma10
    feat["dist_sma20"] = (close - sma20) / sma20
    feat["dist_sma50"] = (close - sma50) / sma50
    feat["dist_sma200"] = (close - sma200) / sma200
    feat["cruce_20_50"] = (sma20 - sma50) / sma50

    # 3. RSI de 14 días (sobrecompra / sobreventa)
    delta = close.diff()
    ganancia = delta.clip(lower=0).rolling(14).mean()
    perdida = (-delta.clip(upper=0)).rolling(14).mean()
    rs = ganancia / (perdida + 1e-9)
    feat["RSI_14"] = 100 - (100 / (1 + rs))

    # 4. MACD (12, 26, 9)
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    feat["MACD_hist"] = (macd - signal) / close

    # 5. Bandas de Bollinger (posición relativa)
    std20 = close.rolling(20).std()
    feat["BB_pos"] = (close - sma20) / (2 * std20 + 1e-9)

    # 6. Volatilidad y ATR relativo
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    feat["ATR_pct"] = tr.rolling(14).mean() / close
    feat["volatilidad_20d"] = feat["ret_1d"].rolling(20).std()

    return feat


def preparar_dataset(ticker, df_macro, period="5y"):
    """Combina indicadores técnicos + variables macro y crea el objetivo a 7 días."""
    try:
        raw = yf.download(
            ticker,
            period=period,
            progress=False,
            auto_adjust=True,
            timeout=TIMEOUT_RED,
        )
    except Exception as e:
        print(f"  [Aviso] Error descargando {ticker}: {e}", flush=True)
        return None

    if raw is None or raw.empty or len(raw) < 260:
        return None

    df_limpio = pd.DataFrame(index=raw.index)
    for col in ["Close", "High", "Low"]:
        s = raw[col]
        if isinstance(s, pd.DataFrame):
            s = s.iloc[:, 0]
        df_limpio[col] = s
    df_limpio = df_limpio.dropna()

    if len(df_limpio) < 260:
        return None

    df = calcular_indicadores_tecnicos(df_limpio)

    # Unir factores macroeconómicos y calcular sus variaciones
    if df_macro is not None and not df_macro.empty:
        df = df.join(df_macro, how="left").ffill()
        for col in FACTORES_MACRO.keys():
            if col in df.columns:
                df[f"{col}_ret5d"] = df[col].pct_change(5)
                df[f"{col}_ret20d"] = df[col].pct_change(20)

    # Variable objetivo: retorno porcentual en las próximas 5 sesiones (7 días naturales)
    df["target_ret"] = df["Close"].shift(-HORIZONTE_DIAS) / df["Close"] - 1
    df["target_dir"] = (df["target_ret"] > 0).astype(int)

    return df


def senal_trading_7d(
    retorno_esperado,
    prob_subida,
    rsi_actual,
    atr_pct,
    precio_actual,
    acc_test,
    mae_test,
):
    """Genera orientación táctica aplicando filtros estadísticos antes de emitir señal."""
    if acc_test < MIN_ACIERTO_HIST:
        return f"ESPERAR / FILTRADO (acierto histórico {acc_test:.1f}% < {MIN_ACIERTO_HIST:.0f}%)"

    error_medio_decimal = mae_test / 100.0
    if abs(retorno_esperado) <= error_medio_decimal:
        return (
            f"ESPERAR / FILTRADO (pronóstico {retorno_esperado*100:+.2f}% dentro del error ±{mae_test:.2f}%)"
        )

    stop_dist = max(atr_pct * 1.5, 0.01)

    if prob_subida >= 58 and retorno_esperado > 0.015 and rsi_actual < 72:
        stop_precio = precio_actual * (1 - stop_dist)
        return f"COMPRAR (táctico 7d) | Stop ref.: {stop_precio:,.2f} (-{stop_dist*100:.1f}%)"

    if prob_subida <= 42 and retorno_esperado < -0.015:
        stop_precio = precio_actual * (1 + stop_dist)
        return f"VENDER / NO COMPRAR (táctico 7d) | Ref. invalidez corto: {stop_precio:,.2f} (+{stop_dist*100:.1f}%)"

    return "MANTENER / ESPERAR (señal sin ventaja clara a 7d)"


def analizar_y_predecir(nombre, ticker, df_macro):
    print(f"Analizando {nombre} ({ticker})...", flush=True)
    df = preparar_dataset(ticker, df_macro)
    if df is None:
        print(f"[!] Datos insuficientes para {nombre} ({ticker})\n", flush=True)
        return

    ultima_fila = df.iloc[[-1]].copy()
    historico = df.dropna().copy()

    if len(historico) < 100:
        print(f"[!] Histórico útil insuficiente para {nombre} ({ticker})\n", flush=True)
        return

    columnas_excluir = {"Close", "target_ret", "target_dir"}
    features = [c for c in historico.columns if c not in columnas_excluir]

    X = historico[features]
    y_ret = historico["target_ret"]
    y_dir = historico["target_dir"]

    corte = int(len(historico) * 0.80)
    X_train, X_test = X.iloc[:corte], X.iloc[corte:]
    y_ret_train, y_ret_test = y_ret.iloc[:corte], y_ret.iloc[corte:]
    y_dir_train, y_dir_test = y_dir.iloc[:corte], y_dir.iloc[corte:]

    reg = RandomForestRegressor(n_estimators=N_ARBOLES, max_depth=5, random_state=42, n_jobs=1)
    clf = RandomForestClassifier(n_estimators=N_ARBOLES, max_depth=5, random_state=42, n_jobs=1)

    reg.fit(X_train, y_ret_train)
    clf.fit(X_train, y_dir_train)

    mae_test = mean_absolute_error(y_ret_test, reg.predict(X_test)) * 100
    acc_test = accuracy_score(y_dir_test, clf.predict(X_test)) * 100

    reg.fit(X, y_ret)
    clf.fit(X, y_dir)

    X_hoy = ultima_fila[features]
    precio_actual = float(ultima_fila["Close"].iloc[0])
    retorno_esperado = float(reg.predict(X_hoy)[0])
    prob_subida = float(clf.predict_proba(X_hoy)[0][1]) * 100
    precio_estimado = precio_actual * (1 + retorno_esperado)

    vol_20d = float(ultima_fila["volatilidad_20d"].iloc[0])
    if np.isnan(vol_20d) or vol_20d <= 0:
        vol_20d = 0.015
    vol_semanal = vol_20d * np.sqrt(HORIZONTE_DIAS)
    rango_bajo = precio_estimado * (1 - vol_semanal)
    rango_alto = precio_estimado * (1 + vol_semanal)

    rsi_actual = float(ultima_fila["RSI_14"].iloc[0])
    atr_pct = float(ultima_fila["ATR_pct"].iloc[0])
    if np.isnan(atr_pct) or atr_pct <= 0:
        atr_pct = vol_20d
    fecha_dato = ultima_fila.index[-1].strftime("%Y-%m-%d")

    if prob_subida >= 58 and retorno_esperado > 0.005:
        sesgo = "ALCISTA MODERADO"
    elif prob_subida <= 42 and retorno_esperado < -0.005:
        sesgo = "BAJISTA MODERADO"
    else:
        sesgo = "NEUTRAL / LATERAL"

    accion_tr = senal_trading_7d(
        retorno_esperado,
        prob_subida,
        rsi_actual,
        atr_pct,
        precio_actual,
        acc_test,
        mae_test,
    )

    print(f"Activo: {nombre} ({ticker}) | Último cierre: {fecha_dato}", flush=True)
    print(f"  Precio actual:        {precio_actual:,.2f}", flush=True)
    print(f"  Pronóstico 7 días:    {precio_estimado:,.2f} ({retorno_esperado*100:+.2f} %)", flush=True)
    print(f"  Rango probable (68%): {rango_bajo:,.2f}  <--->  {rango_alto:,.2f}", flush=True)
    print(f"  Prob. de subida:      {prob_subida:.1f} %  |  RSI(14): {rsi_actual:.1f}  |  Sesgo: {sesgo}", flush=True)
    print(f"  Fiabilidad histórica: Acierto dirección {acc_test:.1f}% | Error medio ±{mae_test:.2f}%", flush=True)
    print(f"  Acción trading (7d):  {accion_tr}", flush=True)
    print("-" * 78, flush=True)


def main():
    hoy = datetime.now().strftime("%Y-%m-%d %H:%M")
    objetivo = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    print("=" * 78, flush=True)
    print(f"MODELO CUANTITATIVO TÉCNICO + MACRO (HORIZONTE: 7 DÍAS -> {objetivo})", flush=True)
    print(f"Ejecutado el: {hoy}", flush=True)
    print("=" * 78, flush=True)

    df_macro = descargar_macro(period="5y")
    if not df_macro.empty:
        ult_macro = df_macro.iloc[-1]
        print(
            f"Contexto Macro Actual -> Dólar (DXY): {ult_macro.get('DXY', np.nan):.2f} | "
            f"Bono EE.UU. 10Y: {ult_macro.get('US10Y', np.nan):.2f}% | "
            f"VIX (Miedo): {ult_macro.get('VIX', np.nan):.2f}",
            flush=True,
        )
        print("=" * 78, flush=True)

    for nombre, ticker in ACTIVOS.items():
        analizar_y_predecir(nombre, ticker, df_macro)

    print("Proceso completado.", flush=True)


if __name__ == "__main__":
    main()