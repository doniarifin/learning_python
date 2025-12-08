import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  ssl_disabled=True
)

if db.is_connected:
  print("mysql connected!")

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS python_app")
print("database created successfully!")

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python_app",
  ssl_disabled=True
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

query = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = "Doni", "Jember"

query2 = "INSERT INTO users (name, address) VALUES (%s, %s)"
val2 = "Arifin", "Surabaya"

cursor.execute(query, val)
cursor.execute(query2, val2)

query = "UPDATE users SET name = 'Doni 2' WHERE name = 'Doni'"
cursor.execute(query)

query = "DELETE FROM users WHERE name = 'Arifin' "
cursor.execute(query)

query = "SELECT * FROM users"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
  print(row)

db.commit()
db.close()