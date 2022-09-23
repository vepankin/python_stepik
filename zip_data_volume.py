from zipfile import ZipFile

with ZipFile('C:/Temp/workbook.zip') as file:
    fs = 0
    cs = 0
    for f in file.infolist():
        fs += f.file_size
        cs += f.compress_size
    print(f'Объем исходных файлов: {fs} байт(а)')
    print(f'Объем сжатых файлов: {cs} байт(а)')