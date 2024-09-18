import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    db = "mccoy",
    user= "root",
    passwd= input("Please Enter Password")
)


