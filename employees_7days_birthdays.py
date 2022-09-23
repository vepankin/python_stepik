from datetime import datetime, timedelta

start = datetime.strptime('29.12.2021', '%d.%m.%Y')
emp = [[], datetime(1, 1, 1)]
bdlst = [(d.day, d.month) for d in [start + timedelta(days=i) for i in range(1, 8)]]

data = ['Иван Петров 30.12.1995', 'Петр Сергеев 04.01.1997', 'Сергей Романов 03.01.1994', 'Маша Иванова 31.12.1996']

for i in range(4):
    *name, sdt = data[i].split()
    dt = datetime.strptime(sdt, '%d.%m.%Y')
    if (dt.day, dt.month) in bdlst:
        if dt > emp[1]:
            *emp, = name, dt

if emp[0]:
    print(*emp[0])
else:    
    print('Дни рождения не планируются')