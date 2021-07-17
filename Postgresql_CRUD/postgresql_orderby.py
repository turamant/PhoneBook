import sys
import psycopg2

def connection_DB():
    conn = psycopg2.connect(database="shopdb",
                            user="user1",
                            password="password1",
                            host="127.0.0.1"
                            )
    return conn

def view_orderby(column):
    try:
        cursor.execute("SELECT * from Products2 order by %s" % column)
        print("Сортировка по %s " % column)
        print("Product ID\tProduct Name\tQuantity\tPrice")
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2], row[3]))
    except psycopg2.Error:
        print("error in fetching(выборка) rows")
        sys.exit(1)
    return None

def view_orderbyTwo(column):
    try:
        cursor.execute("SELECT * from Products2 order by %s" % column)
        print("Сортировка по %s " % column)
        print("Product ID\tProduct Name\tQuantity\tPrice")
        rows = cursor.fetchall()
        for row in rows:
            print("%d\t\t\t%s\t\t\t%d\t\t\t%0.2f" % (row[0], row[1], row[2],row[3]))
    except psycopg2.Error:
        print("Error fetching rows")
        sys.exit(1)
    return None

def close_DB():
    cursor.close()
    connDB.close()

if __name__=='__main__':
    connDB = connection_DB()
    cursor = connDB.cursor()
    view_orderby("id")
    view_orderbyTwo('productname')
    view_orderby("Price")
    view_orderbyTwo("Quantity")
    close_DB()