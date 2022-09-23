import calendar
from datetime import date

def foo(strArg):
    strArg = 'new value'

s = '-=string=-'
foo(s)
print(s)


def get_all_mondays(year):
    return [date(year, m, w[0]) for m in range(1, 13) for w in calendar.monthcalendar(year, m) if w[0]]

print(*get_all_mondays(2022), sep='\n')