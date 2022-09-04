from pandas.core.frame import DataFrame
import mysql.connector
import time
import os 

class MySQL_Connection(object):
    def __init__(self, host : str, user : str, password :str, database : str) -> None:
        #self.apikey = apikey
        self.host = host
        self.user = user 
        self.password = password
        self.database = database
    
    # Connect to the database
    def connect_database(self) -> mysql:
        try:
            db = mysql.connector.connect(host = self.host, user = self.user, password = self.password)
            sql = 'USE ' + self.database
            cursor = db.cursor()
            cursor.execute(sql)
            #print(self.database + ' database has already been connected! ')
            return db 
        except:
            db = mysql.connector.connect(host = self.host, user = self.user, password = self.password)
            sql = 'CREATE DATABASE ' + self.database
            cursor = db.cursor()
            cursor.execute(sql)
            #print(self.database + ' database has already been successfully added in to MySQL! ')
            return db 
    
class Data_to_SQL(object):
    # Call mysql connection and API here 
    def __init__(self, mysql_connection : classmethod) -> None:
        self.mysql_connection = mysql_connection.connect_database()

    # define table datatypes 
    def table_datatypes(self, table_name : str):
        try:
            if table_name == 'daily':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255) NOT NULL, datetime DATE, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume int(11))'
            elif table_name == 'weekly':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255) NOT NULL, datetime DATE, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), adjusted_close DECIMAL(10,5), volume int(11), dividend_amt DECIMAL(10,5))'
            elif table_name == 'monthly':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255) NOT NULL, datetime DATE, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), adjusted_close DECIMAL(10,5), volume int(11), dividend_amt DECIMAL(10,5))'
            elif table_name == 'intraday':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255) NOT NULL, datetime DATETIME, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume INT(11))'
            elif table_name == 'Information':
                table_datatype = '(Symbol VARCHAR(225) NOT NULL, AssetType VARCHAR(225), Name VARCHAR(225), Exchange VARCHAR(225), Country VARCHAR(225), Sector VARCHAR(225), Industry VARCHAR(225), IpoDate DATE, DelistingDate DATE NULL, Status VARCHAR(225), PRIMARY KEY (symbol))'   
            elif table_name == 'Digital Currency Code':
                table_datatype = '(Symbol VARCHAR(225) NOT NULL PRIMARY KEY, Name VARCHAR(225), Type VARCHAR(225), Region VARCHAR(225), MarketOpen TIME, MarketClose TIME, Timezone VARCHAR(225), Currency VARCHAR(225), MatchScore DECIMAL(7,5))' 
            elif table_name == 'Digital Currency Name':
                table_datatype = '(symbol VARCHAR(225) NOT NULL, name VARCHAR(225), exchange VARCHAR(225), assetType VARCHAR(225), ipoDate DATE, delistingDate DATE NULL DEFAULT NULL, status VARCHAR(225), PRIMARY KEY (symbol))'  
            elif table_name == 'Market Code':
                table_datatype = '(symbol VARCHAR(225) NOT NULL PRIMARY KEY, name VARCHAR(225), ipoDate DATE, priceRangeLow DECIMAL(10,4), priceRangeHigh DECIMAL(10,4), currency VARCHAR(225), exchange VARCHAR(225))'
            elif table_name == 'Market Name':
                table_datatype = ''
            elif table_name == 'Time Zone':
                table_datatype = ''    
            # else:
            #     print('No data support! ')
            return table_datatype
        except:
            raise Exception("No datatype support !")
        
        
        