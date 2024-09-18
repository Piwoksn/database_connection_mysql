import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    db = "mccoy",
    user = "root",
    passwd = input("Enter Password: ")
)

cursor = db.cursor()

statement = "SELECT * FROM People"

cursor.execute(statement)

output = cursor.fetchall()

for i in output:
    print(i)