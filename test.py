# proficiencyList = None
# temp_proficiency_list = None
# tempList = None

# with open("./proficiency.txt", "r") as proficiency:
#     proficiencyList = proficiency.readlines()

# with open("./temp_proficiency.txt", "r") as record:
#     temp_proficiency_list = record.readlines()

# with open("./temp.txt", "a") as temp:
#     tempList = temp.readlines()


# # 똑같으면 false
# def isequals(recordGame, tempgame):
#     iss = False
#     for idx in range(0, 10):
#         if not (recordGame[idx].split(",")[1] == tempgame[idx].split(",")[1]):
#             iss = True
#     return iss


# result = []

# for idx in range(0, len(temp_proficiency_list), 10):
#     onegame = temp_proficiency_list[idx : idx + 10]
#     rr = True
#     for idx2 in range(0, len(alreadyrecordList), 10):
#         temponegame = alreadyrecordList[idx2 : idx2 + 10]
#         r = isequals(onegame, temponegame)
#         if r == False:
#             rr = False
#             break
#     if rr == True:
#         result.extend(onegame)
# print(len(result))

# with open("heheeh.txt", "a") as asdf:
#     for ind, elem in enumerate(result):
#         asdf.write(elem)


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

# with open("temp_proficiency.txt", "r") as epr:
#     eprl = epr.readlines()

# with open("temp.txt", "a") as t:
#     for idx in range(0, len(eprl), 10):
#         tempeprl = eprl[idx : idx + 10]
#         templist = []
#         for idx2, elem2 in enumerate(tempeprl):
#             linesplit = elem2.split(",")
#             if not len(linesplit) <= 3:
#                 cn = linesplit[1]
#                 win = int(linesplit[2][0 : len(linesplit[2]) - 1])
#                 lose = int(linesplit[3][0 : len(linesplit[3]) - 1])
#                 y = "LOSE" if idx2 <= 4 else "WIN"
#                 s = y + "," + linesplit[1] + "," + str(round(win / (win + lose) * 100, 6)) + "," + linesplit[4][0 : len(linesplit[4]) - 3]
#                 templist.append(s)
#         if len(templist) == 10:
#             for i, e in enumerate(templist):
#                 t.write(e)
#                 t.write("\n")


champList = []
XtrainList = []
with open("cn.txt", "r") as cntxt:
    l = cntxt.readlines()
    for idx, elem in enumerate(l):
        s = elem.split(",")
        champList.append(s[1].rstrip())

with open("yyyy.txt", "r") as xtrain:
    XtrainList = xtrain.readlines()

with open("Xtest.txt", "a") as xxx:
    with open("Ytest.txt", "a") as ytrain:
        for idx in range(0, len(XtrainList), 10):
            one = XtrainList[idx : idx + 10]
            onehot = [0] * 163
            for idxx in range(0, 5):
                onehot[champList.index(one[idxx].split(",")[1])] = 1
            for idxx in range(5, 10):
                onehot[champList.index(one[idxx].split(",")[1])] = 2
            for idxx in range(0, 10):
                onehot.append(one[idxx].split(",")[2])
                onehot.append(one[idxx].split(",")[3].rstrip())
            xxx.write(str(onehot))
            xxx.write("\n")
            if one[0].split(",")[0] == "LOSE":
                ytrain.write("[0,1]")
                ytrain.write("\n")
            else:
                ytrain.write("[1,0]")
                ytrain.write("\n")
