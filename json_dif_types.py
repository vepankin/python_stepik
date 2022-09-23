import json

updated_data = []

with open("C:/Temp/data_dif_types.json", "r", encoding="utf-8") as json_file:
    data = json.loads(json_file.read())
    for v in data:
        if isinstance(v, str):
            updated_data.append(v + "!")
        elif isinstance(v, bool):
            updated_data.append(not v)
        elif isinstance(v, int):
            updated_data.append(v + 1)            
        elif isinstance(v, list):
            updated_data.append(v * 2)
        elif isinstance(v, dict):
            d = v.copy()
            d.update({"newkey": None})
            updated_data.append(d)

                    
with open("C:/Temp/updated_data.json", "w", encoding="utf-8") as json_file:
    json.dump(updated_data, json_file, indent=3)