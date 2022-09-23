from datetime import datetime
from zipfile import ZipFile

def get_dt(info_item):
    return datetime(*info_item.date_time)

def get_name(info_item):
    return info_item.filename.split('/')[-1]

dt = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
print(dt.isoformat(sep=' '))

with ZipFile('C:/Temp/workbook.zip') as file:
    info = [get_name(i) for i in file.infolist() if not i.is_dir() and get_dt(i) > dt]
    print(*sorted(info), sep='\n')