import sqlite3

connection = sqlite3.connect("activity_tracker.db")
cursor = connection.cursor()

create_table_activities = 'CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, date TEXT, type TEXT, distance REAL, duration REAL, average_speed REAL, additional_info TEXT)'

cursor.execute(create_table_activities)

activity_insert = 'INSERT INTO activities VALUES (?, ?, ?, ?, ?, ?, ?)'

cursor.execute(activity_insert, (1, '2020-02-24', 'run', 10, 60, 10, 'indoor'))

connection.commit()

