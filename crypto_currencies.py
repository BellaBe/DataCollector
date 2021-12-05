import requests
import time
import csv

api_key = "AFWI5CJP4B1C7C6I"

base_query_url = f"https://www.alphavantage.co/query?apikey={api_key}&"


def get_current_exchange_rate(from_currency, to_currency, function="CURRENCY_EXCHANGE_RATE"):
    url = f"{base_query_url}function={function}&from_currency={from_currency}&to_currency={to_currency}"
    data = requests.get(url)
    return data.json()


def get_currency_rating(symbol, function="CRYPTO_RATING"):
    url = f"{base_query_url}function={function}&symbol={symbol}"
    #print(url)
    rating = requests.get(url)
    return rating.json()


# xrp = get_currency_rating("XRP")
# print(xrp)

# btc = get_current_exchange_rate("BTC", "GBP")
# print(btc)

def get_symbols():
    with open("digital_currency_list2.csv") as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        currencies_list = []
        for dct in map(dict, data):
            currencies_list.append(dct)
        return currencies_list


symbols = get_symbols()

to_file = []
for s in symbols:
    rating = get_currency_rating(s["currency code"])
    list_values = list(rating.values())
    if len(list_values) >= 1:
        data = list_values[0]
        if type(data) != "str":
            to_file.append(data)
    time.sleep(20)

keys = to_file[0].keys()
with open("crypt_rating_fcas2.csv", "w", newline="") as f:
    w = csv.DictWriter(f, keys)
    w.writeheader()
    w.writerows(to_file)
