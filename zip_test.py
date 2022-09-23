from zipfile import ZipFile
from datetime import datetime

with ZipFile('C:/Temp/test.zip') as zip_file:
    #1
    #zip_file.printdir()
    
    #2
    info = zip_file.infolist()
    print(info[6].file_size)                # размер начального файла в байтах
    print(info[6].compress_size)            # размер сжатого файла в байтах
    print(info[6].filename)                 # имя файла
    print(datetime(*info[6].date_time))     # дата изменения файла

    print(info[0].is_dir())
    print(info[6].is_dir())

    print('-' * 40)

    info = zip_file.namelist()                # получаем названия всех файлов архива
    print(*info, sep='\n')

    print('-' * 40)

    last_file = zip_file.getinfo(info[-1])    # получаем информацию об отдельном файле
    print(last_file.file_size)
    print(last_file.compress_size)
    print(last_file.filename)
    print(last_file.date_time)

    print('-' * 40)
     
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read()) # Метод ZipFile.open() открывает файл именно в бинарном виде, не в текстовом
                           # возвращает сырые байты(тип bytes)
        print('-' * 40)

        file.seek(0)
        print(file.read().decode('utf-8')) # Метод ZipFile.open() открывает файл именно в бинарном виде, не в текстовом
        