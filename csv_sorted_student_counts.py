import csv

with open('C:/Temp/student_counts.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    columns = reader.fieldnames
    data = list(reader)
    
    columns.remove('year')
    columns.sort(key=lambda x: (int((b := x.split('-'))[0]), b[1]))
    columns.insert(0, 'year')

with open('C:/Temp/sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as csv_new_file:
    writer = csv.DictWriter(csv_new_file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)