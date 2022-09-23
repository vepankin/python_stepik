from datetime import datetime
from zipfile import ZipFile

def get_strdt(info_item):
    return datetime(*info_item.date_time).isoformat(sep=' ')

def get_name(info_item):
    return info_item.filename.split('/')[-1]

with ZipFile('C:/Temp/workbook.zip') as file:
    flag = True
    for el in sorted([[get_name(i), get_strdt(i), i.file_size, i.compress_size] for i in file.infolist() if not i.is_dir()], key=lambda x: x[0].upper()):
        if flag:
            flag = False
        else:
            print('') #empty string
        print(el[0])    
        print(f'  Дата модификации файла: {el[1]}')     
        print(f'  Объем исходного файла: {el[2]} байт(а)')
        print(f'  Объем сжатого файла: {el[3]} байт(а)')