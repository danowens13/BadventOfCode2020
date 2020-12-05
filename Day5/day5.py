import sys

file = open("input.txt", 'r')
maximum = 0
minimum = 1025
missing = 0
total = 0

for line in file:
    line = line.strip('\n')
    #maybe do this in a dictionary?
    line = line.replace('B', '1')
    line = line.replace('F', '0')
    line = line.replace('R', '1')
    line = line.replace('L', '0')
    lineVal = int(line, 2)
    total = total + lineVal
    if(lineVal > maximum):maximum = lineVal
    if(lineVal < minimum):minimum = lineVal
        
#calculate sum using gauss's formula and minus our observed sum
totalAct = ((maximum * (maximum + 1))/2) - (minimum * (minimum - 1)/2)
missing = totalAct - total
        
#First question prompt
print(maximum)
#Second question prompt
print(missing)
    