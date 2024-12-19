import mysql.connector

def connection_db():
    try:

        db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "ConVox@4",
            database = "db1"
        )
    
        cr_create = db_connection.cursor()
    
        if cr_create:
            print("Connection successfull")
    
    except mysql.connector.Error as err:
        print(f"Error:{err}")

    finally:
        cr_create.close()
    
connection_db()
    