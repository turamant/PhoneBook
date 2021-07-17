import sys
import psycopg2

try:
    conn = psycopg2.connect(database="studentdb",
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
    cursor.execute(""" CREATE TABLE STUDENT
    (id int primary key not null,
    family varchar(30) not null,
    rank  varchar(50) not null);
    """)
    print("Table create!")
except psycopg2.OperationalError:
    print("Table 'products' already exists")
    sys.exit(1)

cursor.close()
conn.commit()
conn.close()

