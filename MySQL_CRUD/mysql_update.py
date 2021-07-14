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
print("Сделаем редактирование данных товара")

pname = input("Введите новое имя Product Name: ")
qty = int(input("Введите новое количество товара Quantity: "))
price = int(input("введите новую цену товара Price: "))
cursor.execute("UPDATE products set prod_name='%s', quantity=%d, price=%f where prod_id=%d" % (pname, qty, price, p))
cursor.close()
conn.commit()
print("Изменения проведены успешно для ID: %d" % p)
conn.close()