import numpy as np
import pandas as pd 

def verdict_mom_spy(df_momentum: pd.DataFrame, df_spy: pd.DataFrame) -> pd.DataFrame:
    df_mom = df_momentum.copy()
    
    df_mom = df_mom.rename(columns={"Composite Score" : "Composite Momentum"})
    df_mom["Composite Spy"] = df_spy["Composite Score"]

    df_mom["winner"] = np.where(df_mom["Composite Momentum"] > df_mom["Composite Spy"],
                               "Winner Momentum",
                               np.where(df_mom["Composite Momentum"] < df_mom["Composite Spy"],
                                        "Winner Spy",
                                        "tie"))
    df_mom["edge"] = df_mom["Composite Momentum"] - df_mom["Composite Spy"] 

    return df_mom
