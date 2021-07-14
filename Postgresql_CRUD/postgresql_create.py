import sys
import psycopg2

try:
    conn = psycopg2.connect(database="shopdb",
                            user="user1",
                            password="password1",
                            host="127.0.0.1"
                            )
except psycopg2.Error:
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
        INSERT INTO Products2 (id, productname, quantity, price)
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