from classes.question import Question
from classes.person import Person
from classes.answer import Answer
import pickle

personsToCreate = 1000

filename = "data.dat"
def dump():
    '''save all data into file data.dat'''
    data = {"persons" : Person.persons, "questions" : Question.questions, "answers" : Answer.answers}
    with open(filename,"wb") as file:
        pickle.dump(data, file, protocol=pickle.DEFAULT_PROTOCOL)

def load():
    ''' load all data from file data.dat '''
    try:
        with open(filename,"rb") as file:
            data = pickle.load(file)
            Question.questions = data["questions"]
            Answer.answers = data["answers"]
            Person.persons  = data["persons"]    
    except FileNotFoundError as e:
        pass
    

if __name__=="__main__":
    load()
    Answer.answers={}
    Person.persons={}
    print("Starting to create " + str(personsToCreate) + " random persons")
    for i in range(0,personsToCreate):
        id = Person.createNewRandomPerson(5)
        answers = Question.answerAllRandomly()
        Answer.createAnswerForPerson(answers,id)
        if(i % 100 == 0):
            print("Progress: " + str((i/personsToCreate)*100) + "%")
    print("Successfully created " + str(personsToCreate) + " random persons")
    dump()