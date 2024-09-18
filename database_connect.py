import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    database="mccoy",  # Use 'database' instead of 'db'
    user="root",
    passwd=input("Please Enter Password: ")
)

if db.is_connected():
    print("Database is connected")
    
    cursor = db.cursor()
    
    try:
        # Insert data into the table
        cursor.execute(
            "INSERT INTO People (Name, Age, Location) VALUES (%s, %s, %s), (%s, %s, %s);",
            ('Justice Piwoks', 31, 'Port harcourt', 'Surely Piwoks', 25, 'Delta')
        )
        db.commit()  # Commit the transaction
        print("Data inserted successfully")
        
    except mysql.Error as err:
        print(f"Error: {err}")
        
    finally:
        cursor.close()
        db.close()
else:
    print("Not Connected")
