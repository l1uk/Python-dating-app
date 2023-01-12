class Question(object):
    questions={}
    def __init__(self, text,answers=("1","2","3","4","5"), weight = 1, Id = None):
            '''
            Constructor
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
        answers = []
        for key, value in Question.questions.items():
            answers.append(value.answer())
        return answers
            
if __name__ == "__main__":
    q1 = Question("Sample question",("True","False") )