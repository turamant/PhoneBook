import sqlite3

def login(login, passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    #Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw: # кортеж [(id, login, password),]
        signal.emit('Успешно авторизован! Добро пожаловать!')
    else:
        signal.emit("Введенная комбинация админ и пароль не существует!")

    cur.close()
    con.close()

def register(login, passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    #Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой логин уже используется!')
    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit("Вы успешно зарегистрированы!")
        con.commit()

    cur.close()
    con.close()