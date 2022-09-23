from datetime import datetime, time
import json

with open("C:/Temp/pools.json", "r", encoding="utf-8") as file:
    pools = json.load(file)
    best_pool = None
    for p in pools:

        print(p)
        
        if "Понедельник" in p["WorkingHoursSummer"]:
            t = p["WorkingHoursSummer"]["Понедельник"].split('-')
            t1 = datetime.strptime(t[0],'%H:%M').time()
            t2 = datetime.strptime(t[1],'%H:%M').time()

            print(t1, t2)

            if t1 <= time(10) and t2 >= time(12):
                if best_pool is None:
                    best_pool = p
                elif best_pool["DimensionsSummer"]["Length"] < p["DimensionsSummer"]["Length"]:
                    best_pool = p
                elif best_pool["DimensionsSummer"]["Length"] == p["DimensionsSummer"]["Length"] and \
                     best_pool["DimensionsSummer"]["Width"]   < p["DimensionsSummer"]["Width"]:
                    best_pool = p
    if best_pool:
        bpl = best_pool["DimensionsSummer"]["Length"]
        bpw = best_pool["DimensionsSummer"]["Width"]
        bpa = best_pool["Address"]
        print(f'{bpl}x{bpw}\n{bpa}')