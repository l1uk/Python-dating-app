'''
Main file, aggregating all the functions and presenting a menu to the user.
'''
from classes.question import Question
from classes.person import Person
from classes.answer import Answer
from classes.utils import Utils
from classes.matchMaker import *
from enum import Enum
import pickle

class MainMenuItem(Enum):
    QuitProgram = '0'
    OpenUserAccount = '1'
    ListParticipants = '2'
    redoQuestionaryForGivenParticipant = '3'
    seeAnswersForGivenParticipant = '4'
    findBestMatchForGivenParticipant = '5'
    findBestMatchForALLParticipants = '6'

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
    
def printMenu():
    '''simple method to print the User menu'''
    print("MAIN MENU:")
    print(" Statistics: ")
    print("     # of users: " + str(len(Person.persons)))
    print("     # of questions: " + str(len(Question.questions)))
    print("\n".join(["{:>3}. {}".format(i.value, i.name) for i in MainMenuItem]))



if __name__ == "__main__":
    load()
    exit = False
    while(not exit):
        printMenu()
        choice = Utils.integerInput(0,len(MainMenuItem)-1)
        match choice:
            case 0:
                exit = True
            case 1:
                person_id = Person.createNewPerson()
                answers = Question.answerAll()
                Answer.createAnswerForPerson(answers,person_id)
            case 2: 
                if len(Person.persons)>0:
                    Person.printPersons()
                else: 
                    print("### No participants! ###") 
            case 3:
                if len(Person.persons)>0:
                    Person.printPersons()
                    choice = Utils.integerInput(0,len(Person.persons)-1)
                    answers = Question.answerAll()
                    Answer.deleteAnswersForPerson(choice)
                    Answer.createAnswerForPerson(answers,choice)  
                else: 
                    print("### No participants! ###") 
            case 4:
                if len(Person.persons)>0:
                    Person.printPersons()
                    choice = Utils.integerInput(0,len(Person.persons)-1)
                    for ans in Answer.getAnswersForPerson(choice):
                        print(str(ans))
                else: 
                    print("### No participants! ###")            
            case 5:
                if len(Person.persons)>0:
                    Person.printPersons()
                    choice = Utils.integerInput(0,len(Person.persons)-1)
                    match = MatchMaker.findBestMatch(choice)
                    if match != -1:
                        print(str(Person.get(choice)) + " has been matched with " + str(Person.get(match)))
                    else: 
                        print("### No match! ###")
                else: 
                    print("### No participants! ###") 
            case 6:
                if len(Person.persons)>0:
                    matches, notAllMatched = MatchMaker.matchAll()
                    for ids in matches:
                        print(str(Person.get(ids[0])) + " has been matched with " + str(Person.get(ids[1])))
                    if(notAllMatched):
                        print("### Warning! Not all people have been matched ###")     
                else:
                    print("### No participants! ###")          

    dump()