import copy

file = open('input.txt', 'r')
seats = []
for line in file:
    seats.append(list(line.strip()))
baseSeats = copy.deepcopy(seats)

rowLen = range(0, len(seats))
colLen = range(0, len(seats[0]))
change = True
newSeats = copy.deepcopy(seats)
#partOne
while(change):
    change = False
    for i in rowLen:
        for j in colLen:
            ocuCount = 0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if(i + r in rowLen and j + c in colLen and not (r == 0 and c == 0)):
                        if seats[i + r][j + c] == '#': ocuCount = ocuCount + 1
            if(ocuCount == 0 and seats[i][j] == 'L'): 
                newSeats[i][j] = '#'
                change = True
            if(ocuCount >= 4 and seats[i][j] == '#'): 
                newSeats[i][j] = 'L'
                change = True
    #causes slowdown, definitely a better way to do this but im already behind
    seats = copy.deepcopy(newSeats)

count = 0
for i in seats:
    count = count + i.count('#')
print("Part 1: " + str(count))

#partTwo
seats = copy.deepcopy(baseSeats)
while(change):
    change = False
    for i in rowLen:
        for j in colLen:
            ocuCount = 0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if(not (r == 0 and c == 0)):
                        checkR = i + r
                        checkC = j + c
                        while(checkR in rowLen and checkC in colLen and seats[checkR][checkC] == '.'):
                            checkR = checkR + r
                            checkC = checkC + c
                        if(checkR in rowLen and checkC in colLen and seats[checkR][checkC] == '#'):
                            ocuCount = ocuCount + 1
            if(ocuCount == 0 and seats[i][j] == 'L'): 
                newSeats[i][j] = '#'
                change = True
            if(ocuCount >= 5 and seats[i][j] == '#'): 
                newSeats[i][j] = 'L'
                change = True
    #causes slowdown, definitely a better way to do this but im already behind
    seats = copy.deepcopy(newSeats)
            
count = 0
for i in seats:
    count = count + i.count('#')
print("Part 2: " + str(count))

