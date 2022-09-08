
class Data_to_SQL(object):
    # Call mysql connection and API here 
    def __init__(self, mysql_database : classmethod) -> None:
        self.mysql_connection = mysql_database.connect_database()