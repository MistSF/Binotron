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

for x in promo_data["member"] :
    App = Apprenant(promo, x["name"])

for x in promo_data["member"] :
    for y in promo.member :
        if y.name == x["name"] :
            y.setAllData(x["skill"], x["learners"])

historyGroup = []
groups = []

run = True
groups = []

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