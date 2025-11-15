import requests

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX" #insert your tingo key

tickers = ["NVDA", "MSFT", "AAPL", "AMZN", "META", "AVGO", "GOOG", "GOOGL", "BRK-B", "TSLA", "JPM", "WMT", "V", "LLY", "ORCL", "NFLX", "MA", "XOM", "COST","PG", "JNJ", "HD", "BAC", "ABBV", "PLTR", "KO", "UNH", "PM", "CSCO", "TMUS", "IBM", "WFC", "GE", "CRM", "CVX", "ABT", "MS", "AXP", "LIN", "DIS",
    "AMD", "GS", "INTU", "NOW", "MCD", "T", "MRK", "TXN", "UBER", "RTX" ]

all_data = {}

for ticker in tickers:
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    params = {
        "startDate": "2004-07-01",
        "endDate": "2025-07-01",
        "resampleFreq": "monthly",
        "format": "json"
    }
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        df["ticker"] = ticker
        all_data[ticker] = df
        print(f" Données récupérées : {ticker}")
    else:
        print(f" Erreur {response.status_code} pour {ticker}")


final_df = pd.concat(all_data.values(), ignore_index=True)
final_df.to_csv("SP500_Tiingo_Monthly.csv", index=False)
print("Fichier CSV enregistré sous : SP500_Tiingo_Monthly.csv")

API_KEY = "XXXXXXXXXXXXXXXXXXXXXX" 

tickers = [
    "ISRG", "ACN", "CAT", "BKNG", "PEP", "VZ", "QCOM", "BLK", "SCHW", "C", "SPGI", "BA", "TMO",
    "ADBE", "AMGN", "HON", "BSX", "NEE", "PGR", "AMAT", "SYK", "DHR", "PFE", "GEV", "ETN", "UNP",
    "DE", "COF", "TJX", "GILD", "MU", "PANW", "CMCSA", "LOW", "ANET", "CRWD", "ADP", "LRCX", "KKR",
    "ADI", "KLAC", "APH", "BX", "COP", "VRTX", "MDT", "CB", "NKE", "LMT", "SBUX", "MMC", "ICE", 
    "AMT"
]

all_data1 = {}

for ticker in tickers:
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    params = {
        "startDate": "2004-07-01",
        "endDate": "2025-07-01",
        "resampleFreq": "monthly",
        "format": "json"
    }
    headers = {"Authorization": f"Token {API_KEY}"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        df1 = pd.DataFrame(response.json())
        df1["ticker"] = ticker
        all_data1[ticker] = df1
        print(f"Données récupérées : {ticker}")
    else:
        print(f"Erreur {response.status_code} pour {ticker}")


final_df1 = pd.concat(all_data1.values(), ignore_index=True)
final_df1.to_csv("SP500_Tiingo_Monthly2.csv", index=False)
print("Fichier CSV enregistré sous : SP500_Tiingo_Monthly2.csv")
