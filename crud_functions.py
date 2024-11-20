import sqlite3
import random

conn = sqlite3.connect('test.db')
cursor = conn.cursor()




# for num in range(1, 11):
#     new_balance = 500
#     cursor.execute("""UPDATE Users SET balance=(?) WHERE id % 2 = 1""", (new_balance, ))
# conn.commit()

# cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

# data = cursor.execute("""SELECT title, description, price FROM Products""").fetchall()
# for row in data:
#     username, email, age = row
#     print(f'title: {username} | description: {email} | price: {age}')
# conn.commit()


    
def initiate_db():
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                    username TEXT NOT NULL,
                                                    email TEXT NOT NULL,
                                                    age INTEGER,
                                                    balance INTEGER NOT NULL)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                               title TEXT NOT NULL,
                                                               description TEXT,
                                                               price INTEGER NOT NULL)""")

def get_all_products():
    with conn:
        return cursor.execute("""SELECT title, description, price FROM Products""").fetchone()

def add_user(username, email, age):
    with conn:
        return cursor.execute("""INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)""",(username, email, age, 1000))
    
def is_include(username):
    check_user = cursor.execute("""SELECT * FROM Users WHERE username=(?)""", (username, )).fetchone()
    if check_user is None:
        return False
    conn.commit()
    return True

# initiate_db()

# for num in range(1,5):
#     title = f'Product{num}'
#     description = f'Description{num}'
#     price = random.randint(100, 1000)
#     print(title, description, price)
#     cursor.execute("""INSERT INTO Products (title, description, price) VALUES (?, ?, ?)""", (title, description, price))
# conn.commit()