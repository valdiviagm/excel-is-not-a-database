import csv

count = 0
with open('large_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['status'] == 'fail' and float(row['value']) > 500:
            count += 1
print(f"Number of rows where status='fail' and value > 500: {count}")
