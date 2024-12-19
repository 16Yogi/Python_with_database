from connection import *

def create_table():
    try:
        connection = connection_databasae()  
        
        if connection is None:
            print("Failed to connect to the database")
            return
        
        cr_create = connection.cursor()  
        
        qry1 = """CREATE TABLE table1 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    time_date DATETIME DEFAULT CURRENT_TIMESTAMP
                );"""
        qry2 = """CREATE TABLE table2 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    time_date DATETIME DEFAULT CURRENT_TIMESTAMP
                );"""
        cr_create.execute(qry1)
        cr_create.execute(qry2)
        #cr_create.execute(f"{qry};{qry}")
        print("Table created successfully")  
    except mysql.connector.Error as err:
        print(f"Error: {err}")  

    finally:
        if 'cr_create' in locals():  
            cr_create.close()
        if connection:  
            connection.close()
        print("operation complete")  

create_table()
