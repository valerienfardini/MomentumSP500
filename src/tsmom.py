import numpy as np
import pandas as pd
from .metrics import perf_metrics

def mom_spy(spy_df: pd.DataFrame, lookback: int, price_col: str = "SPY"):
    """TSMOM sur SPY mensuel : position 1 si tendance L>0 (décalée), sinon 0."""
    px = spy_df[price_col].sort_index()
    ret = px.pct_change()
    sig = px.pct_change(lookback).shift(1)
    pos = (sig > 0).astype(float)
    port = (pos * ret).dropna()
    cum = (1 + port).cumprod()
    return port, cum, {"lookback": lookback, **perf_metrics(port)}

def buy_hold_metrics(spy_df: pd.DataFrame, price_col: str = "SPY"):
    ret = spy_df[price_col].sort_index().pct_change().dropna()
    return perf_metrics(ret)
