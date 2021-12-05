import requests
import time
import csv


class GlobalFundamentals:


    api_key = "AFWI5CJP4B1C7C6I"

    base_query_url = "https://www.alphavantage.co/query?apikey={api_key}&".format(api_key=api_key)

    functions_dictionary = {
        "listing_status": "LISTING_STATUS",
        "ipo_calendar": "IPO_CALENDAR",
        "earnings_calendar": "EARNINGS_CALENDAR",
    }


    def csv_to_list(self, csv_url):
        with requests.Session() as s:
            download = s.get(csv_url)
            decoded_content = download.content.decode("utf-8")
            cr = csv.reader(decoded_content.splitlines(), delimiter=",")
            data_list = list(cr)
            for row in data_list:
                print(row)
            return data_list


    def get_earnings_calendar_all(self, period):
        earnings_url = f"{self.base_query_url}function=EARNINGS_CALENDAR&horizon={period}"
        return self.csv_to_list(earnings_url)


    def get_ipo_calendar(self):
        ipo_data_url = f"{self.base_query_url}function=IPO_CALENDAR"
        return self.csv_to_list(ipo_data_url)


    def get_listing_status(self):
        listing_url = f"{self.base_query_url}function=LISTING_STATUS"
        return self.csv_to_list(listing_url)


    def get_global_fundamentals(self):
        for key in self.functions_dictionary:
            if key == "listing_status":
                result = self.get_listing_status()
                time.sleep(20)
            elif key == "ipo_calendar":
                result = self.get_ipo_calendar()
                time.sleep(20)
            elif key == "earnings_calendar":
                result = self.get_earnings_calendar_all("3moth")
                time.sleep(20)
