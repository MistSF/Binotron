import numpy as np
import os
import json
import functionGroup as fg
from classBinotron import Promo, Apprenant

promo = Promo()
listdir = os.listdir('./')
exist = False
for x in listdir :
    if x == 'promo.json' :
        exist = True
        
if not exist :
    file = open('./promo.json', 'x')
    with open('./promo.json', 'w') as file :
        file.write(promo.toJSON())
    
with open('./promo.json', 'r') as file :
    promo_data = json.load(file)

print(promo_data["member"][0]["skill"], promo_data["member"][0]["learners"])

for x in promo_data["member"] :
    App = Apprenant(promo, x["name"])
    App.setAllData(x["skill"], x["learners"])
    promo.addMember(App)

print(promo.member[0].skill, promo.member[0].learners)

historyGroup = []
groups = []

run = True
groups = []


"""Apprenant("Antoine Dewynter", 2)
Apprenant("ArthurT", 3)
Apprenant("CamilleS", 1)
Apprenant("Farid Berrabah", 2)
Apprenant("Giovanny M", 3)
Apprenant("Joséphine" ,3)
Apprenant("Julien Vansteenkiste", 2)
Apprenant("Kevin Faby", 3)
Apprenant("Marie De smedt", 3)
Apprenant("Mickael Fayeulle", 3)
Apprenant("Phichet", 3)
Apprenant("Rachid K.", 2)
Apprenant("Tanguy Meyer", 2)
Apprenant("vivien", 3)
Apprenant("kevinb", 3)
Apprenant("Hatice", 3)"""

print("Welcome in group generator 0.1\nsend help to see our commands !\nHave fun\n")

while run :
    inp = input().lower()
    
    if inp == 'quit':
        print("bye")
        run = False
    elif inp == "help":
        fg.helps()
    elif inp == "edit":
        fg.edit(promo)
    elif inp == "print":
        fg.printLearners(promo)
    elif inp == "remove":
        fg.removeLearner(promo)
    elif inp == "add":
        fg.addLearner(promo)
    elif inp == "create comp":
        print("group size :")
        size = input()
        print("add filtre : \n1: none\n2 : Heterogene\n3 : Homogene")
        filtre = input()
        groups = fg.getGroups(promo, int(size), int(filtre))
        fg.printGroups(groups)
        print("save groups ? (Y/N)")
        rep = input().lower()
        if rep == 'y':
            fg.saveGroups(promo, historyGroup, groups)
            historyGroup.append(groups)
            print("group saved\n")
    elif inp == "create history":
        print("enter group size :")
        size = input()
        groups = fg.getHistoryGroup(promo, int(size))
        fg.printGroups(groups)
        print("save groups ? (Y/N)")
        rep = input().lower()
        if rep == 'y':
            fg.saveGroups(promo, historyGroup, groups)
            historyGroup.append(groups)
            print("group saved\n")
        else :
            groups = []
    elif inp == "show" :
        fg.printGroups(groups)
    else :
        pass