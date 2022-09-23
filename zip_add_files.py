from zipfile import ZipFile

with ZipFile('C:/Temp/test_zip.zip', mode='a') as zip_file:
    zip_file.write('C:/Temp/pools.json', 'test/pools.json')
    zip_file.write('C:/Temp/best_scores.json', 'best_scores.json')
    print(*zip_file.namelist(), sep='\n')