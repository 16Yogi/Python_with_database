from connection import *

def delete_table():
    try:
        # connection 
        connect = connection_databasae()

        if connect is None:
            print("Connection failed")
        else:
            print("Connection successfull")
        
        cr_create = connect.cursor()

        qry = """
                DELETE FROM table2;
            """

        cr_create.execute(qry)
        connect.commit()

        if cr_create:
            print("Table deleted")
        else:
            print("Table deletion failed")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
delete_table()