'''
Script allowing a developer to store questions in the data file.
'''

from classes.question import Question
from classes.person import Person
from classes.answer import Answer
import pickle

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

def createQuestions(): 
    '''Questions are defined here. The questions dict is empyted and repopulated.'''
    Question.questions={}
    Question("Would you consider your values to be traditional or progressive?")

    Question("Are you a spontaneous person or a planner?")

    Question("Do you prefer going out or staying in more?")

    Question("Are you religious?")

    Question("Do you enjoy traveling?")

    Question("Would you like to be famous?")

    Question("How would you best describe your character? (Shy to Expressive)")

    Question("Would you date someone from a different cultural background?")

    Question("Do you prefer the people in your life to be simple or complex?")
if __name__=="__main__":
    load()
    createQuestions()
    dump()