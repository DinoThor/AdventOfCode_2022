f = open("dataP2.txt", "r")

# weaponScore = {"X":1, "Y":2, "Z":3}
# tie         = [("A","X"), ("B","Y"), ("C","Z")]
# lostRound   = [("A","Z"),("B","X"),("C","Y")]
# totalPoints = 0

# for l in f:
#     round  = l.split()
#     choose = (round[0], round[1])
#     if   (choose in lostRound):
#         totalPoints += weaponScore[round[1]]
#     elif (choose in tie):
#         totalPoints += weaponScore[round[1]] + 3
#     else:
#         totalPoints += weaponScore[round[1]] + 6

weaponScore = {"X":1, "Y":2, "Z":3}
tie         = {"A":"X", "B":"Y", "C":"Z"}
lostRound   = {"A":"Z", "B":"X", "C":"Y"}
wonRound    = {"A":"Y", "B":"Z", "C":"X"}
totalPoints = 0

for l in f:
    round  = l.split()
    print(lostRound[round[0]])

    if   (round[1] == "X"):
        totalPoints += weaponScore[lostRound[round[0]]]
    elif (round[1] == "Y"):
        totalPoints += weaponScore[tie[round[0]]] + 3
    else:
        totalPoints += weaponScore[wonRound[round[0]]] + 6

print(totalPoints)