from main_connection import *

def alter_tabl():
    try:
        db_connect = db_connection()
        
        if db_connection is None:
            print("Connection failed")
        else:
            print("Connection succssfull")
        
        cr_create = db_connect.cursor()

        qry = """
                ALTER TABLE table2
                
            """