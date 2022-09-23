import csv

with open('C:/temp/products.csv', encoding='utf-8') as file:
    #rows1 = csv.DictReader(file)
    #print(rows1)

    rows = csv.reader(file, delimiter=';', quotechar='"')
    for index, row in enumerate(rows):
        if index > 5:
            break
        elif index > 0:
            print(row)