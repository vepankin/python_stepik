class User:
    def __init__(self, name):
        self.name = name
    
    def skip_ads(self):
        return False

class PremiumUser(User):    
    def skip_ads(self):
        return True
    
    def skip_ads(self):
        #return not super().skip_ads()
        return not User.skip_ads(self)
    
PU = PremiumUser('Bob')
print(PU.skip_ads())