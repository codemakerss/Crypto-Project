from re import M
from CryptoAPI.crypto_api import *
from Database.mysql_database import *

apikey = "BF4TLBIGC0D0F8RY"
market_currency = "CNY"

# crypto data test
CryptoAPI = CryptoAPI(apikey,market_currency)
#result = CryptoAPI.Get_Crypto_Daily_Weekly_Monthly_Price("BTC","monthly")
#result = CryptoAPI.Get_Crypto_Interval_Price("BTC","5min")
#print(result)

# mysql connection test 
host="localhost" 
user="root"
password="Dhy9904191asd@@" 
database="crytodatatest"
print(mysql.connector.connect(host = host, user = user, password = password, database = database))
# MySQL_Database = MySQL_Database(host = host, user = user, password = password, database = database)
# connection_test = MySQL_Database.connect_database()
# print(connection_test)

