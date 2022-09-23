import csv

with open('C:/Temp/prices.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    data = list(reader)

min_price = None
min_data = []

for row in data:
    shop = row.pop('Магазин')
    shop_min_price = int(min(row.values(), key=int))
    shop_min_product = min([k for k, v in row.items() if int(v) == shop_min_price])

    if min_price is None:
        min_price = shop_min_price

    if shop_min_price < min_price:
        min_data.clear()
        min_price = shop_min_price

    if shop_min_price <= min_price:
        min_data.append([shop, shop_min_product, shop_min_price])

min_product = min([x[1] for x in min_data])
min_shop = min(x[0] for x in min_data if x[1] == min_product)

print(min_product, min_shop, sep=': ')