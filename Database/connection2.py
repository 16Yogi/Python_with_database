import mysql.connector

def connect_db():
    try:
        connect_database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4",
            database="db1"
        )

        cr_create = connect_database.cursor()

        if cr_create:
            print("connection successfull")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()

connect_db()