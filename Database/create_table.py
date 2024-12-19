from connection import *

def create_table():
    try:
        connection_db()
        
        # cr_create = 
        create_table = ""

    except mysql.connector.Error as err:
        print(f"Error:{err}")

create_table()