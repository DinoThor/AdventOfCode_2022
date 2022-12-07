f = open("dataP1.txt", "r")
currElf = 0; elfs = []

for line in f:
    if line == "\n":
        elfs.append(currElf)
        currElf = 0
    else:
        currElf += int(line)

print(max(elfs))
print(sum(sorted(elfs, key = int, reverse=True)[:3]))