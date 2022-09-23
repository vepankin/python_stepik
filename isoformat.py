from datetime import date, time
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_date = date(2021, 12, 31)
my_time = time(21, 15, 17)

# ��������������� ����� ���� � ������� �����������
print(my_date.strftime("%A %d, %B %Y"))

print('����: ' + my_date.isoformat())
print('�����: ' + my_time.isoformat())

my_date = date(2019, 2, 4)
print(my_date)
