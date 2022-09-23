import csv
from datetime import datetime

with open('C:/Temp/name_log.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file))
    dicdata = {}
    for row in rows[1:]:
        dt = datetime.strptime(row[2], '%d/%m/%Y %H:%M')
        k = row[1]
        v = dicdata.get(k)
        if v is None or dt > v[2]:
            dicdata[k] = [row[0], row[2], dt]

with open('C:/Temp/new_name_log.csv', 'w', encoding='utf-8', newline='') as csv_new_file:
    writer = csv.writer(csv_new_file)
    writer.writerow(rows[0])
    for row in sorted(dicdata.items()):
        writer.writerow((row[1][0], row[0], row[1][1]))