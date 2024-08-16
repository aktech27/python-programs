import mysql.connector
import pandas as pd

df=pd.read_csv(r"test.csv")
print(df)
print(df.dtypes[0])
AKDB=mysql.connector.connect(host="localhost",user="testpy",password="12345678")

cursor=AKDB.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS ak_db")
cursor.execute("USE ak_db")
cursor.execute("CREATE TABLE IF NOT EXISTS tbl1(NAME VARCHAR(255))")

sqltx="CREATE TABLE IF NOT EXISTS tbl2("+""

#cursor.execute("CREATE TABLE IF NOT EXISTS tbl2(NAME VARCHAR(255))")


cursor.executemany("INSERT INTO tbl1 VALUES(%s)",[("KEETHIR",),("AHAMED",),("KABEER",)])

cursor.execute("SELECT * FROM tbl1")

for i in cursor.fetchall():
    print(i)
