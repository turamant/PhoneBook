import sys
import MySQLdb

conn = MySQLdb.connect(host="localhost",
                       user="user1",
                       passwd="password1",
                       db="shop")
cursor = conn.cursor()
try:
    cursor.execute("""
    create table phonebook (id int primary key,
    firstName varchar(20),
    lastName varchar(30),
    telNumber varchar(12),
    address varchar(30))
    """)
except MySQLdb.OperationalError:
    print("Table 'products' already exists")
    sys.exit(1)

cursor.close()
conn.commit()
conn.close()


