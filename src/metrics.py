import numpy as np
import pandas as pd

def perf_metrics(returns_m: pd.Series) -> dict:
    """Calcule CAGR, Sharpe, Calmar, vol annualisée, MDD à partir de rendements mensuels."""
    r = returns_m.dropna()
    n = len(r)
    if n == 0:
        return {"CAGR": np.nan, "sharpe_ratio": np.nan, "calmar": np.nan,
                "annual_volatility": np.nan, "max_drawdown": np.nan}
    cum = (1 + r).cumprod()
    cagr = (1 + r).prod()**(12/n) - 1
    vol_m = r.std(ddof=1)
    vol_a = vol_m * np.sqrt(12) if n > 1 else np.nan
    sharpe = (r.mean()/vol_m)*np.sqrt(12) if pd.notna(vol_m) and vol_m > 0 else np.nan
    mdd = (cum / cum.cummax() - 1).min()
    calmar = cagr / abs(mdd) if (pd.notna(mdd) and mdd < 0) else np.nan
    return {"CAGR": cagr, "sharpe_ratio": sharpe, "calmar": calmar,
            "annual_volatility": vol_a, "max_drawdown": mdd}
