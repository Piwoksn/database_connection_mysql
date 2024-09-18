import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    db = "mccoy",
    user= "root",
    passwd= input("Please Enter Password: ")
)

if db.is_connected:
    print("Databae is connected")
    
    cursor = db.cursor()
    # Created database Peple
    cursor.execute(
        "CREATE TABLE People (Name varchar(50), Age int,Location varchar(50))"
    )
    
else:
    print("Not Connected")
