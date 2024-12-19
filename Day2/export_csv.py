from connection import *
import csv 

def export_csv():
    try:
        connection = connection_databasae()

        if connection is None:
            print("Connection failed")
        
        cr_create = connection.cursor()

        qry = "SELECT * FROM table2"

        cr_create.execute(qry)

        rows = cr_create.fetchall()

        with open('csv/table2.csv','w',newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['id','name','email','time_date'])

            for row in rows:
                writer.writerow(row)
        print("Data successfully exported to CSV")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cr_create.close()
export_csv()