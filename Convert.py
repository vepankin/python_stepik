def convert(s):
    if sum([1 if c.islower() else -1 for c in s if c.isalpha()]) < 0:
        print(s.upper())
    else:    
        print(s.lower())

convert('abcDEF')