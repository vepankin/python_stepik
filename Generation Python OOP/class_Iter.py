class I:
    def __init__(self):
        self.list = [1,2,3,4,5,6,7]
        
    def __iter__(self):
        return iter(self.list)
    
        


i = I()

print([e for e in i], list(iter(i)))