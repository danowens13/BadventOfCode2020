import sys

file = open("input.txt", 'r')


valid = [False] * 7
validMap={
    'byr': 0,
    'iyr':1,
    'eyr':2,
    'hgt':3,
    'hcl':4,
    'ecl':5,
    'pid':6
}

def byr(val):

    return (len(val) == 4 and int(val) >= 1920 and int(val) <= 2002)

def iyr(val):
    return (len(val) == 4 and int(val) >= 2010 and int(val) <= 2020)

def eyr(val):
    return (len(val) == 4 and int(val) >= 2020 and int(val) <= 2030)

def hgt(val):
    label = val[len(val)-2:len(val)]
    if(label == 'cm'):
        val = int(val[0:len(val)-2])
        if(val >= 150 and val <= 193):
            return True
    if(label == 'in'):
        val = int(val[0:len(val)-2])
        if(val >= 59 and val <= 76):
            return True
    return False
        
def hcl(val):
    if(val[0] == '#'):
        val = val[1:len(val)]
        try:
            int(val, 16)
        except ValueError:
            return False
        else:
            return True

def ecl(val):
    #probably should be a map
    return(val == 'amb' or val == 'blu' or val == 'brn' or val == 'gry' or val == 'grn' or val == 'hzl' or val == 'oth')

def pid(val):
    return (len(val) == 9 and str.isnumeric(val))

def default(val):
    return False

validatorMap={
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}
validCount = 0
for line in file:
    line = line.strip('\n')
    if(line == ''):
        if all(valid):
            validCount = validCount + 1
        valid = [False] * 7
    else:
        vals = line.split(' ')
        for val in vals:
            #problem 1
            if(len(sys.argv) == 2 and sys.argv[1] == '1'):
                val = val.split(':')[0]
                pos = validMap.get(val, -1)
                if(pos != -1):
                    valid[pos] = True
            #problem 2
            if(len(sys.argv) == 2 and sys.argv[1] == '2'):
                valArray = val.split(':')
                field = valArray[0]
                val = valArray[1]
                passed = validatorMap.get(field, default)(val)
                if(passed):
                    pos = validMap.get(field, -1)
                    if(pos != -1):
                        valid[pos] = True
print(validCount)
    