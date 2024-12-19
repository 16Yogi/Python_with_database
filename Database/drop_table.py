from main_connection import *

def delete_table():
    try:
        db_connect = db_connection()
    
        if db_connect is None:
            print("Connection failed")
        else:
            print("Connection successfull")
        
        cr_create = db_connect.cursor()

        qry = "DROP TABLE IF EXISTS table1"

        cr_create.execute(qry)
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
        db_connect.close()
delete_table()