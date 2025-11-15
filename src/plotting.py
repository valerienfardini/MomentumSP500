import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt

# Compute log-returns and plot the cumulative performance of the strategy
rets = np.log(final_df2/final_df2.shift(1))
rets.cumsum().apply(np.exp).plot(figsize=(30,30))

# Plot a comparison of the strategy vs. the S&P 500 using CAGR and Sharpe ratio
mom = metrics_df2["CAGR_pct"]
spy = metrics_spy["CAGR_pct"]
mom_s = metrics_df2["sharpe_ratio_pct"]
spy_s = metrics_spy["sharpe_ratio_pct"]
common_all = mom.index.intersection(spy.index).intersection(mom_s.index).intersection(spy_s.index)

df_plot   = pd.DataFrame({"Momentum": mom.loc[common_all],   "SPY": spy.loc[common_all]})
df_plot_s = pd.DataFrame({"Momentum": mom_s.loc[common_all], "SPY": spy_s.loc[common_all]})

fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharex=True)

(df_plot * 100).plot(kind="bar", edgecolor="black", ax=axes[0], legend=True)
axes[0].set_title("CAGR Momentum vs SPY par bucket")
axes[0].set_ylabel("CAGR (%)")
axes[0].set_xlabel("Bucket")
axes[0].grid(axis="y", linestyle="--", alpha=0.7)
axes[0].tick_params(axis="x", rotation=0)

df_plot_s.plot(kind="bar", edgecolor="black", ax=axes[1], legend=True)
axes[1].set_title("Sharpe ratio Momentum vs SPY par bucket")
axes[1].set_ylabel("Sharpe ratio")
axes[1].set_xlabel("Bucket")
axes[1].grid(axis="y", linestyle="--", alpha=0.7)
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.show()
