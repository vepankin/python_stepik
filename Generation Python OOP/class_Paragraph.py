from abc import ABC,abstractmethod 

class ABCParagraph(ABC):
    def __init__(self, length):
        self._length = length
        self._data = []
        
    def add(self, string):
        if line:= string.strip():
            if not self._data or len(self._data[-1]) == self._length:
                self._data.append('')
                
            line = (self._data[-1] + ' ' + line).strip()
            
            while line:    
                
                if len(line) <= self._length:
                    idx = self._length
                elif (idx := line.rfind(' ',0,self._length+1)) in (-1, self._length):
                    idx = self._length
                    
                self._data[-1] = line[:idx].strip()
                line = line[idx:].strip()
                
                if line:
                    self._data.append('')
        
    @abstractmethod    
    def end(self):
        self._data = []

class LeftParagraph(ABCParagraph):
    def end(self):
        for line in self._data:
            print(line) 
        super().end()
    
class RightParagraph(ABCParagraph):
    def end(self):
        for line in self._data:
            print(f'{line :>{self._length}}') 
        super().end()

rightparagraph = RightParagraph(28)

rightparagraph.add('I will not  regret the roses')
rightparagraph.add('Withered with a light spring 123')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()

rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()