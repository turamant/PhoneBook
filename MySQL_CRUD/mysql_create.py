import sys

import MySQLdb, mariadb

try:
    conn = mariadb.connect(host="localhost",
                           user="user1",
                           passwd="password1",
                           db="shop")
except mariadb.Error:
    print("Erorr in establishing connection with 'base data'")
    sys.exit(1)
cursor = conn.cursor()
k = "YES"
while k.upper() == "YES":
    pid = int(input("Enter Product ID: "))
    pname = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))
    try:
        cursor.execute("""
        INSERT INTO products (prod_id, prod_name, quantity, price)
        VALUES (%d, '%s', %d, %f)
        """ % (pid, pname, qty, price))
        conn.commit()
        print("продукт успешно добавлен в базу данных!")
        k = input("Want to insert more products, yes/no: ")
    except:
        conn.rollback()
        sys.exit(1)
cursor.close()
conn.close()