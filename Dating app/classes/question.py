'''
Question class, containing the text of the question itself and the possible answers 
'''
class Question(object):
    questions={}
    def __init__(self, text,answers=("1","2","3","4","5"), weight = 1, Id = None):
            '''
            In the constructor, the attributes text, answers are statically assigned
            and the answer Id is generated in case the parameter is not supplied, otherwise is checked for duplicates and assigned
            the weight parameter allows the developer to assign more or less importancy to the question (1: default). 
            '''
            if Id is None:
                if len(Question.questions) > 0:
                    Id = max(Question.questions.keys())+1
                else:
                    Id=0
            elif Id in Question.questions:
                    raise KeyError("Duplicate ID")
            if not isinstance(answers, tuple):  
                raise ValueError("Wrong answers format; must be a tuple")
            self.Id=Id
            self.answers = answers
            self.text = text
            self.weight = weight
            Question.questions[self.Id] = self
    pass

    def answer(self):
        '''Prompts the user to answer the question and validates the answer'''
        print(self)
        x = -1
        while(x < 1 or x > len(self.answers)):
            try:
                x = int(input("Insert your answer: "))
            except ValueError:
                print("Invalid input")
        return(self.Id, x)
    def __str__(self):
        retVal = ["Question " + str(self.Id) + ": " + self.text]
        i = 0
        for answer in self.answers:
            i += 1
            retVal.append(str(i) + ". " + answer)
        return  "\n".join(retVal)

    @staticmethod
    def answerAll():
        '''Prompts the user to answer all the saved questions and validates the answers'''
        answers = []
        for key, value in Question.questions.items():
            answers.append(value.answer())
        return answers
    @classmethod
    def getWeight(cls, num):
        '''Returns the weight associated to the provided question ID'''
        return cls.questions[num].weight if num in cls.questions else 0 
    @classmethod
    def get(cls, num):
        '''Returns the question associated to the provided question ID'''
        return cls.questions[num] if num in cls.questions else None 
if __name__ == "__main__":
    q1 = Question("Sample question",("True","False") )