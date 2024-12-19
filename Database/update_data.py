from main_connection import *

def update_table():
    try:
        db_connect = db_connection()

        if db_connect is None:
            print("Connection failed")
        else:
            print("Data base connected")
        
        cr_create = db_connect.cursor()

        qry = """
               UPDATE table2
               SET 
               name='Ramlal',email='ramlal@gmail.com'
               WHERE
               id=1;  
            """
        
        cr_create.execute(qry)

        db_connect.commit()

        if cr_create:
            print("data updated")

    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()

update_table()