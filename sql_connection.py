import mysql.connector

__mydb= None

def get_sql_connection():
    global __mydb
    if __mydb is None:
        __mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="*********",
            database="grocery_store"
        )
    return __mydb