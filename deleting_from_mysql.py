import mysql.connector as mysql
from getpass import getpass

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = getpass("Enter Password: "),
    db = "mccoy"
)

cursor = db.cursor()

statement = "DELETE FROM People where Name= 'Noble Piwoks'"

cursor.execute(statement)

db.commit()

print("Row(s) deleted")