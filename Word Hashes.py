################################################################################
# Match all words in a document against an name dictionary and anonymize them
# using a hash.
import hashlib
import re

def anonymise(text: str, dictionary: list) -> str:
    hashes = {
        word: hashlib.sha512(word.encode()).hexdigest() for word in dictionary}

    current_word = ''
    anon_text = ''

    for char in text:
        if char in " .:;-\r\n":
            if current_word in hashes:
                anon_text += hashes[current_word]
            else:
                anon_text += current_word

            anon_text += char
            current_word = ''

        else:
            current_word += char

    return anon_text

print(anonymise("bar \nfoobar foo bar.", ["foo"]))

