import sys
import MySQLdb

conn = MySQLdb.connect(host="localhost",
                       user="user1",
                       passwd="password1",
                       db="shop")
cursor = conn.cursor()
try:
    cursor.execute("""
    create table users (id int primary key,
    firstName varchar(20),
    lastName varchar(30),
    password varchar(12))
    """)
except MySQLdb.OperationalError:
    print("Table 'users' already exists")
    sys.exit(1)

cursor.close()
conn.commit()
conn.close()


