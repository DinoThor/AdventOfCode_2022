f = open("dataP6.txt", "r")
data = list(f.readline())

# for i in range(len(data)):
#     marker = [data[j] for j in range(i, i + 4)]
#     if len(marker) == len(set(marker)):
#         print((i + 3) + 1)
#         break

for i in range(len(data)):
    marker = [data[j] for j in range(i, i + 14)]
    if len(marker) == len(set(marker)):
        print((i + 14) + 1)
        break