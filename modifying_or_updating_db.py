import mysql.connector as mysql
from getpass import getpass

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = getpass("Enter Password: "),
    db = "mccoy",
)

cursor = db.cursor()

statement = "UPDATE People SET Location = 'USA' where Name= 'Noble Piwoks'"

cursor.execute(statement)
db.commit()