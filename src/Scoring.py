import numpy as np
import pandas as pd

def prep_percentiles(df : pd.DataFrame):
    out = df.copy()
    out["CAGR_pct"] = out["CAGR"].rank(pct=True, ascending=True)
    out["sharpe_ratio_pct"] = out["sharpe_ratio"].rank(pct=True, ascending=True)
    out["calmar_pct"] = out["calmar"].rank(pct=True, ascending=True)
    out["annual_volatility_pct"] = 1 - out["annual_volatility"].rank(pct=True, ascending=True)
    mdd_mag = out["max_drawdown"].abs()
    out["max_drawdown_pct"] = 1 - mdd_mag.rank(pct=True, ascending=True)
    out = out.drop(columns=["CAGR", "sharpe_ratio","calmar","annual_volatility", "max_drawdown"])
    return out

def pareto_front(df_pct: pd.DataFrame, cols_pct) -> pd.DataFrame:
    Z = df_pct[cols_pct].to_numpy()
    n = len(df_pct)
    is_dom = np.zeros(n, dtype=bool)
    for i in range(n):
        dominates_i = (Z >= Z[i]).all(axis=1) & (Z > Z[i]).any(axis=1)
        if dominates_i.any():
            is_dom[i] = True
    return df_pct.loc[~is_dom].copy()
def add_composite_per_bucket(df: pd.DataFrame, weights_map: dict,  cols_pct: list) -> pd.DataFrame:
    s = df.copy()
    s["Composite Score"] = np.nan

    for bkt, part in s.groupby(level=0, sort=False, observed=True):
        wdict = weights_map[bkt]
        cols = [c for c in cols_pct if c in part.columns and c in wdict]
        X = part[cols].to_numpy(dtype=float)
        W = np.array([wdict[c] for c in cols], dtype=float)
        scores = X @ W
        s.loc[part.index, "Composite Score"] = scores

    return s

def select_best_per_bucket(df: pd.DataFrame):
    idx = df.groupby(level="Bucket", observed=True)["Composite Score"].idxmax()
    best = df.loc[idx]
    best = best.drop(columns = cols_pct)
    return best 
