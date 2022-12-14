from crypt import crypt
from pandas.core.frame import DataFrame
import requests
import time
import pandas as pd 
import datetime
apikey = "BF4TLBIGC0D0F8RY"

# stock_id = "ETH"
# market_currency = "USD" 
# interval = "5min"

class CryptoAPI(object):
    """
    This class is for retrieving crypto data from 
    Alpha Vantage website 

    Attributes 
    ----------
    apikey : str
    market_currency : str

    Methods
    ----------
    get_crypto_interval_price(self, crypto : str, interval : str)
        return crypto interval data 

    get_crypto_daily_weekly_monthly_price(self, crypto : str, day_time : str)
        return cryto daily/weekly/monthly data
    """
    def __init__(self, apikey : str, market_currency : str):
        self.apikey = apikey
        #self.crypto = crypto
        self.market_currency = market_currency

    def get_crypto_interval_price(self, crypto : str, interval : str) -> DataFrame:
        """
        return crypto interval data in DataFrame format

        Parameters 
        ----------
        crypto : str
            cryptocurrency name in abbreviation
        interval : str
            choose time interval from 1min, 5min, 15min, 30min, 60min
        """
        try:
            start = time.time()
            base_url = 'https://www.alphavantage.co/query?'
            params = {"function": "CRYPTO_INTRADAY", "symbol": crypto, "market": self.market_currency,"interval": interval, "outputsize": "full","apikey": self.apikey}
            response = requests.get(base_url, params=params)
            data = response.json() # dict
        
            intraday_data = data["Meta Data"]
            crypto_info = pd.DataFrame.from_dict(intraday_data, orient='index', columns=['info']) 
            crypto_interval_data = data["Time Series Crypto ("+ interval +")"]

            crypto_interval_data_full = pd.DataFrame.from_dict(crypto_interval_data, orient='index') 
            crypto_interval_data_full = crypto_interval_data_full.rename(columns={'1. open':'OPEN','2. high':'HIGH','3. low':'LOW','4. close':'CLOSE','5. volume':'VOLUME'})
            
            # time cost
            end = time.time()
            time_cost= end - start

            # reconstruct dataframe to match with the mysql database format
            crypto_interval_data_full.reset_index(inplace=True)
            crypto_interval_data_full = crypto_interval_data_full.rename(columns = {'index':'DATETIME'})
            
            symbol_list = []
            r,c = crypto_interval_data_full.shape
            for i in range(r):
                symbol_list.append(crypto)

            crypto_interval_data_full.insert(loc=0,column='CRYPTO',value=symbol_list)

            # show information about the data output and time cost
            print(crypto_info,"\n")
            print("time cose : ", time_cost, "\n")

            return crypto_interval_data_full
        except:
            raise Exception("Fail to retrieve crypto " + interval + " interval data !")

    def get_crypto_daily_weekly_monthly_price(self, crypto : str, day_time : str) -> DataFrame:
        """
        return crypto daily/weekly/monthly data in DataFrame format

        Parameters 
        ----------
        crypto : str
            cryptocurrency name in abbreviation
        day_time : str
            choose from daily/weekly/monthly
        """
        try:
            start = time.time()
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

            # time cost
            end = time.time()
            time_cost= end - start

            # reconstruct dataframe to match with the mysql database format
            crypto_day_time_data_full.reset_index(inplace=True)
            crypto_day_time_data_full = crypto_day_time_data_full.rename(columns = {'index':'DATETIME'})
            # add symbol column 
            symbol_list = []
            r,c = crypto_day_time_data_full.shape
            for i in range(r):
                symbol_list.append(crypto)

            crypto_day_time_data_full.insert(loc=0,column='CRYPTO',value=symbol_list)
            
            #print(crypto_day_time_data_full)
            print(crypto_info,"\n")
            print("time cose : ", time_cost, "\n")
            
            return crypto_day_time_data_full
        except:
            raise Exception("Fail to retrieve " + crypto + " data !")

    




