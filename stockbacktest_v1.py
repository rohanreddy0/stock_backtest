import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# define stocks and download data to csv
ticker_list = ["VUAG.L", "XNAQ.L", "VWRP.L", "VHVG.L", "VFEG.L"]

# save price data as dataframes in dictionary
d = {}
for ticker in ticker_list:
    d[ticker] = yf.Ticker(ticker).history(period="max")

# find starting date of data for each ticker
datelist = {}
for ticker in d:
    datelist[ticker] = min(d[ticker].index)

# earliest date from which all ticker items can be tested
earliest_date = min(d[max(datelist)].index)
print(f"Simulation can begin from: {earliest_date}")