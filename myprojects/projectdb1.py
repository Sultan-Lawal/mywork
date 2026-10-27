import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "orderdb"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE orderdb")


# mycursor.execute("show databases")
# for db in mycursor:
#      print(db)