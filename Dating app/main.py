from datingApp.package.question import Question
from datingApp.package.person import Person
from datingApp.package.answer import Answer
from datingApp.package.utils import Utils
import pickle
filename = "data.dat"
def dump():
    # combine all data to one object
    data = {"persons" : Person.persons, "questions" : Question.questions, "answers" : Answer.answers}
    with open(filename,"wb") as file:
        pickle.dump(data, file, protocol=pickle.DEFAULT_PROTOCOL)

def load():
    # read data file into object
    try:
        with open(filename,"rb") as file:
            data = pickle.load(file)
            Question.questions = data["questions"]
            Answer.answers = data["answers"]
            Person.persons = data["persons"]    
    except OSError as e:
        print(f"{type(e)}: {e}")

def printMenu():
    print("""Press 0 for exit, 1 to join if you are a new partecipant, 2 to list all partecipants, 
3 for redo the questionary for a given participant, 4 to see the answer for a given participant,
5 to find the best partner for a given participant""".replace('\n',''))

def findBestMatch(person_id):
    answVal = Answer.getTotalForPerson(person_id)
    minDiff = 0
    personID = 0
    for person in Person.persons:
        if(person != person_id):
            diff = abs(answVal - Answer.getTotalForPerson(person))
            if(minDiff > diff):
                minDiff = diff
                personID = person
    return personID

if __name__ == "__main__":
    load()
    exit = False
    while(not exit):
        printMenu()
        choice = Utils.integerInput(0,5)
        match choice:
            case 0:
                exit = True
            case 1:
                person_id = Person.createNewPerson()
                answers = Question.answerAll()
                Answer.createAnswerForPerson(answers,person_id)

            case 2: 
                Person.printPersons()
            case 3:
                Person.printPersons()
                choice = Utils.integerInput(0,len(Person.persons))
                answers = Question.answerAll()
                Answer.createAnswerForPerson(answers,choice)  
            case 4:
                Person.printPersons()
                choice = Utils.integerInput(0,len(Person.persons))
                for ans in Answer.getAnswersForPerson(choice):
                    print(str(ans))
            case 5:
                Person.printPersons()
                choice = Utils.integerInput(0,len(Person.persons))
                match = findBestMatch(choice)
                print(Person.get(match))  
    dump()