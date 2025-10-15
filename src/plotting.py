import matplotlib.pyplot as plt
import pandas as pd

def bar_cagr_compare(df_mom: pd.DataFrame, df_spy: pd.DataFrame, title="CAGR — Momentum vs SPY"):
    cmp = pd.concat([
        df_mom["CAGR"].rename("Momentum"),
        df_spy["CAGR"].rename("SPY")
    ], axis=1)
    ax = cmp.plot(kind="bar", edgecolor="black")
    ax.set_title(title)
    ax.set_ylabel("CAGR")
    ax.set_xlabel("Bucket")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    return ax

def bar_sharpe_compare(df_mom: pd.DataFrame, df_spy: pd.DataFrame, title="Sharpe — Momentum vs SPY"):
    cmp = pd.concat([
        df_mom["sharpe_ratio"].rename("Momentum"),
        df_spy["sharpe_ratio"].rename("SPY")
    ], axis=1)
    ax = cmp.plot(kind="bar", edgecolor="black")
    ax.set_title(title)
    ax.set_ylabel("Sharpe (annualisé)")
    ax.set_xlabel("Bucket")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    return ax
