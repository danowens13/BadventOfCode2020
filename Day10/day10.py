import sys

file = open('basic.txt', 'r')

vals = []
difs = [0, 0, 0, 1]
for line in file:
    line = line.strip()
    vals.append(int(line))

vals.sort()
# part 1
prev = 0
for val in vals:
    dif = val - prev
    difs[dif] = difs[dif] + 1
    prev = val
print(str(difs[1] * difs[3]))