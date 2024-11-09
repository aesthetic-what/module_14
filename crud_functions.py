import sqlite3
import random

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                                                     title TEXT NOT NULL,
#                                                     description TEXT,
#                                                     price INTEGER NOT NULL)""")

# for num in range(1,5):
#     title = f'Product{num}'
#     description = f'Description{num}'
#     price = random.randint(100, 1000)
#     cursor.execute("""INSERT INTO Products (title, description, price) VALUES (?, ?, ?)""", (title, description, price))


# for num in range(1, 11):
#     new_balance = 500
#     cursor.execute("""UPDATE Users SET balance=(?) WHERE id % 2 = 1""", (new_balance, ))
# conn.commit()

# cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

data = cursor.execute("""SELECT title, description, price FROM Products""").fetchall()
for row in data:
    username, email, age = row
    print(f'title: {username} | description: {email} | price: {age}')
conn.commit()


def get_all_products():
    with conn:
        return cursor.execute("""SELECT title, description, price FROM Products""").fetchall()
