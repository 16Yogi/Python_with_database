import mysql.connector

def connection_databasae():
    try:
        db_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4",
            database="db1"
        )
        return db_connect
        # cr_create = db_connect.cursor()

        # if cr_create:
            # print("Connection successfull")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    # finally:
        # db_connect.close()
        # cr_create.close()

connection_databasae()