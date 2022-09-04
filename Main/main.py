from re import M
from CryptoAPIFile.crypto_api import *
from Database.MySQL_Database import *
apikey = "BF4TLBIGC0D0F8RY"
market_currency = "USD"

# crypto data test
CryptoAPI = CryptoAPI(apikey,market_currency)
#result = CryptoAPI.Get_Crypto_Daily_Weekly_Monthly_Price("BTC","monthly")
#result = CryptoAPI.Get_Crypto_Interval_Price("BTC","5min")
#print(result[1].columns)

# mysql connection test 
host="localhost" 
user="root"
password="Dhy9904191asd@@" 
database="crytodatatest"
MySQL_Database = MySQL_Database(host = host, user = user, password = password, database = database)
connection_test = MySQL_Database.connect_database()
print(connection_test)

