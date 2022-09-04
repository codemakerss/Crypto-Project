from CryptoAPIFile.crypto_api import *

apikey = "BF4TLBIGC0D0F8RY"
market_currency = "CNY"

CryptoAPI = CryptoAPI(apikey,market_currency)
#result = CryptoAPI.Get_Crypto_Daily_Weekly_Monthly_Price("BTC","monthly")
result = CryptoAPI.Get_Crypto_Interval_Price("BTC","5min")
print(result)