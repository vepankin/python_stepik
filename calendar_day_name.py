import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

for name in calendar.day_name:
    print(name.title())

