import statsmodels.api as sm
import numpy as np
import pandas as pd

def build_bucket_return(prices: pd.DataFrame, returns: pd.DataFrame, lookback: int, quantile: float) -> pd.Series:
    mom = prices.pct_change(lookback).shift(1)
    thr = mom.quantile(quantile, axis=1)
    sel = mom.ge(thr, axis=0)
    w = sel.div(sel.sum(axis=1).clip(lower=1).astype(float), axis=0)
    port = (w * returns).sum(axis=1)
    return port.dropna()

def build_final_portfolio(prices: pd.DataFrame, returns: pd.DataFrame, selection: pd.DataFrame) -> pd.Series:
    parts = []
    sel = selection.reset_index()
    for _, row in sel.iterrows():
        r_bkt = build_bucket_return(prices, returns, int(row["lookback"]), float(row["quantile"]))
        parts.append(r_bkt.rename(row["Bucket"]))
    ret_port = pd.concat(parts, axis=1).mean(axis=1)
    return ret_port.dropna()

def ols_alpha_beta_monthly(port: pd.Series, bench: pd.Series, rf_annual: float = 0.0):
    df = pd.concat([port.rename("p"), bench.rename("b")], axis=1).dropna()
    if df.empty:
        return None
    rf_m = (1 + rf_annual)**(1/12) - 1
    y = df["p"] - rf_m
    x = df["b"] - rf_m
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    alpha_m  = model.params["const"]
    beta     = model.params["b"]
    alpha_ann = alpha_m * 12
    return model, alpha_ann, beta
