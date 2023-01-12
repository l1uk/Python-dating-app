class Answer(object):
    answers={}
    def __init__(self, value, personId, questionId, Id = None):
            '''
            Constructor
            '''
            if Id is None:
                if len(Answer.answers) > 0:
                    Id = max(Answer.answers.keys())+1
                else:
                    Id=0
            elif Id in Answer.answers:
                    raise KeyError("Duplicate ID")
            self.value=value
            self.personId=personId
            self.questionId=questionId
            self.Id=Id
            Answer.answers[self.Id] = self
    pass
    def getValue(self):
        return int(self.value) 
    @staticmethod 
    def createAnswerForPerson(answers, personID):
        for ans in answers:
            Answer(ans[1],personID,ans[0])
    @staticmethod 
    def getAnswersForPerson(personID):
        result = []
        for key, value in Answer.answers.items():
            if value.personId == personID:
                result.append(value)
        return result
    @staticmethod 
    def getTotalForPerson(personID):
        result = 0
        for key, value in Answer.answers.items():
            if value.personId == personID:
                result += value.getValue()
        return result
    def __str__(self):
        return f"Question ID: {self.questionId}, Answer value: {self.value}, Answer ID: {self.Id}, Person ID: {self.personId}"
if __name__ == "__main__":
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
    p1 = Answer(10, 1000, 1000)
    print(p1)