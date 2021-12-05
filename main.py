import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import yfinance as yf

alpha_vantage_api_key = "AFWI5CJP4B1C7C6I"

ts = TimeSeries(key=alpha_vantage_api_key, output_format="pandas")

ticker = "GE"


# GE_daily_data_tuple = ts.get_daily("GE")
#
# GE_daily_data_full = ts.get_daily(ticker, outputsize="full")[0]
#
# GE_daily_data_length = len(GE_daily_data_tuple)
#
# GE_daily_data = GE_daily_data_tuple[0]
# GE_daily_metadata = GE_daily_data_tuple[1]
#
# GE_daily_metadata_info = GE_daily_metadata["1. Information"]
#
# GE_daily_metadata_symbol = GE_daily_metadata["2. Symbol"]
#
# GE_daily_metadata_last_refreshed = GE_daily_metadata["3. Last Refreshed"]
#
# GE_daily_metadata_output_size = GE_daily_metadata["4. Output Size"]
#
# GE_daily_metadata_timezone = GE_daily_metadata["5. Time Zone"]
#
# GE_head = GE_daily_data.head()
#
# GE_tail = GE_daily_data.tail()
#
#
# GE_daily_data_datetime_index = GE_daily_data.index

# print(GE_daily_data_datetime_index)

# GEy = yf.download(ticker, start=GE_daily_data_datetime_index[1])

# GEa_adjusted = ts.get_daily_adjusted(ticker, outputsize="full")[0]

# print(GEa_adjusted.iloc[:, -1].value_counts())
# print(GEa_adjusted[GEa_adjusted.iloc[:, -1] == 3])
# print(GEa_adjusted.loc["2000-05-03":"2000-05-10"])

# GEa = ts.get_daily(ticker, outputsize="full")[0]
#
#
def convert_to_datetime_index(index):
    index = pd.to_datetime(index)
    return index


#
#
# print(GEa.head())
# print(GEa.info())
# print(GEa.index[0])
# GEa.index = convert_to_datetime_index(GEa.index)
# print(GEa.info())
#
# print(GEa.loc["2017"])


GEa = ts.get_intraday(ticker, outputsize="full", interval="60min")[0]


# print(GEa)


def get_batch_data(tickers):
    stocks = ts.get_batch_stock_quotes(tickers)
    return stocks

# def main(name):
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# if __name__ == '__main__':
#     main('PyCharm')
