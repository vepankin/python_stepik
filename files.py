def get_summary_val(f_list):
    size_sum = sum(map(lambda x: x[3], f_list))

    for n, m in byte_mult.items():
        if m <= size_sum:
            size_name = n
            size_bytes = m
        else:
            break
           
    return f'{round(size_sum/size_bytes)} {size_name}'
    
d = {}
byte_mult = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}

with open('C:/Temp/files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, size, size_name = line.strip().split()
        ext = name.split('.')[1]
        byte_size = byte_mult.get(size_name, 1) * int(size)
        d.setdefault(ext, []).append([name, size, size_name, byte_size])

flag_empty_string = False
for ext in sorted(d):
    if flag_empty_string:
        print()
    else:
        flag_empty_string = True

    s_val = get_summary_val(d[ext])
    print(*sorted([f[0] for f in d[ext]]),
          '----------', f'Summary: {s_val}', sep='\n')

