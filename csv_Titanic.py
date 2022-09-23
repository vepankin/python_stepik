import csv

with open('C:/Temp/titanic.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))
    del rows[0]
    data = [ (v[1], v[2], i) for i, v in enumerate(rows) if v[0]=='1' and float(v[3]) < 18]

    for row in sorted(data, key=lambda x: (0 if x[1] == 'male' else 1, x[2])):
        print(row[0])