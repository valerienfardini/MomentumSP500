import numpy as np
import pandas as pd

def prep_percentiles(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["CAGR_pct"]             = out["CAGR"].rank(pct=True, ascending=True)
    out["sharpe_ratio_pct"]     = out["sharpe_ratio"].rank(pct=True, ascending=True)
    out["calmar_pct"]           = out["calmar"].rank(pct=True, ascending=True)
    out["annual_volatility_pct"]= 1 - out["annual_volatility"].rank(pct=True, ascending=True)
    out["max_drawdown_pct"]     = 1 - out["max_drawdown"].abs().rank(pct=True, ascending=True)
    return out

def add_composite_score(df_pct: pd.DataFrame, global_weights: dict,
                        cols_pct=None, score_col="CompositeScore") -> pd.DataFrame:
    if cols_pct is None:
        cols_pct = ["CAGR_pct","sharpe_ratio_pct","calmar_pct","annual_volatility_pct","max_drawdown_pct"]
    cols = [c for c in cols_pct if c in df_pct.columns and c in global_weights]
    if not cols:
        raise ValueError("Aucune colonne percentile utilisable.")
    X = df_pct[cols].to_numpy(dtype=float)
    W = np.array([global_weights[c] for c in cols], dtype=float)
    out = df_pct.copy()
    out[score_col] = X @ W
    return out

def add_bucket_column(df: pd.DataFrame, buckets: dict) -> pd.DataFrame:
    L2B = {L: b for b, Ls in buckets.items() for L in Ls}
    out = df.copy()
    out["Bucket"] = out["lookback"].map(L2B)
    return out

def select_best_per_bucket(df_scored: pd.DataFrame, score_col="CompositeScore"):
    idx = df_scored.groupby("Bucket", observed=True)[score_col].idxmax()
    return df_scored.loc[idx].sort_values("Bucket")
