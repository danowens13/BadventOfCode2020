import sys
import copy

def run(operations):
    op = operations[0]
    pc = 0
    ppc = 0
    acc = 0
    tried = []
    while op[2] != 1 and pc < len(operations):
        ppc = pc
        if(op[0] == 'nop'):
            pc = pc + 1      
        if(op[0] == 'acc'):
            acc = acc + op[1]
            pc = pc + 1
        if(op[0] == 'jmp'):
            pc = pc + op[1]
        op[2] = 1
        if(pc < len(operations)):
            op = operations[pc]
    return [operations, acc]

def combValues(operations):
    validPos = []
    switchPos = -1
    lastPos = -1
    i = len(operations) - 1
    while(operations[i][0] in ('nop', 'acc') or (operations[i][0] == 'jmp' and operations[i][1] == 1)):
        validPos.append(i)
        i = i - 1
    lastPos = i
    while(switchPos == -1):
        while(i > -1 and switchPos == -1):
            if(operations[i][0] == 'nop'):
                if(operations[i][2] == 1 and operations[i][1] + i in validPos):
                    switchPos = i
                if(i + 1 in validPos):
                    validPos.append(i)
            if(operations[i][0] == 'jmp'):
                if(operations[i][2] == 1 and i + 1 in validPos):
                    switchPos = i
                if(operations[i][1] + i in validPos):
                    validPos.append(i)
                    k = i - 1
                    while(k > -1 and operations[k][0] in ('nop', 'acc')):
                        validPos.append(k)
                        k = k - 1
            i = i - 1    
        i = lastPos
    return switchPos

operations = []
file = open('input.txt', 'r')
for line in file:
    line = line.strip().split()
    operations.append([line[0], int(line[1]), 0])
operationsSwitched = copy.deepcopy(operations)
vr = run(operations)
ranOperations = vr[0]
print("Problem 1: " + str(vr[1]))
switchPos = combValues(ranOperations)
if(operationsSwitched[switchPos][0] == 'jmp'):
    operationsSwitched[switchPos][0] = 'nop'
else:
    operationsSwitched[switchPos][0] = 'jmp'
print("Problem 2: " + str(run(operationsSwitched)[1]))


        

