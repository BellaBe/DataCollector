import requests
import time
import csv


class SymbolFundamentals:

    api_key = "AFWI5CJP4B1C7C6I"

    base_query_url = "https://www.alphavantage.co/query?apikey={api_key}&".format(api_key=api_key)

    functions_dictionary = {
        "overview": "OVERVIEW",
        "earnings": "EARNINGS",
        "income_statement": "INCOME_STATEMENT",
        "balance_sheet": "BALANCE_SHEET",
        "cash_flow": "CASH_FLOW",
        "earnings_calendar": "EARNINGS_CALENDAR",
    }

    def base_function(self, symbol, function):
        base_url = "{base_query_url}function={function}&symbol={symbol}".format(base_query_url=base_query_url,
                                                                                symbol=symbol, function=function)
        data = requests.get(base_url)
        return data.json()

    def get_symbol_fundamentals(self, symbol):
        for k in self.functions_dictionary:
            if k == "earnings_calendar":
                response = self.get_earnings_calendar(symbol, k, "3month")
            else:
                response = self.base_function(symbol, k)
            print(f"{k}: {response}")
            time.sleep(20)

    def get_earnings_calendar(self, symbol, function, period):
        earnings_url = f"{self.base_query_url}symbol={symbol}&function={function}&horizon={period}"
        return self.csv_to_list(earnings_url)

    def csv_to_list(self, csv_url):
        with requests.Session() as s:
            download = s.get(csv_url)
            decoded_content = download.content.decode("utf-8")
            cr = csv.reader(decoded_content.splitlines(), delimiter=",")
            data_list = list(cr)
            for row in data_list:
                print(row)
            return data_list
