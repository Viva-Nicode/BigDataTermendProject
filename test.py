# proficiencyList = None
recordList = None
alreadyrecordList = None

# with open("./proficiency.txt", "r") as proficiency:
#     proficiencyList = proficiency.readlines()

with open("./record.txt", "r") as record:
    recordList = record.readlines()

with open("./temp.txt") as temp:
    alreadyrecordList = temp.readlines()

# 똑같으면 false
def isequals(recordGame, tempgame):
    iss = False
    for idx in range(0, 10):
        if not (recordGame[idx].split(",")[1] == tempgame[idx].split(",")[1]):
            iss = True
    return iss

result = []

for idx in range(0, len(recordList), 10):
    onegame = recordList[idx : idx + 10]
    rr = True
    for idx2 in range(0, len(alreadyrecordList), 10):
        temponegame = alreadyrecordList[idx2 : idx2 + 10]
        r = isequals(onegame, temponegame)
        if r == False:
            rr = False
            break
    if rr == True:
        result.extend(onegame)
print(len(result))

with open('heheeh.txt', 'a') as asdf:
    for ind,elem in enumerate(result):
        asdf.write(elem)





# for idx in range(0, len(recordList), 10):
#     onegame = recordList[idx : idx + 10]
#     pl = []
#     for inidx, elem in enumerate(onegame):
#         cn = str(elem).split(",")[1]
#         n = str(elem).split(",")[2]
#         s = n + "," + cn

#         for ininidx, inelem in enumerate(proficiencyList):
#             if s in inelem:
#                 pl.append(elem.rstrip() + "," + inelem)
#                 break

#     if len(pl) == 10:
#         with open('existProfiRecord.txt', 'a') as epr:
#             for i, e in enumerate(pl):
#                 epr.write(e)


# eprl = []
# with open("existProfiRecord.txt", "r") as epr:
#     eprl = epr.readlines()

# with open("temp.txt", "a") as t:
#     for idx, elem in enumerate(eprl):
#         l = elem.split(",")
#         win = int(l[9][0 : len(l[9]) - 1])
#         lose = int(l[10][0 : len(l[10]) - 1])

#         s = l[0] + "," + l[1] + "," + str(round(win / (win + lose) * 100, 6)) + "," + l[11][0 : len(l[11]) - 3]
#         t.write(s)
#         t.write("\n")
