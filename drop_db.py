def delete_db():
    import mysql.connector

    drop_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ConVox@4"
    )

    cr_create = drop_db.cursor()

    cr_create.execute("DROP DATABASE db2;")

    if cr_create:
        print("database deleted")
    else:
        print("Database not deleted")

delete_db()