import sys
file = open("input.txt", 'r')
validCount = 0
if(len(sys.argv) == 2 and sys.argv[1] == '1'):
    for line in file:
        min = int(line.split("-")[0])
        max = int(line.split(" ")[0].split("-")[1])
        car = line[line.rindex(':') - 1]
        count = len(line.split(car)) - 2
        if(min <= count & count <= max):
            validCount = validCount + 1
    
if(len(sys.argv) == 2 and sys.argv[1] == '2'):
     for line in file:
        valid = False
        first = int(line.split("-")[0]) - 1
        second = int(line.split(" ")[0].split("-")[1]) - 1
        car = line[line.rindex(':') - 1]
        line = line.split(" ")[2]
        if(line[first] == car):
            valid = not valid
        if(line[second] == car):
            valid = not valid
        if(valid):
            validCount = validCount + 1
print(validCount)