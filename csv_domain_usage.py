import csv

with open('C:/Temp/data.csv', encoding='utf-8') as csv_data_file:
    rows = csv.DictReader(csv_data_file)
    dicdata = {}
    for row in rows:
        k = row['email'].split('@')[1]
        dicdata[k] = dicdata.get(k, 0) + 1

with open('C:/Temp/domain_usage.csv', 'w', encoding='utf-8', newline='') as csv_usage_file:
    writer = csv.writer(csv_usage_file, delimiter=',')
    columns = ['domain', 'count']
    writer.writerow(columns)
    for row in sorted(dicdata.items(), key=lambda x: (x[1], x[0])):
        writer.writerow(row)