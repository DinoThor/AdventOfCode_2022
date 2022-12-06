import string

f = open("dataP3.txt", "r")
res = 0
priority = {}; value = 1

for char in string.ascii_lowercase:
    priority[char] = value
    value += 1

for char in string.ascii_uppercase:
    priority[char] =  value
    value += 1

# for line in f:
#     firstComp = line[:len(line)//2]
#     secComp   = line[len(line)//2:]
#     inter = set(firstComp).intersection(secComp)
#     res += priority[inter.pop()]

group = 0
team = []
for line in f:
    group += 1
    team.append(line.replace("\n", ""))

    if group % 3 == 0:   
        print(team)
        firstComp = line[:len(line)//2]
        secComp   = line[len(line)//2:]
        inter     = set(team[0]).intersection(team[1]).intersection(team[2])
        res       += priority[inter.pop()]
        team      = []

print(res)