import pandas as pd
import snowflake.connector

data = pd.read_csv("../csv/customers_100.csv")

df = pd.DataFrame(data)

#clean data
df_dropna = df.dropna()

conn = snowflake.connector.connect(
    user="***REMOVED***",
    password="***REMOVED***",
    account="***REMOVED***",
    warehouse="COMPUTE_WH",
    database="LEARNING_DB",
    schema="RAW",
    role="ACCOUNTADMIN"
)

cursor = conn.cursor()
cursor.execute("SELECT CURRENT_VERSION();")
result = cursor.fetchone()

print("Connected to Snowflake!")
print("Snowflake version:", result[0])

#create table
sql = """
  CREATE TABLE IF NOT EXISTS customers (
    id INT AUTOINCREMENT,
    customer_id STRING,
    first_name STRING,
    last_name STRING,
    company STRING,
    city STRING,
    country STRING,
    phone_1 STRING,
    phone_2 STRING,
    email STRING,
    subscription_date DATE,
    website STRING
  )
"""

cursor.execute(sql)

#insert csv data to table
sql = """
  INSERT INTO customers (customer_id, first_name, last_name, company, city, country, phone_1, phone_2, email, subscription_date, website) 
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

cursor.execute("SELECT * FROM customers")

cursor.close()
conn.close()