import sys

file = open('input.txt', 'r')
preamble = 25
numsVal = []
numsAge = []
cnt = 0

def insertion(nums, val):
    i = 0
    while(i < len(nums) and nums[i] < val): i = i + 1
    nums.insert(i, val)

def checkSum(nums, val):
    found = False
    low = 0
    high = len(nums) - 1
    while(not found and low != high):
        tmp = nums[low] + nums[high]
        if(tmp == val):
            found = True
        if(tmp > val):
            high = high - 1
        if(tmp < val):
            low = low + 1
    return found

p1 = None
lines = []
for line in file:
    line = line.strip()
    val = int(line)
    #used for part two
    lines.append(val)
    if(cnt < preamble):
        numsVal.append(val)
        numsAge.append(val)
    if(cnt == preamble):numsVal.sort()
    if(cnt >= preamble):
        if(not checkSum(numsVal, int(line))):
            print(line)
            p1 = int(line)
        old = numsAge[0]
        #two arrays is not a great solution, probably should rewrite this
        numsAge = numsAge[1:preamble]
        numsAge.append(val)
        numsVal.remove(old)
        insertion(numsVal, val)
    cnt = cnt + 1

a = 0
b = 2
setSum = sum(lines[a:b])
while(b < len(lines) and setSum != p1):
    if(setSum < p1):b = b + 1
    else: a = a + 1; b = a + 2
    setSum = sum(lines[a:b])

p2 = min(lines[a:b]) + max(lines[a:b])
print(str(p2))