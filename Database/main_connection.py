import mysql.connector

def db_connection():
    try:
        db_connect = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "ConVox@4",
            database = "db1"
        )
    
        return db_connect
    except mysql.connector.Error as err:
        print(f"Error:{err}")
db_connection()