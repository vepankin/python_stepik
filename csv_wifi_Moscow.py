import csv

with open('C:/Temp/wifi.csv', encoding='utf-8') as csv_data_file:
    rows = csv.DictReader(csv_data_file, delimiter=';')
    data = {}
    for row in rows:
        k = row['district']
        data[k] = data.get(k, 0) + int(row['number_of_access_points'])

    for row in sorted(data.items(), key=lambda x: (-x[1], x[0])):
        print(*row, sep=': ')