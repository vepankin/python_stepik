import json

data = {1: 'Timur', False: 'Arthur', None: 'Ruslan', 2: True, 3: None}
json_data = json.dumps(data)
print(json_data)

data = {'1': 'Timur', 'False': 'Arthur', 'None': 'Ruslan', '2': 'True', '3': None}
json_data = json.dumps(data, indent=3, sort_keys=True)
print(json_data)

data = json.loads(json_data)
print(data)

data = json.loads('{"1": "Timur"}')
print(data)
data = json.loads('{"1": "Timur", "1": "Bob"}')
print(data)



colors = ['black', 'white']
colors_json = json.dumps(colors, indent='-> ')
print(colors_json)