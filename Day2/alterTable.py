from connection import *

def alter_table():
    try:
        # connection
        connect = connection_databasae()
    
        if connect is None:
            print("Connection failed")
        else:
            print("Connection successfull")
    
        cr_create = connect.cursor()
    
        # qry = """
        #         ALTER TABLE table2 
        #         ADD COLUMN 
        #             number INT(255) NOT NULL;
        #     """
        
        qry = """
                ALTER TABLE table2
                MODIFY COLUMN
                number VARCHAR(255) NOT NULL;
                
            """

        cr_create.execute(qry)
    except mysql.connect.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
alter_table()