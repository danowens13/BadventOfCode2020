x = 0
y = 0
direct = 90
card = {
    0 : 'N',
    90 : 'E',
    180 : 'S',
    270 : 'W'
}

file = open('input.txt', 'r')

for line in file: 
    direction = line[0]
    distance = int(line.strip()[1:])
    if(direction == 'F'):
        direction = card[direct]
    if(direction == "N"):
        y = y + distance
    if(direction == "S"):
        y = y - distance
    if(direction == "E"):
        x = x + distance
    if(direction == "W"):
        x = x - distance
    if(direction == "L"):
        direct = (direct - distance) % 360 
    if(direction == "R"):
        direct = (direct + distance) % 360 
    
print("Part 1: " + str(abs(x) + abs(y)))

x = 0
y = 0
wayX = 10
wayY = 1
direct = 0

file = open('input.txt', 'r')
for line in file: 
    direction = line[0]
    distance = int(line.strip()[1:])
    if(direction == 'F'):
        x = x + (wayX) * distance
        y = y + (wayY) * distance
    if(direction == "N"):
        wayY = wayY + distance
    if(direction == "S"):
        wayY = wayY - distance
    if(direction == "E"):
        wayX = wayX + distance
    if(direction == "W"):
        wayX = wayX - distance
    if(direction == "L" or direction == "R" ):
        quadX = wayX - x
        quadY = wayY - y
        if(direction == "L"): 
            distance = 360 - distance
        if(distance == 90):
            tmpX = wayX
            wayX = wayY
            wayY = tmpX * -1
        if(distance == 180):
            wayY = wayY * -1
            wayX = wayX * -1
        if(distance == 270):
            tmpX = wayX
            wayX = wayY * -1
            wayY = tmpX 

print("Part 2: " + str(abs(x) + abs(y)))