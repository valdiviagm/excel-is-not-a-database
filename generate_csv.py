import csv
import random
from datetime import datetime, timedelta

num_rows = 10000000  # Adjust this number to control the size of the CSV file

statuses = ['pass', 'fail', 'unknown']
start_date = datetime(2020, 1, 1)

with open('large_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'date', 'status', 'value'])
    for i in range(num_rows):
        date = start_date + timedelta(days=random.randint(0, 1000))
        status = random.choice(statuses)
        value = random.uniform(0, 1000)
        writer.writerow([i, date.strftime('%Y-%m-%d'), status, value])
        if (i + 1) % 1000000 == 0:
            print(f"Written {i + 1} of {num_rows} rows ({((i + 1) / num_rows) * 100:.2f}%)")
