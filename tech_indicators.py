import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import yfinance as yf
alpha_vantage_api_key = "AFWI5CJP4B1C7C6I"
ti = TechIndicators(key=alpha_vantage_api_key, output_format="pandas")

sma = ti.get_sma("MSFT", interval="daily", time_period=50)[0]
ts = TimeSeries(key=alpha_vantage_api_key, output_format="pandas")

close = ts.get_daily("MSFT")[0]

#print(close.loc[:, "4. close"].head())
# print(type(close.loc[:, "4. close"].head()))
# for d in close.loc[:, "4. close"].head():
#     print(d)

reindexed_close = close.loc[:, "4. close"].head().reindex(sma.tail().index)

#reindexed_close["SMA"] = sma.tail()

#print(reindexed_close)

sma["close"] = reindexed_close



# print(close)

print(sma.tail())

tail = sma.tail()

tail.plot(figsize=(12, 8))
plt.show()

# df = sma.tail().merge(reindexed_close, left_index=True, right_index=True)
# print(df)