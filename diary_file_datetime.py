from datetime import datetime

diary = {}
key = None

with open('C:/Temp/diary.txt', 'r', encoding='utf-8') as file:
    for line in file:

        if line == '\n':
            continue
        
        try:
            key = datetime.strptime(line, '%d.%m.%Y; %H:%M\n')
        except:
            pass
        
        diary[key] = diary.setdefault(key, '') + line
            
print(*[diary[k].rstrip('\n') for k in sorted(diary)], sep='\n\n')
