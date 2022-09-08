from crypt import crypt
from pandas.core.frame import DataFrame
import requests
import pandas as pd 

apikey = "BF4TLBIGC0D0F8RY"

# stock_id = "ETH"
# market_currency = "USD" 
# interval = "5min"

class CryptoAPI(object):
    def __init__(self, apikey : str, market_currency : str):
        self.apikey = apikey
        #self.crypto = crypto
        self.market_currency = market_currency

    def Get_Crypto_Interval_Price(self, crypto : str, interval : str) -> DataFrame:
        try:
            base_url = 'https://www.alphavantage.co/query?'
            params = {"function": "CRYPTO_INTRADAY", "symbol": crypto, "market": self.market_currency,"interval": interval, "outputsize": "full","apikey": self.apikey}
            response = requests.get(base_url, params=params)
            data = response.json() # dict
        
            intraday_data = data["Meta Data"]
            crypto_info = pd.DataFrame.from_dict(intraday_data, orient='index', columns=['info']) 
            crypto_interval_data = data["Time Series Crypto ("+ interval +")"]

            crypto_interval_data_full = pd.DataFrame.from_dict(crypto_interval_data, orient='index') 
            crypto_interval_data_full = crypto_interval_data_full.rename(columns={'1. open':'OPEN','2. high':'HIGH','3. low':'LOW','4. close':'CLOSE','5. volume':'VOLUME'})
        
            return crypto_info, crypto_interval_data_full
        except:
            raise Exception("Fail to retrieve crypto " + interval + " interval data !")

    def Get_Crypto_Daily_Weekly_Monthly_Price(self, crypto : str, day_time : str) -> DataFrame:
        try:
            try:
                # check day time and output error 
                if (day_time.lower() == "daily"):
                    params = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": crypto, "market": self.market_currency,"apikey": self.apikey}
                elif (day_time.lower() == "weekly"):
                    params = {"function": "DIGITAL_CURRENCY_WEEKLY", "symbol": crypto, "market": self.market_currency,"apikey": self.apikey}
                elif (day_time.lower() == "monthly"):
                    params = {"function": "DIGITAL_CURRENCY_MONTHLY", "symbol": crypto, "market": self.market_currency,"apikey": self.apikey}
            except:
                raise Exception("Error in day time choose !") 

            # reorganize json data to DataFrame type
            base_url = 'https://www.alphavantage.co/query?'
            response = requests.get(base_url, params=params)
            data = response.json() # dict
            
            daily_data = data["Meta Data"]
            crypto_info = pd.DataFrame.from_dict(daily_data, orient='index', columns=['info'])

            try:
                # check day time and output error 
                if (day_time.lower() == "daily"):
                    crypto_day_time_data = data["Time Series (Digital Currency Daily)"]
                elif (day_time.lower() == "weekly"):
                    crypto_day_time_data = data["Time Series (Digital Currency Weekly)"]
                elif (day_time.lower() == "monthly"):
                    crypto_day_time_data = data["Time Series (Digital Currency Monthly)"]
            except:
                raise Exception("Fail to retrieve " + crypto + " json data !")  
            
            crypto_day_time_data_full = pd.DataFrame.from_dict(crypto_day_time_data, orient='index') 
            crypto_day_time_data_full = crypto_day_time_data_full.rename(columns={'1a. open (' + self.market_currency + ')':'OPEN (' + self.market_currency + ')', \
            '1b. open (USD)' : 'OPEN (USD)', '2a. high (' + self.market_currency + ')':'HIGH (' + self.market_currency + ')', '2b. high (USD)' : 'HIGH (USD)', 
            '3a. low (' + self.market_currency + ')':'LOW (' + self.market_currency + ')', '3b. low (USD)':'LOW (USD)', '4a. close (' + self.market_currency + ')':'CLOSE (' + self.market_currency + ')', \
            '4b. close (USD)':'CLOSE (USD)','5. volume':'VOLUME', '6. market cap (USD)':'MARKET CAP (USD)'})

            # show information about the data output 
            print(crypto_info,"\n")
            
            return crypto_day_time_data_full
        except:
            raise Exception("Fail to retrieve " + crypto + "data !")

    




