def db_create():
    import mysql.connector
    create_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = 'ConVox@4'
    )

    cr_cursor = create_db.cursor()

    cr_cursor.execute("CREATE DATABASE db1")

    if cr_cursor:
        print("Database created")
    else:
        print("Database not created")

db_create()