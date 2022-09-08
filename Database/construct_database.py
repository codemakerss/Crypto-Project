from pandas.core.frame import DataFrame
import mysql.connector
from mysql.connector import ProgrammingError
import time
import os 


class MySQL_Database(object):
    """
    This class is for MySQL database build up and make connection

    Attributes 
    ----------
    host : str
    user : str
    password : str 
    database : str 

    Methods
    ----------
    connect_database(self)
        Connect to MySQL database and create database if not exists 
    
    Results
    ----------

    
    """
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
        except ProgrammingError:
            db = mysql.connector.connect(host = self.host, user = self.user, password = self.password)
            sql = 'CREATE DATABASE ' + self.database
            cursor = db.cursor()
            cursor.execute(sql)
            print(self.database + ' database has already been successfully added in to MySQL! ')
            return db 
        except:
            raise Exception("Fail to connect or create database. ")
    
    # define table datatypes 
    def table_datatypes(self, table_name : str):
        # Intraday columns Index['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']
        # Others (daily, weekly, monthly) columns Index['OPEN (USD)', 'OPEN (USD)', \
        # 'HIGH (USD)', 'HIGH (USD)', 'LOW (USD)','LOW (USD)', 'CLOSE (USD)', 'CLOSE (USD)', \
        # 'VOLUME','MARKET CAP (USD)']
        try:
            if table_name == 'daily' or table_name == 'weekly' or table_name == 'monthly':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(255) NOT NULL, datetime DATE, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume int(11), marketcap int(11))'
           
            elif table_name == 'intraday':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(255) NOT NULL, datetime DATETIME, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume INT(11))'
            # elif table_name == 'Information':
            #     table_datatype = '(Symbol VARCHAR(225) NOT NULL, AssetType VARCHAR(225), Name VARCHAR(225), Exchange VARCHAR(225), Country VARCHAR(225), Sector VARCHAR(225), Industry VARCHAR(225), IpoDate DATE, DelistingDate DATE NULL, Status VARCHAR(225), PRIMARY KEY (symbol))'   
            # elif table_name == 'Digital Currency Code':
            #     table_datatype = '(Symbol VARCHAR(225) NOT NULL PRIMARY KEY, Name VARCHAR(225), Type VARCHAR(225), Region VARCHAR(225), MarketOpen TIME, MarketClose TIME, Timezone VARCHAR(225), Currency VARCHAR(225), MatchScore DECIMAL(7,5))' 
            # elif table_name == 'Digital Currency Name':
            #     table_datatype = '(symbol VARCHAR(225) NOT NULL, name VARCHAR(225), exchange VARCHAR(225), assetType VARCHAR(225), ipoDate DATE, delistingDate DATE NULL DEFAULT NULL, status VARCHAR(225), PRIMARY KEY (symbol))'  
            # elif table_name == 'Market Code':
            #     table_datatype = '(symbol VARCHAR(225) NOT NULL PRIMARY KEY, name VARCHAR(225), ipoDate DATE, priceRangeLow DECIMAL(10,4), priceRangeHigh DECIMAL(10,4), currency VARCHAR(225), exchange VARCHAR(225))'
            # elif table_name == 'Market Name':
            #     table_datatype = ''
            # elif table_name == 'Time Zone':
            #     table_datatype = ''    
            # else:
            #     print('No data support! ')
            return table_datatype
        except:
            raise Exception("No datatype support !")
            
class Data_to_SQL(object):
    # Call mysql connection and API here 
    def __init__(self, mysql_database : classmethod) -> None:
        self.mysql_connection = mysql_database.connect_database()

    
        
        
        