from string import \
    ascii_lowercase as lc, \
    ascii_uppercase as uc


class CaesarCipher:
    
    @staticmethod
    def shift_char(ch, offset):
        
        if ch in lc:
            i = ord(ch)-ord(lc[0])
            return lc[(i+offset)%26]
        elif ch in uc:
            i = ord(ch)-ord(uc[0])
            return uc[(i+offset)%26]
        
        return ch
    
    def __init__(self, offset: int):
        self._offset = offset
        
    def encode(self, data):
        return ''.join(self.shift_char(ch, self._offset) for ch in data)
        
    def decode(self, data):
        return ''.join(self.shift_char(ch, -self._offset) for ch in data)
            
            
cipher = CaesarCipher(5)
    
print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123