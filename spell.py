def spell(*words):
    first_chars = {w[0].lower() for w in words} 
    return {c: max(list(filter(lambda x: x[0].lower() == c, words)), key=lambda x: len(x)) for c in first_chars}

print(spell('1', '2', '3', '4', '5', '6'))

#