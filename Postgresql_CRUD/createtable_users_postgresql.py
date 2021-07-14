import sys
import psycopg2

try:
    conn = psycopg2.connect(database="shopdb",
                            user="user1",
                            password="password1",
                            host="127.0.0.1",
                            port="5432"
                            )
    print("Coonect good!!!")
except psycopg2.Error:
    print("Erorr in establishing connection with 'base data'")
    sys.exit(1)
cursor = conn.cursor()
try:
    cursor.execute(""" CREATE TABLE USERS
    (id int primary key not null,
    firstName varchar(30) not null,
    lastName  varchar(50) not null,
    password varchar(12));
    """)
    print("Table create!")
except psycopg2.OperationalError:
    print("Table 'users' already exists")
    sys.exit(1)

cursor.close()
conn.commit()
conn.close()
