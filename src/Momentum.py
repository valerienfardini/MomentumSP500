import numpy as np
import pandas as pd

returns = final_df2.pct_change() 

def backtest_with_horizon(prices: pd.DataFrame, returns: pd.DataFrame, lookback: int, quantile: float): 
    mom = prices.pct_change(lookback).shift(1) 
    thr = mom.quantile(quantile, axis=1) 
    sel = mom.ge(thr, axis=0) 
    denom = sel.sum(axis=1).clip(lower=1).astype(float) 
    w = sel.div(denom, axis=0) 
    port = (w * returns).sum(axis=1).dropna() 
    n = len(port) 
    cum = (1 + port).cumprod() 
    cagr = (1 + port).prod()**(12/n) - 1 if n else np.nan 
    vol_m = port.std(ddof=1) 
    vol_a = vol_m * np.sqrt(12) if n > 1 else np.nan 
    sharpe = (port.mean()/vol_m)*np.sqrt(12) if vol_m and vol_m > 0 else np.nan 
    mdd = (cum / cum.cummax() - 1).min() 
    calmar = cagr / abs(mdd) if pd.notna(mdd) and mdd < 0 else np.nan 
    return port, cum, { "quantile": quantile, 
                       "lookback": lookback, 
                       "CAGR": cagr, 
                       "sharpe_ratio": sharpe, 
                       "calmar": calmar, 
                       "annual_volatility": vol_a, 
                       "max_drawdown": mdd }
