import sqlite3

conn = sqlite3.connect('large_data.db')
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM data WHERE status = 'fail' AND value > 500")
count = c.fetchone()[0]
print(f"Number of rows where status='fail' and value > 500: {count}")

conn.close()
