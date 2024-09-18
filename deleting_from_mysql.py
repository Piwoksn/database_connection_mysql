import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = input("Enter Password: "),
    db = "mccoy"
)

cursor = db.cursor()

statement = "DELETE FROM People where Name= 'Noble Piwoks'"

cursor.execute(statement)

db.commit()

print("Row(s) deleted")