import mysql.connector
import csv

def insertData():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4",
            database="db1"
        )
    
        cr_create = db_connection.cursor()
    
        insert_data = """
                        INSERT INTO 
                            user_form (fullname, email)
                        VALUES
                            ('dsfs', 'mfdsfdsd@gmail.com');
                       """
    
        cr_create.execute(insert_data)
        db_connection.commit()
    
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cr_create.close()
        db_connection.close()

    exportToCSV()

def exportToCSV():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4",
            database="db1"
        )

        cr_cursor = db_connection.cursor()

        select_data = "SELECT * FROM user_form"
        cr_cursor.execute(select_data)

        rows = cr_cursor.fetchall()

        with open('csv/user_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['id', 'name', 'email', 'date'])

            for row in rows:
                writer.writerow(row)

        print("Data successfully exported to CSV.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cr_cursor.close()
        db_connection.close()

insertData()
