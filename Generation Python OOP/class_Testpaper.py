from decimal import Decimal, ROUND_HALF_UP

class Testpaper:
    
    def __init__(self, subject: str, answers: list, percentage: str):
        self._subject = subject
        self._answers = answers
        self._percentage = int(percentage.strip('%'))
    
    def __len__(self):
        return len(self._answers)
    
    def __iter__(self):
        yield from self._answers        
    
    @property
    def subject(self):
        return self._subject

    @property
    def percentage(self):
        return self._percentage
    
class Student:
    
    def __init__(self):
        self._tests_taken = {}
    
    @property
    def tests_taken(self):
        if self._tests_taken:
            return f'{{{', '.join(f"'{k}': '{v}'" for k,v in self._tests_taken.items())}}}'
        return 'No tests taken'
    
    def take_test(self, test: Testpaper, answers: list):
        score = sum(map(lambda x: x[0]==x[1], zip(test, answers)))*100/len(test)       
        iscore = int(Decimal(score).quantize(Decimal(1), rounding=ROUND_HALF_UP))
        self._tests_taken[test.subject] = f"{'Failed!' if iscore<test.percentage else 'Passed!'} ({iscore}%)"
        
testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}