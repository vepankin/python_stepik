def get_biggest(numbers):

    def biggest_sort(r):
        for max_idx in range(len(r) - 1, 0, -1):
            for i in range(max_idx):
                if r[i] + r[i + 1] < r[i + 1] + r[i]:
                    r[i], r[i + 1] = r[i + 1], r[i]

    if numbers:
        str_list = list(map(str, numbers))
        first_digits = {s[0] for s in str_list}
        d = {fd: [s for s in str_list if s[0] == fd] for fd in first_digits}

        for k, v in d.items():
            max_len = max(map(len, v))
            biggest_sort(d[k])
            d[k] = ''.join(v)

        l = list(d.values())
        biggest_sort(l)
        return int(''.join(l))
    else:
        return -1


print(get_biggest([3, 1, 2]))