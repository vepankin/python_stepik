from re import fullmatch

class DomainException(Exception):
    pass

class Domain:

    def __init__(self, domain, validate=True):
        if validate and not (domain := self.get_domain(domain, r'(?P<domain>\w+.\w+)')):
            raise DomainException('Недопустимый домен, url или email')
        self._domain = domain
    
    def __str__(self):
        return self._domain
    
    @staticmethod
    def get_domain(data, reg_exp):
        if match := fullmatch(reg_exp, data):
            return match.group('domain')         
  
    @classmethod
    def from_url(cls, url):
        if domain := cls.get_domain(url, r'https?://(?P<domain>\w+.\w+)'):
            return cls(domain, False)
        raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_email(cls, email):
        if domain := cls.get_domain(email, r"[a-zA-Z]+@(?P<domain>\w+.\w+)"):
            return cls(domain, False)
        raise DomainException('Недопустимый домен, url или email')
    
# test 01    
print('test 01 '.ljust(80, '-'))

domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')
domain3 = Domain.from_email('support@pygen.ru')

print(domain1)
print(domain2)
print(domain3)

# test 02    
print('test 02 '.ljust(80, '-'))
try:
    domain1 = Domain('pygen..org')
except DomainException as e:
    print(e)

# test 08
print('test 08 '.ljust(80, '-'))

emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
        print(email, '->', domain)
    except DomainException as e:
        print(e)