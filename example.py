import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on conditions
cursor.execute("SELECT * FROM  events WHERE date='2099.12.25'")
rows = cursor.fetchall()
print(rows)

# Query specific data columns based on conditions
cursor.execute("SELECT band,date FROM  events WHERE date='2099.12.25'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cat city', '2088.11.22'),
            ('Cats', 'Cat city', '2088.11.23')]
cursor.executemany("INSERT into events values(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM  events")
rows = cursor.fetchall()
print(rows)