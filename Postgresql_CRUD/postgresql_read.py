import sys
import psycopg2

conn = psycopg2.connect(database="shopdb",
                        user="user1",
                        password="password1",
                        host="127.0.0.1"
                        )

cursor = conn.cursor()
try:
    cursor.execute("SELECT * from Products2")
    print("Product ID\tProduct Name\tQuantity\tPrice")
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2], row[3]))
except psycopg2.Error:
    print("error in fetching(выборка) rows")
    sys.exit(1)

print("Second variant")
try:
    cursor.execute("SELECT * from Products2")
    print("Product ID\tProduct Name\tQuantity\tPrice")
    rows = cursor.fetchall()
    for row in rows:
        print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2],row[3]))
except psycopg2.Error:
    print("Error fetching rows")
    sys.exit(1)

cursor.close()
conn.close()