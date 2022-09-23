import csv

with open('C:/Temp/sales.csv', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    for row in rows:
        if float(row['old_price']) > float(row['new_price']):
            print(row['name'])