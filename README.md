# Momentum cross-sectionnel sur S&P 500 (long-only, mensuel)

[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Reproducible](https://img.shields.io/badge/Reproducible-Yes-success)]()

> Stratégie momentum cross-sectionnel long-only sur univers actions US, rééquilibrage mensuel avec latence d’un mois.  
> Sélection des couples \((L,q)\) via frontière de Pareto et score composite (CAGR, Sharpe, Calmar, Vol, MDD).  
> Long terme (L=60, q=0.50) = meilleur compromis rendement/risque ; Très long (L=120, q=0.50) = profil défensif (β & MDD bas).

---

## Résultats

| Bucket | (L, q) | CAGR | Vol | Sharpe | MDD | Calmar | AlphaAnn | Beta |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Court terme | (3, 0.70) | 17.0% | 15.82% | 1.08 | −44.6% | 0.38 | +6.6% | 0.94 |
| Moyen terme | (12, 0.30) | 15.29% | 14.61%| 1.05 | −41.1% | 0.37 | +4.9% | 0.94 |
| **Long terme** | **(60, 0.50)** | **15.26%** | 13.57% | **1.13** | **−29.8%** | **0.52** | **+9.7%** | **0.75** |
| Très long terme | (120, 0.50) | 9.32% | 12.08% | 0.80 | −26.90% | 0.35 | +3.3% | 0.57 |
| **SPY (bench)** | — | 10.71% | 14.82% | 0.76 | −50.80% | 0.21 | n/a | 1.00 |

> Lecture : les versions Court/Moyen/Long surperforment le SPY en **CAGR & Sharpe**.  
> La version Très long est défensive (β, MDD bas) mais lag en bull market prolongé ; **α annuel positif**.

---

## Méthodologie
- **Signal** : performance cumulée sur **L mois** (momentum).   
- **Sélection** : top \(1-q\) des titres (ex. \(q=0.50\) ⇒ top ~50 %) en pondération égale.  
- **Latence** : calcul du signal à \(t-1\), exécution à \(t\) (pas de look-ahead).  
- **Rééquilibrage** : mensuel.  
- **Évaluation** : CAGR, Vol, Sharpe, MDD, Calmar, CAPM α/β (vs SPY), Pareto + score pour choisir (L,q).  
- **Benchmark** : SPY (buy&hold) sur les mêmes fenêtres mensuelles.

Parfait 🚀
Voici une proposition de **README.md** rédigé en **Markdown** pour ton projet momentum, calibré pour un niveau **ENS/Polytechnique / Hedge Fund (Citadel, Two Sigma)**.
Le but : être **pro, clair et impactant** → présentation structurée, explication du code, résultats et axes d’amélioration.

---

# Momentum Strategy on the S&P500

## 📌 Project Overview

This project implements and backtests a **cross-sectional momentum strategy** on the **S&P500** universe (2004–2025).
The objective is to test the robustness of the momentum anomaly, compare it with the benchmark (SPY), and analyze its **performance/risk profile across multiple horizons**.

Key features:

* Long-only momentum portfolio selection (top quantiles by lookback horizon).
* Pareto front and **composite scoring** to select optimal parameters.
* Benchmark comparison with **Buy & Hold** and **Time-Series Momentum (TSMOM) on SPY**.
* Factor analysis (linear regression vs SPY) to measure **beta exposure and alpha generation**.

---

## ⚙️ Methodology

1. **Universe & Data**

   * Monthly prices of S&P500 constituents (2004–2025).
   * Benchmark: SPY ETF (Buy&Hold & TSMOM strategies).

2. **Momentum Signal**

   * Computed as past *L*-month returns, lagged to avoid look-ahead bias.
   * Horizons tested: *3, 6, 12, 24, 36, 48, 60, 120, 180 months*.

3. **Portfolio Construction**

   * Quantile selection (e.g. top 30%, 50%, 90%).
   * Equal weighting of selected stocks.
   * Rebalanced monthly.

4. **Evaluation Metrics**

   * CAGR, Sharpe ratio, Calmar ratio.
   * Annualized volatility, Maximum Drawdown.
   * Pareto front optimization and composite score.
   * Linear regression vs SPY: alpha, beta, R².

---

## 📊 Results (Highlights)

* **Momentum beats Buy&Hold SPY** in most horizons.
* **Long-term (60 months)**: best trade-off between return and risk (Sharpe > 1.1, Calmar 0.52).
* **Very long-term (120 months)**: lower CAGR, but strong defensiveness (lower drawdown, reduced beta).
* **Linear regression** shows momentum remains partially **correlated with SPY** (positive beta), highlighting the need for **hedging** or **market-neutral construction**.

Example visualizations:

* Bar charts comparing **CAGR** and **Sharpe ratio** across horizons (Momentum vs SPY).
* Equity curve overlays.

---

## ⚠️ Limitations

* No transaction costs, dividends, or liquidity constraints included.
* Survivorship bias (only stocks still in S&P500 as of 2025).
* Strategy tested only on US large caps.

---

## 🚀 Next Steps

To make the strategy **hedge-fund deployable**:

* Implement **hedging** (e.g. short S&P500 futures) to neutralize market beta.
* Extend to **long-short momentum portfolios** (winners vs losers).
* Apply **volatility targeting** to stabilize Sharpe across regimes.
* Add **transaction costs & liquidity filters**.
* Test across multiple asset classes and out-of-sample periods.

---

## 🛠️ Tech Stack

* **Python**: `numpy`, `pandas`, `matplotlib`
* Backtesting logic custom-built for transparency and extensibility
* Code structured for reproducibility and GitHub publication

---

## 📂 Repository Structure

```
├── data/                 # Input datasets (S&P500 prices, SPY benchmark)
├── notebooks/            # Jupyter notebooks (main workflow & experiments)
├── src/                  # Core backtest functions (momentum, metrics, scoring)
├── results/              # Output plots and summary tables
└── README.md             # Project documentation (this file)
```

---

## 📝 Conclusion

This project demonstrates a rigorous **quantitative finance pipeline**:
from **signal construction** to **portfolio backtest**, **performance attribution**, and **factor exposure analysis**.

It highlights both the **strength of the momentum anomaly** and the **importance of hedging/neutralization** to convert it into a true source of **alpha** suitable for hedge fund deployment.

---

## Données
- **Prix mensuels ajustés** (US equities, SPY).  
- **Clés API** : passez par variables d’environnement (voir `.env.example`), ne committez jamais une clé en clair.  
- **Biais** : survivance potentielle (univers figé en 2025), pas de dividendes ni coûts dans les chiffres du tableau ci-dessus.

---

## Reproduire

### Installation rapide
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
