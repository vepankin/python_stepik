import locale
from datetime import date

florida_hurricane_dates = [date(2022, 8, 18)]

# ����������� ����� ������ ���� ������� � ���������� first_date
first_date = min(florida_hurricane_dates)

# ������������ ���� � ISO � RU ������
iso = '���� ������� ������� � ISO �������: ' + first_date.isoformat()

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
ru = '���� ������� ������� � RU �������: ' + first_date.strftime('%x')

locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
us = '���� ������� ������� � US �������: ' + first_date.strftime('%x')

print(iso)
print(ru)
print(us)