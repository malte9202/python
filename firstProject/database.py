import sqlite3

connection = sqlite3.connect("sqlite3_tutorial.db")
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, name TEXT)')

cursor.execute('INSERT INTO names VALUES (?, ?)', (1, 'Elena'))

connection.commit()