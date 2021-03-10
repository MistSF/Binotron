import json

class Apprenant:
    def __init__(self, promo, name, skill=0): #Renseigner obligatoirement, firstname et lastname, skill est optionel
        self.name = name
        self.skill = skill
        self.link = []
        self.learners = {}
        for x in promo.getMember() :
            self.newLearner(x.name)
            x.newLearner(name)
        promo.addMember(self)
        
    def removeLearner(self, value) :
        self.learners.pop(value)
        
    def setName(self, promo, value):
        for x in promo.getMember() :
            for nameLearner in x.learners :
                if nameLearner == self.name :
                    x.newLearner(value, x.learners[nameLearner])
                    x.removeLearner(self.name)
        self.name = value
        
        
    def setSkill(self, value):
        self.skill = value
        
    def newLearner(self, new, history=0) :
        self.learners[new] = history
    
    def setAllData(self, skill, learners) :
        self.skill = skill
        for x in learners :
            self.learners[x] = learners[x]

class Promo:
    def __init__(self) :
        self.member = []
    
    def addMember(self, learner) :
        self.member.append(learner)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def getMember(self) :
        return self.member