f = open("dataP5.txt", "r")
stack = []
stack.append(["P", "Z", "M", "T", "R", "C", "N"])
stack.append(["Z", "B", "S", "T", "N", "D"])
stack.append(["G", "T", "C", "F", "R", "Q", "H", "M"])
stack.append(["Z", "R", "G"])
stack.append(["H", "R", "N", "Z"])
stack.append(["D", "L", "Z", "P", "W", "S", "H", "F"])
stack.append(["M", "G", "C", "R", "Z", "D", "W"])
stack.append(["Q", "Z", "W", "H", "L", "F", "J", "S"])
stack.append(["N", "W", "P", "Q", "S"])

for i in range(0, 9): stack[i].reverse()

# for l in f:
#     num     = int(l.split()[1])
#     from_   = int(l.split()[3]) - 1
#     to      = int(l.split()[5]) - 1
#     for _ in range(num):
#         lift = stack[from_].pop()
#         stack[to].append(lift)

for l in f:
    num     = int(l.split()[1])
    from_   = int(l.split()[3]) - 1
    to      = int(l.split()[5]) - 1
    lift    = []
    for i in range(num): lift.append(stack[from_].pop())

    lift.reverse()
    for i in lift: stack[to].append(i)

res = ""
for i in range(0, 9): res += stack[i].pop()

print(res)