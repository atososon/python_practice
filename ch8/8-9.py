import sqlite3
db = sqlite3.connect("books.db")
for row in db.execute('select * from book order by year'):
    print(*row, sep = ', ')