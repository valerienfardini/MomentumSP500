import numpy as np
import pandas as pd
from .metrics import perf_metrics

def backtest_with_horizon(prices: pd.DataFrame, returns: pd.DataFrame,
                          lookback: int, quantile: float):
    """
    Cross-sectional momentum long-only, égal-pondéré.
    prices/returns: DataFrames (dates en index, tickers en colonnes)
    """
    mom = prices.pct_change(lookback).shift(1)
    thr = mom.quantile(quantile, axis=1)
    sel = mom.ge(thr, axis=0)  # True si au-dessus du seuil

    denom = sel.sum(axis=1).clip(lower=1).astype(float)
    w = sel.div(denom, axis=0)  # poids égal-pondérés
    port = (w * returns).sum(axis=1).dropna()

    metrics = perf_metrics(port)
    out = {"quantile": quantile, "lookback": lookback, **metrics}
    cum = (1 + port).cumprod()
    return port, cum, out
