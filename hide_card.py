s = '1234   5'
s = ''.join(s.split())
print('*' * (len(s) - 4) + s[-4:])