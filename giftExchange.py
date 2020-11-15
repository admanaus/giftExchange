# -*- coding: utf-8 -*-

import random

# Track couples with letters "A" etc.
names = [["Martin", "A"],
         ["Julie", "A"],
         ["Patrick", "B"],
         ["Tori", "C"],
         ["Adrien", "C"],
         ["Akayla", "D"],
         ["Tiffany", "D"],
         ["Zack", "E"],
         ["Brooke", "E"]]

# names = [["Dad", "A"],
#          ["Mom", "A"],
#          ["Adrien", "B"],
#          ["Tori", "B"],
#          ["Mark", "D"]]


# Track original array position for easy 'buy for each other' comparison
def addArrayPosition():
    for i in range(len(names)):
        names[i].append(i)

def printNames():
    for i in range(len(names)):
        print(names[i][0], 'buys for', mixedNames[i][0])

# Not buying for yourself or your spouse
def checkForCleanList():
    for i in range(len(names)):
        if (names[i][0] == mixedNames[i][0]) or (names[i][1] == mixedNames[i][1]):
            return False
    return True

# Not two people buying for each other
def checkIfBuyingForEachOther():
    for i in range(len(names)):
        if mixedNames[int(mixedNames[i][2])][0] == names[i][0]:
            return False
    return True

addArrayPosition()

# Give mixedNames it's own memory space
mixedNames = names[:]

random.shuffle(mixedNames)

while (checkForCleanList() is False) or (checkIfBuyingForEachOther() is False):
    random.shuffle(mixedNames)
    checkForCleanList()
    checkIfBuyingForEachOther()

printNames()
