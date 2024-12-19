import mysql.connector

def create_database():
    try:
        create_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4"
        )
        
        cr_create=create_db.cursor()
    
        qry="""CREATE DATABASE db2"""
    
        cr_create.execute(qry)

        if cr_create:
            print("Database created")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()

create_database()

