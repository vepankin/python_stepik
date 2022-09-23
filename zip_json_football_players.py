import json
from zipfile import ZipFile

def is_correct_json(string):
    try:
        jdata = json.loads(string)
        return True
    except:
        return False
    
with ZipFile('C:/Temp/data_arsenal.zip') as zip:
    l = []

    for inf in zip.infolist():
        fname = inf.filename
        
        if not inf.is_dir() and fname[-5:].lower() == '.json':
            with zip.open(fname) as jfile:
                try:
                    s = jfile.read().decode('utf-8')
                except:
                    continue
                
                if is_correct_json(s):
                    jdata = json.loads(s)

                    if jdata['team'] == 'Arsenal':
                        n = f'{jdata["first_name"]} {jdata["last_name"]}'
                        l.append(n)
         
    print(*sorted(l), sep='\n')
