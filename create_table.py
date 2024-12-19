import mysql.connector

def create_table():
    try:
        create_table_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ConVox@4",
            database="db1"  
        )
        
        cr_create = create_table_conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS `user_form` (
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            fullname VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """

        cr_create.execute(create_table_query)
        
        create_table_conn.commit()

        print("Table created successfully")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cr_create.close()
        create_table_conn.close()

create_table()
