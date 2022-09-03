from crypt import crypt
from pandas.core.frame import DataFrame
from locale import currency
from mimetypes import init
import requests
import pandas as pd 

apikey = "BF4TLBIGC0D0F8RY"

# stock_id = "ETH"
# market_currency = "USD" 
# interval = "5min"

class CrytoAPI(object):
    def __init__(self, apikey : str, market_currency : str):
        self.apikey = apikey
        #self.crypto = crypto
        self.market_currency = market_currency

    def Get_Crypto_Interval_Price(self, crypto : str, interval : str) -> DataFrame:
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

    def Get_Crypto_Daily_Price(self, crypto : str) -> DataFrame:
        base_url = 'https://www.alphavantage.co/query?'
        params = {"function": "DIGITAL_CURRENCY_DAILY", "symbol": crypto, "market": self.market_currency,"apikey": self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        
        daily_data = data["Meta Data"]
        crypto_info = pd.DataFrame.from_dict(daily_data, orient='index', columns=['info']) 
        crypto_interval_data = data["Time Series (Digital Currency Daily)"]

        crypto_daily_data_full = pd.DataFrame.from_dict(crypto_interval_data, orient='index') 
        crypto_daily_data_full = crypto_daily_data_full.rename(columns={'1a. open (' + self.market_currency + ')':'OPEN (' + self.market_currency + ')', \
        '1b. open (USD)' : 'OPEN (USD)', '2a. high (' + self.market_currency + ')':'HIGH (' + self.market_currency + ')', '2b. high (USD)' : 'HIGH (USD)', 
        '3a. low (' + self.market_currency + ')':'LOW (' + self.market_currency + ')', '3b. low (USD)':'LOW (USD)', '4a. close (' + self.market_currency + ')':'CLOSE (' + self.market_currency + ')', \
        '4b. close (USD)':'CLOSE (USD)','5. volume':'VOLUME', '6. market cap (USD)':'MARKET CAP (USD)'})
    
        return crypto_info, crypto_daily_data_full




