def dbconnection():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",        
        user="root",     
        password="ConVox@4", 
        database="db1" 
    )
    
    if(mydb):
        print("Connection successfull")
    else:
        print("connection failied")

dbconnection()