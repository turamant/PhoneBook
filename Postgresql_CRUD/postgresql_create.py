import sys
import psycopg2

try:
    conn = psycopg2.connect(database="studentdb",
                            user="user1",
                            password="password1",
                            host="127.0.0.1"
                            )
except psycopg2.Error:
    print("Erorr in establishing connection with 'base data'")
    sys.exit(1)
print("Ok basa")
cursor = conn.cursor()
k = "YES"
while k.upper() == "YES":
    pid = int(input("Enter ID: "))
    family = input("Enter Family: ")
    rank = input("Enter Rank: ")
    try:
        cursor.execute("""
        INSERT INTO student (id, family, rank)
        VALUES (%d, '%s', '%s')
        """ % (pid, family, rank))
        conn.commit()
        print("студент успешно добавлен в базу данных!")
        k = input("Хотите добавить еще одного студента yes/no: ")
    except:
        conn.rollback()
        sys.exit(1)
cursor.close()
conn.close()