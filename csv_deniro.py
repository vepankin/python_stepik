import csv

n = 3

with open('C:/Temp/deniro.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=','))
    n -= 1
    isalldigit = all([x[n].isdigit() for x in rows])
    for row in sorted(rows, key=lambda x: int(x[n]) if isalldigit else x[n]):
        print(*row, sep=',')
