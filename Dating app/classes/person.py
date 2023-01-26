'''Person class, contatining name and gender (M, F, D).'''
import string
import random
class Person(object):
    persons={}
    genders = {"M" : "male", "F" : "female", "D" : "diverse"}
    def __init__(self, name, gender, Id = None):
            '''
            The attributes name, gender are statically assigned in the constructor while the ID gets automatically generated if empty; otherwise it is checked for duplicates 
            '''
            if Id is None:
                Id=Person.getNextID()
            elif Id in Person.persons:
                    raise KeyError("Duplicate ID")
            if gender not in Person.genders:
                raise ValueError("invalid gender")
            self.name=name
            self.gender=gender
            self.Id=Id
            Person.persons[self.Id] = self
    pass
    def __str__(self):
        '''
        str() to string method 
        '''
        return f"{self.Id}: {self.name}, {self.gender}"
     
    @staticmethod
    def createNewPerson():
        '''Prompts the user for new person data and saves it'''
        name = str(input("Please insert name: "))
        gender = "l"
        while gender not in Person.genders:
            gender = str(input("please insert gender: "))
        Id = Person.getNextID()
        Person(name,gender, Id)
        return Id

    @staticmethod
    def createNewRandomPerson(nameLength):
        '''Generates new person data and saves it'''
        name = ''.join(
            random.choice(string.ascii_lowercase) for _ in range(nameLength)
        )
        gender = ''.join(
            random.choice("MFD") for _ in range(1)
        )
        Id = Person.getNextID()
        Person(name,gender, Id)
        return Id

    @staticmethod
    def getNextID():
        '''Internally used method to get the ID for the next person'''
        if len(Person.persons) > 0:
                Id = max(Person.persons.keys())+1
        else:
            Id=0
        return Id

    @staticmethod
    def printPersons():
        '''Prints all the saved persons'''
        for key, value in Person.persons.items():
            print(value)
    @classmethod
    def get(cls, num):
        '''Returns the given person's object'''
        return cls.persons[num] if num in cls.persons else None
    def getId(self):
        '''Returns the id of the given person'''
        return int(self.Id)
    def getGender(self):
        '''Returns the gender of the given person'''
        return str(self.gender)
if __name__ == "__main__":
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
    p1 = Person("Luca", "M")
    print(p1)