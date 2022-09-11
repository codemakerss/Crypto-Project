#from construct_database import *

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
    
    