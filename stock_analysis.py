# investment_dashboard/modules/stock_analysis.py
import pandas as pd
import random

def scan_all_stocks(min_roi):
    sp500_stocks = [
        "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "BRK-B", "JNJ", "JPM", "V",
        "NVDA", "UNH", "HD", "PG", "DIS", "MA", "BAC", "XOM", "VZ", "INTC",
        "KO", "MRK", "PEP", "T", "ABBV", "CVX", "ABT", "WMT", "MCD", "ADBE",
        "CRM", "NFLX", "COST", "WFC", "MDT", "TMO", "NKE", "AMGN", "LLY", "NEE",
        "DHR", "LIN", "TXN", "BMY", "AVGO", "PM", "UNP", "LOW", "UPS", "SBUX",
        "INTU", "RTX", "HON", "QCOM", "IBM", "GS", "AMAT", "GE", "CAT", "DE",
        "ZTS", "ISRG", "BLK", "LMT", "ADI", "BKNG", "PLD", "CB", "GILD", "MO",
        "TGT", "SYK", "MMC", "EL", "USB", "CI", "MDLZ", "FIS", "PNC", "SO",
        "ADP", "SPGI", "DUK", "CL", "VRTX", "BDX", "APD", "FISV", "C", "REGN",
        "AON", "ITW", "ETN", "HUM", "AEP", "TFC", "CSCO", "EMR", "PSA", "EXC"
    ]

    penny_stocks = [
        "SNDL", "NOK", "GPRO", "ZOM", "GTE", "IDEX", "TRCH", "ENZC", "AITX", "HCMC",
        "ASTI", "PUGE", "OPTI", "DPLS", "ILUS", "ALPP", "VYST", "CLWD", "HMBL", "INND",
        "IQST", "TONR", "NSAV", "OWUV", "BDGR", "AABB", "IFAN", "CYBL", "GGII", "SFOR",
        "RNVA", "TGGI", "TSNP", "RGGI", "PHIL", "XELA", "AXXA", "ALZN", "AVGR", "BBIG",
        "CEI", "ENSC", "GNS", "HUSA", "IMPP", "JAGX", "KAVL", "LTRY", "MULN", "NAKD",
        "NXTP", "OPTT", "PRTY", "QNRX", "RDBX", "SEEL", "TBLT", "VINE", "XCUR", "ZIVO",
        "ACER", "AEI", "AEMD", "AGRX", "ALLR", "AMST", "APRN", "AYRO", "BBLG", "BIMI",
        "BKYI", "BOXL", "BRQS", "BSQR", "BTB", "CBAT", "CLRB", "CLSN", "CNTG", "CPHI",
        "CRIS", "CTIB", "CWBR", "CYCC", "DRRX", "DSS", "DYNT", "EDSA", "ELOX", "ENOB",
        "EVFM", "EYEG", "FAMI", "FORD", "GALT", "GIGM", "GLBS", "GLMD", "WISA", "YTEN"
    ]

    all_stocks = sp500_stocks + penny_stocks
    stock_data = []

    for stock in all_stocks:
        price = random.uniform(5, 500)
        projected_value = price * random.uniform(1.05, 2.5)
        roi = (projected_value - price) / price

        if roi >= min_roi:
            stock_data.append({
                "Stock": stock,
                "Price": round(price, 2),
                "Projected Value": round(projected_value, 2),
                "ROI": round(roi * 100, 2),
                "Stock URL": f"https://finance.yahoo.com/quote/{stock}"
            })

    return pd.DataFrame(stock_data)
