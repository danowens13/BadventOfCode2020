import sys
from collections import defaultdict

file = open("input.txt", 'r')

parents = defaultdict(lambda: [])
children = defaultdict(lambda: [])

def updateParentsAndChildren(childrenString="", parent=""):
    childrenString = childrenString.split(', ')
    for child in childrenString:
        if(child[0] != 'n'):
            if(child[len(child) - 1] == 's'): child = child[0:len(child) - 1]
            count = int(child[0])
            child = child[2:len(child)]
            parents[child].append(parent)
            children[parent].append((child, count))

def getParentList(bag):
    parentList = parents[bag]
    for bag in parents[bag]:
        tmpParentList = getParentList(bag)
        for tmpParent in tmpParentList:
            if(tmpParent not in parentList):
                parentList.append(tmpParent)
    return parentList

def getChildrenCount(bag):
    childrenCount = 0
    
    for bagTuple in children[bag]:
        childrenCount += bagTuple[1]
        childrenCount += bagTuple[1] * getChildrenCount(bagTuple[0])
    return childrenCount

for line in file:
    line = line.strip('.\n')
    line = line.split('s contain ')
    updateParentsAndChildren(line[1], line[0])


print(str(len(getParentList("shiny gold bag"))))
print(str(getChildrenCount("shiny gold bag")))

