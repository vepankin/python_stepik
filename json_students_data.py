import csv
import json

with open("C:/Temp/students.json", "r", encoding="utf-8") as fin, \
        open("C:/Temp/students_data.csv", "w", encoding="utf-8", newline="") as fout:
    
    students = json.load(fin)
    flds=["name","phone"]
    data = [dict(zip(flds,[s[flds[0]],s[flds[1]]])) for s in students if s["age"]>=18 and s["progress"]>=75]
    
    writer = csv.DictWriter(fout, fieldnames=flds)
    writer.writeheader()
    writer.writerows(sorted(data, key=lambda x: x[flds[0]]))