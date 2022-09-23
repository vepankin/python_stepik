def choose_plural(amount, declensions):
    i = 0
    d = amount%10
    dd = amount % 100
    if d == 0 or 5 <= d <= 9 or dd in (11, 12, 13, 14):
        i = 2
    elif 2 <= d < 5:
            i = 1
        
    return '{} {}'.format(amount, declensions[i])

print(choose_plural(512312, ('цент', 'цента', 'центов')))