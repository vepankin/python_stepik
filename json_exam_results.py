import csv
import json
from datetime import datetime

with open("C:/Temp/exam_results.csv", "r", encoding="utf-8") as fin, \
        open("C:/Temp/best_scores.json", "w", encoding="utf-8") as fout:

    best_scores = {}
    rfields = ['name', 'surname', 'best_score', 'date_and_time', 'email']
    results = csv.DictReader(fin)
    
    for r in results:
        r['score'] = int(r['score'])
        key = (r['name'], r['surname'])
        bs = best_scores.setdefault(key)

        if bs == None:
            best_scores[key] = dict(zip(rfields, r.values()))
        elif r['score'] > bs['best_score']:    
            bs['best_score'] = r['score']
            bs['date_and_time'] = r['date_and_time']
        elif r['score'] == bs['best_score']:
            rdt = datetime.fromisoformat(r['date_and_time'])
            bsdt = datetime.fromisoformat(bs['date_and_time'])
            if rdt > bsdt:
                bs['date_and_time'] = r['date_and_time']

    json.dump(sorted(best_scores.values(), key=lambda x: x['email']), fout, indent=3)