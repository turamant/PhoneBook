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
p = int(input("Enter Product ID: "))
cursor.execute("SELECT * from products where prod_id=%d" % p)
row = cursor.fetchone()
if row == None:
    print("Нет такого ID  в таблице")
else:
    print("Есть такая информайия о продукте с ID %d :" % p)
    print("Product ID\tProduct Name\tQuantity\tPrice")
    print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2], row[3]))
    k = input("Подтвердите что хотите удалить эту запись, yes/no: ")
    if k.upper() == "YES":
        cursor.execute("DELETE from products where prod_id=%d" % p)
        print("Продукт с номером ID %d удален!" % p)
    cursor.close()
    conn.commit()
    conn.close()