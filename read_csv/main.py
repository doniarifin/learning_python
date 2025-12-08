import pandas as pd
import mysql.connector

data = pd.read_csv("customers_100.csv")

df = pd.DataFrame(data)

#clean data
df_dropna = df.dropna()

print(df.isnull().sum())
print(df_dropna)

# connect db
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  ssl_disabled=True
)

if db.is_connected:
  print("mysql connected!")


cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS customers_csv")

#create table customers
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="customers_csv",
  ssl_disabled=True
)

cursor = db.cursor()

sql = """
  CREATE TABLE IF NOT EXISTS clean_customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(100),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    company VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    phone_1 VARCHAR(100),
    phone_2 VARCHAR(100),
    email VARCHAR(100),
    subscription_date DATE,
    website VARCHAR(100)
  )
"""
cursor.execute(sql)

#insert csv data to table
sql = """
  INSERT INTO clean_customers (customer_id, first_name, last_name, company, city, country, phone_1, phone_2, email, subscription_date, website) 
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
"""

values = [
  (
    row["Customer Id"], row["First Name"], row["Last Name"], row["Company"], row["City"], row["Country"], row["Phone 1"], row["Phone 2"], row["Email"],
    row["Subscription Date"], row["Website"]
  )
    for _, row in df_dropna.iterrows()
]

cursor.executemany(sql, values)

cursor.execute("SELECT * FROM clean_customers")

rows = cursor.fetchall()

print(rows)

#commit to db
db.commit()
db.close()