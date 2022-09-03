# from coinapi_rest_v1.restapi import CoinAPIv1
# import datetime, sys

# #test_key = sys.argv[1]

# api = CoinAPIv1("5A1DB058-A448-461A-BF9F-22AD6E9A3DB8")
# exchanges = api.metadata_list_exchanges()

# print('Exchanges')


#import platform    
#platform.python_implementation()


from locale import currency
import requests
import pandas as pd 

stock_id = "ETH"
market_currency = "USD" 
interval = "5min"
apikey = "BF4TLBIGC0D0F8RY"
base_url = 'https://www.alphavantage.co/query?'
df = pd.DataFrame()
df_new = pd.DataFrame()
params = {"function": "CRYPTO_INTRADAY", "symbol": stock_id, "market": market_currency,"interval": interval, "outputsize": "full","apikey": apikey}
response = requests.get(base_url, params=params)
data = response.json() # dict

intraday_data = data["Meta Data"]
#print(data)
data_2 = pd.DataFrame.from_dict(intraday_data, orient='index', columns=['info'])                                                             
print(data_2)
data_3 = data["Time Series Crypto (5min)"]
d2 = pd.DataFrame.from_dict(data_3, orient='index') 
d2 = d2.rename(columns={'1. open':'OPEN','2. high':'HIGH','3. low':'LOW','4. close':'CLOSE','5. volume':'VOLUME'})
print(d2)

# data_1 = intraday_data.items()
# info_list = []
# for i in data_1:
#     info_list.append(i[0])
# dict_col = {"info":info_list}
# dataframe_info = pd.DataFrame(dict_col)
# #d = dataframe_info.rename(columns={"0": "a"})
# dataframe_info =  dataframe_info.set_index("info")
# print(dataframe_info)
# for i in data["Meta Data"]["1. Information"]:
#     print(i)
# for dict in intraday_data:
#     small_dict = intraday_data[dict]
#     small_dict["Datetime"] = dict
#     df = df.append(pd.DataFrame([small_dict]))


# df_new = df[["Datetime", "1. open", "2. high", "3. low", "4. close", "5. volume"]]
# df_new = df_new.rename(columns = {"1. open" : "Open", "2. high": "High", "3. low" : "Low", "4. close" : "Close", "5. volume" : "Volume"})

# col_name = df_new.columns.tolist()
# col_name.insert(0,"Symbol")
# df_new = df_new.reindex(columns=col_name)
# df_new["Symbol"] = stock_id
import os
print(os.popen('which python').read())
