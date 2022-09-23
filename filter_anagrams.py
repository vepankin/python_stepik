def filter_anagrams(word, words):

    def get_dict(w):
        return {c: w.count(c) for c in set(w)}
            
    def is_anagram(wd1, w):
        if set(word) == set(w) and len(word) == len(w):
            wd2 = get_dict(w)
            return min([wd1[c]==wd2[c] for c in set(w)])
        else:
            return False

    wd = get_dict(word)
    
    return [w for w in words if is_anagram(wd, w)]

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))