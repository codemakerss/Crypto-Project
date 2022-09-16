from logging import raiseExceptions
from pandas.core.frame import DataFrame
import mysql.connector
from mysql.connector import ProgrammingError
from mysql.connector import Error
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
        connect to mysql database and create database if not exists 
    
    table_datatypes(self, table_name : str)
        create database table datatypes

    create_table(self, table_name : str)
        create tables by selecting the correct datatypes
    """
    def __init__(self, host : str, user : str, password :str, database : str) -> None:
        #self.apikey = apikey
        self.host = host
        self.user = user 
        self.password = password
        self.database = database

    # Connect to the database
    def connect_database(self) -> mysql:
        """
        connect to mysql database if exsists
        create new database if not

        Parameters 
        ----------
        none
        
        Raises
        ----------
        raise mysql.connector errors 
        """
        try:
            db = mysql.connector.connect(host = self.host, user = self.user, password = self.password)
            sql = 'USE ' + self.database
            cursor = db.cursor()
            cursor.execute(sql)
            #print(self.database + ' database has already been connected! ')
            return db 
        except Error:
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
        """
        create mysql database table datatypes 

        Parameters 
        ----------
        table_name : str
            choose table name datatypes 
        
        Raises
        ----------
        raise mysql.connector errors 
        """
        # Intraday columns Index['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']
        # Others (daily, weekly, monthly) columns Index['OPEN (USD)', 'OPEN (USD)', \
        # 'HIGH (USD)', 'HIGH (USD)', 'LOW (USD)','LOW (USD)', 'CLOSE (USD)', 'CLOSE (USD)', \
        # 'VOLUME','MARKET CAP (USD)']
        try:
            if table_name == 'daily' or table_name == 'weekly' or table_name == 'monthly':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(255) NOT NULL, datetime DATE, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume int(11), marketcap int(11))'
            elif table_name == 'intraday':
                table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(255) NOT NULL, datetime DATETIME, open DECIMAL(10,5), high DECIMAL(10,5), low DECIMAL(10,5), close DECIMAL(10,5), volume INT(11))'
            elif table_name == 'digitalcurrencylist':
                 table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(225) NOT NULL, name VARCHAR(225))'   
            elif table_name == 'physicalcurrencylist':
                 table_datatype = '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, crypto VARCHAR(225) NOT NULL, name VARCHAR(225))' 
            # elif table_name == 'Digital Currency Name':
            #     table_datatype = '(symbol VARCHAR(225) NOT NULL, name VARCHAR(225), exchange VARCHAR(225), assetType VARCHAR(225), ipoDate DATE, delistingDate DATE NULL DEFAULT NULL, status VARCHAR(225), PRIMARY KEY (symbol))'  
            # elif table_name == 'Market Code':
            #     table_datatype = '(symbol VARCHAR(225) NOT NULL PRIMARY KEY, name VARCHAR(225), ipoDate DATE, priceRangeLow DECIMAL(10,4), priceRangeHigh DECIMAL(10,4), currency VARCHAR(225), exchange VARCHAR(225))'  
            # else:
            #     print('No data support! ')
            return table_datatype
        except:
            raise Exception("No datatype support !")

    def create_table(self, table_name : str) -> str:
        """
        create mysql database tables 

        Parameters 
        ----------
        table_name : str
            choose table name users want to insert data for
        
        Raises
        ----------
        raise mysql.connector errors 
        """
        try:
            mysql_connection = self.connect_database()
            cursor = mysql_connection.cursor()
            #for name in table_name:
            try:
                order = self.table_datatypes(table_name)
                sql = 'CREATE TABLE ' + table_name + ' '+ order
                cursor.execute(sql)
                mysql_connection.commit()
                return table_name + ' table has already been successfully added in to MySQL! '
            except Error as e:
                raise(e)
            mysql_connection.close()
        except Error as e:
            raise(e)
    
    def reconstruct_inputs(self, original_input : DataFrame):
        """
        reconstruct the database inputs 

        Parameters 
        ----------
        original_input : DataFrame
            original data from the api port online  
        
        Raises
        ----------
        raise mysql.connector errors 
        """

        # ['SYMBOL', 'DATETIME', 'OPEN (CNY)', 'OPEN (USD)', 
        # 'HIGH (CNY)', 'HIGH (USD)', 'LOW (CNY)', 'LOW (USD)', 
        # 'CLOSE (CNY)', 'CLOSE (USD)', 'VOLUME', 'MARKET CAP (USD)']
        try:
            col_name = list(original_input)
            # remove index 3,5,7,9
            remove_index = [3,5,7,9]
            for i in remove_index:
                original_input.pop(col_name[i - 1])
        except:
            raiseExceptions("Fail to reconstruct the original data.")

        return original_input
        


    
        
        
        