import csv

with open('C:/Temp/salary_data.csv', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    data = {}
    for i, row in enumerate(rows):
        name = row['company_name']
        salary = int(row['salary'])
        data.setdefault(name, {'idx': i, 'salary': []})['salary'].append(salary)

    print(*[k[0] for k in sorted(data.items(), key=lambda x: (sum(x[1]['salary']) / len(x[1]['salary']), x[1]['idx']))], sep='\n')