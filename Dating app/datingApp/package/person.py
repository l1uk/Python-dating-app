class Person(object):
    persons={}
    def __init__(self, name, gender, Id = None):
            '''
            Constructor
            '''
            if Id is None:
                Id=Person.getLastID()
            elif Id in Person.persons:
                    raise KeyError("Duplicate ID")
            self.name=name
            self.gender=gender
            self.Id=Id
            Person.persons[self.Id] = self
    pass
    def getId(self):
        return int(self.Id)
    def __str__(self):
        '''
        str() to string method 
        '''
        return f"{self.Id}: {self.name}, {self.gender }"
     
    @staticmethod
    def createNewPerson():
        name = str(input("Please insert name: "))
        gender = str(input("please insert gender: "))
        Id = Person.getLastID()
        Person(name,gender, Id)
        return Id

    @staticmethod
    def getLastID():
        if len(Person.persons) > 0:
                Id = max(Person.persons.keys())+1
        else:
            Id=0
        return Id

    @staticmethod
    def printPersons():
        for key, value in Person.persons.items():
            print(value)
    @classmethod
    def get(cls, num):
        return cls.persons[num]
    
if __name__ == "__main__":
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
    p1 = Person("Luca", "M")
    print(p1)