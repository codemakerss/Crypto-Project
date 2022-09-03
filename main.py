from CryptoAPIFile.crypto_api import *

apikey = "BF4TLBIGC0D0F8RY"
market_currency = "CNY"

CrytoAPI = CrytoAPI(apikey,market_currency)
result = CrytoAPI.Get_Crypto_Daily_Weekly_Monthly_Price("BTC","monthly")
print(result)