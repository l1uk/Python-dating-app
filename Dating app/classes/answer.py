'''
Answer class, related to its originatory question and to the user who answered it 
'''
from classes.question import Question
class Answer(object):
    answers={}
    def __init__(self, value, personId, questionId, Id = None):
            '''
            In the constructor, the attributes value, personId, questionId are statically assigned
             and the answer Id is generated in case the parameter is not supplied, otherwise is checked for duplicates and assigned
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
        '''return the numeric value of the answer, according to the weight of the question'''
        return int(self.value) * int(Question.getWeight(self.questionId))

    @staticmethod 
    def createAnswerForPerson(answers, personID):
        '''     given a list of answers values and questions IDs as well as the ID of the person replying,
     create and store Answers objects'''
        for ans in answers:
            Answer(ans[1],personID,ans[0])
    
    @staticmethod 
    def getAnswersForPerson(personID):
        '''returns all the answers for a given person '''
        result = []
        for key, value in Answer.answers.items():
            if value.personId == personID:
                result.append(value)
        return result
    @staticmethod 
    def deleteAnswersForPerson(personID):
        '''delete all the answers for a given person'''
        keys = Answer.getAnswersForPerson(personID)
        for key in keys:
            del Answer.answers[key.Id]
    @staticmethod 
    def getTotalForPerson(personID):
        '''return the total value of all the questions for a given person'''
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
    p1.getValue()
    print(p1)