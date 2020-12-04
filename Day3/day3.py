import sys
import array

file = open("input.txt", 'r')
#python is weird
count = array.array('i', [0 for i in range(5)])
pos = array.array('i', [0 for i in range(5)])
inc = array.array('i', [1, 3, 5, 7])
#first line doesn't matter, we dont start in a tree. Reducing one length because of the new line character
length = len(file.readline()) - 1
even = False
for line in file:
    line = line.strip('\n')
    for i in range(4):
        pos[i] = (pos[i] + inc[i]) % length
        if(line[pos[i]] == '#'):
            count[i] = count[i] + 1
    if(even):
        pos[4] = (pos[4] + 1) % length
        if(line[pos[4]] == '#'):
            count[4] = count[4] + 1
    even = not even

total = 1
for totals in count:
    total = total * totals
print("Problem 1: " + str(count[1]))
print("Problem 2: " + str(total))