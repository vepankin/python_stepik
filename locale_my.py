import locale
from datetime import date

florida_hurricane_dates = [date(2022, 8, 18)]

# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%x')

locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%x')

print(iso)
print(ru)
print(us)