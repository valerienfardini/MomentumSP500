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
