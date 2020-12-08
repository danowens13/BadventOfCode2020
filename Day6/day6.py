import sys
file = open("input.txt", 'r')

answerAny = []
answerAll = [0] * 26
total1 = 0
total2 = 0
peopleCount = 0
for line in file:
    line = line.strip('\n')
    if(line == ''):
        total1 = total1 + len(answerAny)
        for ans in answerAll:
            if(ans == peopleCount):
                total2 = total2 + 1
        answerAny = []
        answerAll = [0] * 26
        peopleCount = 0
    else:
        peopleCount = peopleCount + 1
        for char in line:
            if(not char in answerAny):
                answerAny.append(char)
            answerAll[ord(char) - 97] = answerAll[ord(char) - 97] + 1
            
print("answer 1: " + str(total1))
print("answer 2: " + str(total2))