from main_connection import *

def data_selection():
    try:
        db_connect = db_connection()

        if db_connect is None:
            print("Connection successfull")
        else:
            print("Database connection")

        cr_create = db_connect.cursor()

        qry = "SELECT * FROM table1"

        cr_create.execute(qry)

        result = cr_create.fetchall()

        for i in result:
            print(i)
            
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    # finally:
data_selection()