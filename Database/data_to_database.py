#from construct_database import *
from logging import raiseExceptions
import pandas as pd 
from pandas.core.frame import DataFrame
from mysql.connector import Error
class Data_to_SQL(object):
    """
    This class is for inserting data to mysql database

    Attributes 
    ----------
    mysql_database : classmethod

    Methods
    ----------
    connect_database(self)
        connect to mysql database and create database if not exists 
    
    table_datatypes(self, table_name : str)
        create database table datatypes

    create_table(self, table_name : str)
        create tables by selecting the correct datatypes
    """
    def __init__(self, mysql_database : classmethod) -> None:
        self.mysql_connection = mysql_database.connect_database()

    def insert_mysql_data(self, table):
        pass
    def insert_mysql_data(self, data : DataFrame, table_name : str, symbol : str) -> str:
        try:
            connection = self.mysql_connection.connect_database()
            cursor = connection.cursor()
            lst = ["daily", "weekly", "monthly"]
            # ['SYMBOL', 'DATETIME', 'OPEN (CNY)', 'OPEN (USD)', 
            # 'HIGH (CNY)', 'HIGH (USD)', 'LOW (CNY)', 'LOW (USD)', 
            # 'CLOSE (CNY)', 'CLOSE (USD)', 'VOLUME', 'MARKET CAP (USD)']

            try:
                if table_name in lst:
                    for index,row in data.iterrows():  
                        #row.datetime = row.datetime.strftime("%Y-%m-%d")
                        sql = "INSERT INTO " + table_name + "(crypto, datetime, open, high, low, close, volume, marketcap)" + " VALUES" + str(tuple(row))
                        cursor.execute(sql)
                        connection.commit()
                    print(symbol + " data has already been updated into the " + table_name + " table! ")
            except:
                raiseExceptions(symbol + " failed to add to databse. ")
            # elif table_name in lst:
            #     for index,row in data.iterrows():  
            #         row.datetime = row.datetime.strftime("%Y-%m-%d")
            #         sql = "INSERT INTO " + table_name + "(symbol, datetime, open, high, low, close, adjusted_close, volume, dividend_amt)" + " VALUES" + str(tuple(row))
            #         cursor.execute(sql)
            #         connection.commit()
            #     print(symbol + " data has already been updated into the " + table_name + " table! ")

            # elif table_name == "intraday":
            #     for index,row in data.iterrows():
            #         sql = "INSERT INTO " + table_name + "(symbol, datetime, open, high, low, close, volume)" + " VALUES" + str(tuple(row))
            #         cursor.execute(sql)
            #         connection.commit()
            #     print(symbol+ " data has already been updated into the " + table_name + " table! ")

            # # use Info_collected classmethod in the API file
            # elif table_name == "company_info":
            #     for index,row in data.iterrows():
            #         sql = "INSERT INTO " + table_name + " VALUES" + str(tuple(row))
            #         cursor.execute(sql)
            #         connection.commit()
            #     print(symbol + " data has already been updated into the " + table_name + " table! ")
                
            # elif table_name == "search":
            #     for index,row in data.iterrows():
            #         sql = "INSERT INTO " + table_name + " VALUES" + str(tuple(row))
            #         cursor.execute(sql)
            #         connection.commit()
            #     print(symbol + " data has already been updated into the " + table_name + " table! ")
            connection.close()
        except Error as e:
             raise e 
    
