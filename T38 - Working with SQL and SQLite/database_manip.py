import sqlite3

db = sqlite3.connect('python_programming_db')

cursor = db.cursor()  # Get a cursor object

# Create a new table
cursor.execute('''CREATE TABLE python_programming
                (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')

# Insert the values into the table
values = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]
db.executemany('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', values)

# Save the changes
db.commit()

# Select all records with a grade between 60 and 80.
db.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
result = cursor.fetchall()
print(result)

# Change Carl Davis’s grade to 65.
db.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"')

# Delete Dennis Fredrickson’s row.
db.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson"')

# Change the grade of all people with an id below than 55.
db.execute('UPDATE python_programming SET grade = 70 WHERE id < 55')

# Save the changes and close the connection
db.commit()
cursor.close()
