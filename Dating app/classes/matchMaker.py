from classes.question import Question
from classes.person import Person
from classes.answer import Answer

class MatchMaker(object):
    # return the single best match for a given person, 
    # excluding the ones specified in the exclude list 
    @staticmethod
    def findBestMatch(person_id, exclude = None):
        answVal = Answer.getTotalForPerson(person_id)
        minDiff = None
        personID = -1
        personGender = Person.get(person_id).getGender()
        for key, value in Person.persons.items():
            if(key != person_id and value.getGender() != personGender and ((exclude != None and key not in exclude) or exclude == None)):
                diff = abs(answVal - Answer.getTotalForPerson(key))
                if(minDiff == None or minDiff > diff):
                    minDiff = diff
                    personID = key
        return personID

    # using the precedent method, match all the participant 
    # returns a list of matches and a boolean 
    # indicating whether all the participans are matched or not
    @staticmethod
    def matchAll():
        matched = []
        matches = []
        for key, value in Person.persons.items():
            if key not in matched:
                match = MatchMaker.findBestMatch(key, matched)
                if match != -1:
                    matched.append(match)
                    matched.append(key)
                    matches.append((key, match))
        return matches, len(matched) < len(Person.persons)
