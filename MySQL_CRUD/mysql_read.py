import sys
import MySQLdb


try:
    conn = MySQLdb.connect(host="localhost",
                           user="user1",
                           passwd="password1",
                           db="shop")
except MySQLdb.Error:
    print("Connection with Base Data error!")
    sys.exit(1)
cursor = conn.cursor()
try:
    cursor.execute("SELECT * from products")
    print("Product ID\tProduct Name\tQuantity\tPrice")
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2], row[3]))
except MySQLdb.Error:
    print("error in fetching(выборка) rows")
    sys.exit(1)

print("Second variant")
try:
    cursor.execute("SELECT * from products")
    print("Product ID\tProduct Name\tQuantity\tPrice")
    rows = cursor.fetchall()
    for row in rows:
        print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2],row[3]))
except MySQLdb.Error:
    print("Error fetching rows")
    sys.exit(1)

cursor.close()
conn.close()