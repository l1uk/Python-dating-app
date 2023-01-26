'''Class related to the matchmaking feature, allowing either to match every participant individually or to pair all the participant togheder.  '''
from classes.question import Question
from classes.person import Person
from classes.answer import Answer

class MatchMaker(object):
    '''Class related to the matchmaking feature, allowing either to match every participant individually or to pair all the participant togheder. Note: M is matched with F and D is paired togheder. '''

    @staticmethod
    def findBestMatch(person_id, exclude = None):
        '''Return the single best match for a given person, 
     excluding the ones specified in the exclude list. '''
        answVal = Answer.getTotalForPerson(person_id)
        minDiff = None
        personID = -1
        personGender = Person.get(person_id).getGender()
        for key, value in Person.persons.items():
            if(key != person_id and ((personGender != "D" and value.getGender() != personGender and value.getGender() != "D" )
                or (value.getGender() == personGender and personGender == "D") ) and ((exclude != None and key not in exclude) or exclude == None)):
                diff = abs(answVal - Answer.getTotalForPerson(key))
                if(minDiff == None or minDiff > diff):
                    minDiff = diff
                    personID = key
        return personID

    @staticmethod
    def matchAll():
        ''' Using the precedent method, match all the participant 
     returns a list of matches and a boolean 
     indicating whether all the participans are matched or not. 
     Note: the implemented algorithm starts by finding the best match for the first person and goes on. It is not granted to return the best possible pairing.'''
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
