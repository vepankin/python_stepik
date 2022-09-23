from datetime import datetime
from calendar import day_name

fridays = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # weekday:count

for y in range(1, 9999 + 1):
    for m in range(1, 13):
        wd = datetime(year=y, month=m, day=13).weekday()
        fridays[wd] += 1

for wday in range(7):
    print('{:.<11}'.format(day_name[wday]), fridays[wday], sep='')