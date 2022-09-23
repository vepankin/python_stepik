from zipfile import ZipFile

with ZipFile('C:/Temp/workbook.zip') as zfile:
    info = zfile.infolist()
    print(sum(map(lambda x: 0 if x.is_dir() else 1, info)))