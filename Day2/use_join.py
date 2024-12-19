from connection import *

def select_join():
    try:
        connection = connection_databasae()  

        if connection is None:
            print("Connection failed")
            return
        else:
            print("Connection successful")
        
        cr_create = connection.cursor()
        
        number_value = "7896541230"  

        qry = """
                INSERT INTO table2 (name, email, time_date, number)
                SELECT table1.name, table1.email, table1.time_date, %s
                FROM table1
                LEFT JOIN table2 
                ON table1.id = table2.id
                AND table1.name = table2.name
                AND table1.email = table2.email
                AND table1.time_date = table2.time_date
            """

        cr_create.execute(qry, (number_value,))

        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cr_create.close()  
        if connection:
            connection.close()  

select_join()
