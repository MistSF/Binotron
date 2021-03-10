import numpy as np
import random
from classBinotron import Apprenant
import pandas as pd
import re

def savePromoJSON(promo) :
    """
        function to save promo in promo.json 
    """
    test = promo.toJSON()
    with open('./promo.json', 'w') as file :
        file.write(test)
        file.close()

def printGroups(groups) :
    """
        show group
    """
    for i, group in enumerate(groups) :
        learners = ""
        for learner in group :
            learners += learner.name + ", "
        print("groupe " + str(i) + " : " + str(learners))

def saveGroups(promo, historyGroup, groups) :
    """
        update learners attribute in promo.json to keep how many times learners as been grouped with the others
    """
    for group in groups :
        members = []
        for learner in group :
            members.append(learner.name)
        for learner in group :
            for m in members :
                if m != learner.name :
                    learner.learners[m] = learner.learners[m] + 1
    historyGroup.append(groups)
    savePromoJSON(promo)

def getMembers(group, tmp) :
    """
        get members with the less value with the actual group
    """
    candidat = []
    listName = []
    saveName = None
    saveValue = -1
    
    for x in tmp :
        listName.append(x.name)
        
    for x in group :
        candidat.append(x.learners.items())
        
    for name in listName :
        tmpValue = 0
        for memberList in candidat :
            for member in memberList :
                if member[0] == name :
                    tmpValue += member[1]
        if tmpValue < saveValue or saveValue == -1 :
            saveValue = tmpValue
            saveName = name
        
    for learner in tmp :
        if learner.name == saveName :
            group.append(learner)
            tmp.remove(learner)

def getHistoryGroup(promo, size=2):
    """
        create group based on history
    """
    if size >= len(promo.getMember()) / 2 :
        size = len(promo.getMember()) // 2
    nb_group = len(promo.getMember()) // size
    tmp = promo.getMember().copy()
    
    groups = []
    for i in range(nb_group) :
        groups.append([])
    
    for group in groups:
        indexLearner = np.random.choice(len(tmp))
        learner = tmp[indexLearner]
        group.append(learner)
        tmp.remove(learner)
            
    grp = 0
    while len(tmp) > 0 :
        getMembers(groups[grp], tmp)
        if grp >= nb_group -1 :
            grp = 0
        else :
            grp = grp + 1

    return groups

def getGroups(promo, group_size, sort_by = None):
    """
        Get groups filtered by skills
    """
    copy_promo = list(promo.getMember())
    if sort_by == 3 or sort_by == 2:
        copy_promo.sort(key=lambda user: user.skill)
    else :
        random.shuffle(copy_promo)
    groups = np.array_split(np.asarray(copy_promo), round(len(promo.getMember()) / group_size))
    
    if sort_by == 2:
        groups_size = [len(group) for group in groups]
        groups = []
        for group_size in groups_size:
            coeff = round(len(copy_promo) / group_size)
            group = []
            for i in range(group_size):
                position = (coeff * i) - i
                group.append(copy_promo[position])
                copy_promo.pop(position)
            groups.append(group)          
    return groups

def helps():
    """
        show available command
    """
    print("help   : print available commands") # OK
    print("add    : add new learner") # OK
    print("edit   : edit learner") #OK
    print("create history : create new group with history") #OK
    print("create comp : create new group")
    print("show   : Show groups") #OK
    print("print  : Print learners") #OK
    print("remove : Remove learners") #OK
    print("quit   : exit programm") # OK
    print("history: Show group history") # Ok
    print("")

def printLearners(promo) :
    """
        show learners in promo
    """
    for x in promo.getMember():
        learnSeries = pd.Series(x.learners)
        print(x.name, x.skill, "\n", learnSeries, "\n")

def removeLearner(promo) :
    """
        remove learner from promo
    """
    printLearners(promo)
    print("Select name :")
    name = input()
    for i, x in enumerate(promo.getMember()) :
        if x.name.lower() == name.lower() :
            promo.getMember().pop(i)
            break
    for x in promo.getMember() :
        x.removeLearner(name)
    savePromoJSON(promo)

def edit(promo):
    """
        edit learner in promo
    """
    for x in promo.getMember() :
        print(x.name)
    
    print("\nSelect learner : ")
    learner = input().lower()
    
    for x in promo.getMember() :
        if x.name.lower() == learner:
            learner = x
            break
    
    print(learner.name, learner.skill, sep=" ")
    print("1: edit name\n2: edit skill")
    nb = input()
    
    if nb == '1':
        print("enter new name")
        new = input()
        learner.setName(new)
    elif nb == '2':
        print("enter new skill level")
        new = input()
        learner.setSkill(int(new))
    else :
        pass
    
    print(learner.name, learner.skill, sep=" ")
    print("Done\n")

def addLearner(promo):
    """
        Add learner in promo
    """
    print('Enter the new name:')
    name = input()
    dontAdd = True
    while dontAdd :
        dontAdd = False
        for x in promo.getMember() :
            if x.name.lower() == name.lower() :
                dontAdd = True
                print(name, ' is already in the promo, please chose a new name :')
                name = input()
    Apprenant(promo, name)
    savePromoJSON(promo)

def getSize() :
    """
        get group size with type verification
    """
    size_state = True
    while size_state == True:
        print("enter group size :")
        size = input()
        size_state = False
        size = re.findall("[0-9]", size)
        if len(size) <= 0 :
            size_state = True
    valret = ""
    for x in size :
        valret = valret + x
    return int(valret)