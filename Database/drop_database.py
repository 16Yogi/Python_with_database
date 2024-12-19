import mysql.connector

def delete_db():
    try:
        del_database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4"
        )

        cr_create = del_database.cursor()

        qry = """DROP DATABASE db2"""

        cr_create.execute(qry)

        if cr_create:
            print("Database deleted")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
delete_db()