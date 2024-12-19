from connection import *
from export_csv import *
def insert_data():
    try:
        connection = connection_databasae()

        if connection is None:
            print("Connection failed")
        
        cr_create = connection.cursor()
        name='test1'
        email='test1@gmail.com'
        qry = """
                INSERT INTO table1(name,email)
                VALUES
                    ('test2','test2@gmail.com');   
        """
        qry1=f"INSERT INTO table1(name,email) VALUES(%s,%s)"
        qry2=f"INSERT INTO table2(name,email) VALUES(%s,%s)"

        cr_create.execute(qry1,(name,email))
        cr_create.execute(qry2,(name,email))

        connection.commit()

        if cr_create:
            print("Data inserted")
        csv_exporting = export_csv()

        if csv_exporting:
            print("CSV exported")
            
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()

insert_data()
