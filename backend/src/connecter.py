import mysql.connector

db = mysql.connector.connect(
    user="",
    password="",
    host="",
    database=""
)

cursor = db.cursor()
