from datingApp.package.question import Question
from datingApp.package.person import Person
from datingApp.package.answer import Answer
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


if __name__=="__main__":
    load()
    Question.questions={}
    """
    Question("Would you consider your values to be traditional or progressive?")

    Question("Are you a spontaneous person or a planner?")

    Question("Do you prefer going out or staying in more?")

    Question("Are you religious?")

    Question("Do you enjoy traveling?")

    Question("Would you like to be famous?")

    Question("How would you best describe your character? (Shy or Expressive)")

    Question("Would you date someone from a different cultural background?")

    Question("Do you prefer the people in your life to be simple or complex?")

    Question("Would you prefer to swim with sharks or go sky diving?")

    Question("Are you interested in fashion?")

    Question("Are you vegan or vegetarian?")"""

    Question("Do you have a university degree or are you currently studying to have one?")
    dump()