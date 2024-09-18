import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    db = "mccoy",
    user = "root",
    passwd = input("Enter Password: ")
)

cursor = db.cursor()

statement = "UPDATE People SET Location = 'USA' where Name= 'Noble Piwoks'"

cursor.execute(statement)
db.commit()