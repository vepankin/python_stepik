import csv

def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file)
        data = {}
        for row in rows:
            k = row[0]
            v = data.setdefault(k, {})
            v[row[1]] = row[2]

    columns = [id_name]
    columns.extend(list(data.values())[0].keys())

    with open('C:/Temp/condensed.csv', 'w', encoding='utf-8', newline='') as csv_new_file:
        writer = csv.DictWriter(csv_new_file, fieldnames=columns)
        writer.writeheader()
        for k, v in data.items():
            rdata = {id_name: k}
            rdata.update(v)
            writer.writerow(rdata)

text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('C:/Temp/data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('C:/Temp/data.csv', id_name='ID')

with open('C:/Temp/condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())
