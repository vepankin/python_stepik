from zipfile import ZipFile

def get_k(info_item):
    return info_item.compress_size / info_item.file_size * 100

def get_name(info_item):
    return info_item.filename.split('/')[-1]

with ZipFile('C:/Temp/workbook.zip') as file:
    info = [i for i in file.infolist() if not i.is_dir()]
    i = info[0]
    
    k_min, best_file = get_k(i), get_name(i)
    
    for i in info[1:]:
        k = get_k(i)
        if k < k_min:
            k_min, best_file = k, get_name(i)

    print(best_file)