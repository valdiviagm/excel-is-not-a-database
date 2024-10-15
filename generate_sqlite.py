import sqlite3
import random
from datetime import datetime, timedelta

num_rows = 10000000  # Adjust this number to control the size of the database

statuses = ['pass', 'fail', 'unknown']
start_date = datetime(2020, 1, 1)

conn = sqlite3.connect('large_data.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE data (
    id INTEGER PRIMARY KEY,
    date TEXT,
    status TEXT,
    value REAL
)
''')

batch_size = 10000
data = []

for i in range(num_rows):
    date = start_date + timedelta(days=random.randint(0, 1000))
    status = random.choice(statuses)
    value = random.uniform(0, 1000)
    data.append((i, date.strftime('%Y-%m-%d'), status, value))
    if len(data) >= batch_size:
        c.executemany('INSERT INTO data VALUES (?, ?, ?, ?)', data)
        conn.commit()
        data = []
        if (i + 1) % 1000000 == 0:
            print(f"Inserted {i + 1} of {num_rows} rows ({((i + 1) / num_rows) * 100:.2f}%)")

# Insert any remaining data
if data:
    c.executemany('INSERT INTO data VALUES (?, ?, ?, ?)', data)
    conn.commit()

print("Data generation complete.")
conn.close()
