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
p = int(input("Enter Product ID: "))
cursor.execute("SELECT * from Products2 where id=%d" % p)
row = cursor.fetchone()
if row == None:
    print("Нет такого ID  в таблице")
else:
    print("Есть такая информайия о продукте с ID %d :" % p)
    print("Product ID\tProduct Name\tQuantity\tPrice")
    print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2], row[3]))
    k = input("Подтвердите что хотите удалить эту запись, yes/no: ")
    if k.upper() == "YES":
        cursor.execute("DELETE from Products2 where id=%d" % p)
        print("Продукт с номером ID %d удален!" % p)
    cursor.close()
    conn.commit()
    conn.close()