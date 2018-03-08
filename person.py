class person:
    counter=0
    def __init__(self,a='Teja', b='female'):
        self.name=a
        self.gender=b
        person.counter=person.counter+1
    def showInfo(self):
        print('name=',self.name)
        print('gender=',self.gender)
    @classmethod
    def showCount(cls):
        print('Number of objects created so far:',cls.counter)
        
