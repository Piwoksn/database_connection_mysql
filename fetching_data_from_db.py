import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = input("Enter Password: "),
    db = "mccoy",
)

cursor = db.cursor()

statement = "SELECT * FROM People"

cursor.execute(statement)

output = cursor.fetchall()

for i in output:
    print(i)