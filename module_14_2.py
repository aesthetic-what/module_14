import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                    username TEXT NOT NULL,
                                                    email TEXT NOT NULL,
                                                    age INTEGER,
                                                    balance INTEGER NOT NULL)""")
conn.commit()

# for num in range(1,11):
#     user = 'User' + f'{num}'
#     email = f'example{num}@gmail.com'
#     age = num * 10
#     balance = 1000
#     cursor.execute("""INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)""", (user, email, age, balance))

for num in range(1, 10):
    new_balance = 500
    cursor.execute("""UPDATE Users SET balance=(?) WHERE id % 2 = 1""", (new_balance, ))

cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

data = cursor.execute("""SELECT username, email, age, balance FROM Users WHERE age <> 60""").fetchall()
for row in data:
    username, email, age, balance = row
    print(f'Имя: {username}| почта: {email}| возраст| {age}, баланс: {balance}')

cursor.execute("""DELETE FROM Users WHERE id = 6""")

total_users = cursor.execute("""SELECT COUNT(*) FROM Users""").fetchone()[0]
print(total_users)

sum = cursor.execute("""SELECT SUM(balance) FROM Users""").fetchone()[0]
print(sum)

avg_sum = cursor.execute("""SELECT AVG(balance) FROM Users""").fetchone()[0]
print(avg_sum)

print(sum / total_users)

conn.commit()

