from zipfile import ZipFile

with ZipFile('C:/Temp/test.zip') as zip_file:
    zip_file.extract('test/Картинки/avatar.png', 'C:/Temp/avatar.png')
    zip_file.extract('test/Картинки/certificate.png', 'C:/Temp/certificate.png')