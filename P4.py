f = open("dataP4.txt" ,"r")
res = 0

for line in f:
    pairs = line.replace("\n", "").split(",")

    elf_1 = list(map(int, [pairs[0].split("-")[0], pairs[0].split("-")[1]]))
    elf_2 = list(map(int, [pairs[1].split("-")[0], pairs[1].split("-")[1]]))

    # if   (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]):
    #     print(elf_1 , elf_2, "TRUE")
    #     res += 1
    # elif elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]:
    #     print(elf_1 , elf_2, "TRUE")
    #     res += 1
    # else:
    #     print(elf_1 , elf_2)

    if set(range(elf_1[0], elf_1[1] + 1)).intersection(range(elf_2[0], elf_2[1] + 1)):
        res += 1

print(res)