from main_connection import *

def data_delete():
    try:
        db_connect = db_connection()
    
        if db_connection is None:
            print("Connection failed")
        else:
            print("Connection successful")
        
        cr_create = db_connect.cursor()
    
        qry = "DELETE FROM table1 WHERE id=2"
    
        cr_create.execute(qry)
    
        db_connect.commit()
        
        if cr_create:
            print("Data deleted")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
        db_connect.close()
data_delete()