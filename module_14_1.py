import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                    username TEXT NOT NULL,
                                                    email TEXT NOT NULL,
                                                    age INTEGER,
                                                    balance INTEGER NOT NULL)""")
conn.commit()

for num in range(1,11):
    user = 'User' + f'{num}'
    email = f'example{num}@gmail.com'
    age = num * 10
    balance = 1000
    cursor.execute("""INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)""", (user, email, age, balance))

conn.commit()

for num in range(1, 11):
    new_balance = 500
    cursor.execute("""UPDATE Users SET balance=(?) WHERE id % 2 = 1""", (new_balance, ))
conn.commit()

data = cursor.execute("""SELECT username, email, age, balance FROM Users WHERE age <> 60""").fetchall()
for row in data:
    username, email, age, balance = row
    print(f'Имя: {username}| почта: {email}| возраст| {age}, баланс: {balance}')

conn.close()
