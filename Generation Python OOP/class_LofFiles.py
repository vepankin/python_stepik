import os

class LogFiles:
    def __init__(self, path):
        self._path = path
                
    def get_names(self):
        lst = []
        for root, dirs, files in os.walk(self._path):
            if root == self._path:
                lst.extend(os.path.splitext(f)[0] for f in files) 
        return lst
    
    def save_names(self, path):
        with open(path, 'w', encoding='utf-8') as file:
            names = self.get_names()
            names_count = len(names)
            
            file.write((s:=f'Total WS count = {names_count}')+'\n')
            file.write('-' * len(s) + '\n')
            file.writelines(name+'\n' for name in names)
        return names_count    
        


log_files = LogFiles(r'\\grand\1CShared\LOG\8.3.22.2239')    
n = log_files.save_names(r'C:\TEMP\Computers.txt')
print(f'WS names saved to file successfully ({n})')