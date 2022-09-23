from zipfile import ZipFile

def str_file_size(item):
    units = ['KB', 'MB', 'GB']
    size_unit = 'B'
    size = item.file_size

    for i in range(3):
        if size < 1024:
            break
        else:
            size /= 1024
            size_unit = units[i]
            
    return f'{size:.0f} {size_unit}'

with ZipFile('C:/Temp/desktop.zip') as zip:
    info = zip.infolist()
    for i in info:
        name = i.filename
        indent = '  ' * (name.count('/') - (1 if i.is_dir() else 0))
        str_size = '' if i.is_dir() else ' ' + str_file_size(i)
        out_name = name.split('/')[-2 if i.is_dir() else -1] + str_size
        print(indent, out_name, sep='')
        