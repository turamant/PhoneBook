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
print("Сделаем редактирование данных товара")

pname = input("Введите новое имя Product Name: ")
qty = int(input("Введите новое количество товара Quantity: "))
price = int(input("введите новую цену товара Price: "))
cursor.execute("UPDATE Products2 set productname='%s', quantity=%d, price=%f where id=%d" % (pname, qty, price, p))
cursor.close()
conn.commit()
print("Изменения проведены успешно для ID: %d" % p)
conn.close()