from MySigSim import mySigSim
from MyJaccardSim import MyJacSimWithSets
from MyJaccardSim import MyJacSimWithOrderedList
import numpy as np
import time

myNeighborsDict = dict()
docDistancesDict = dict()
AvgSimList = []
pairs = []

def getCandidates(candidates):
    for docid1 in candidates:
        for docid2 in candidates:
            if docid1 == docid2:
                continue
            if candidates[docid1] == candidates[docid2]:
                temp = []
                temp.append(candidates[docid1])
                temp.append(candidates[docid2])
                pairs.append(temp)

    print(pairs)


def calculateNumNeighborsWithLSHS_SigSim(sig, numPermutations):
    docDistancesDict.clear()
    for pair in pairs:
        temp = pairs[pair]
        if temp[0] == temp[1]:
            similarity = mySigSim(sig, temp[0], temp[1], numPermutations)

            if temp[0]+1 in docDistancesDict.keys():
                docDistancesDict[temp[0] + 1].append(1 - similarity)
                myNeighborsDict[temp[0] +1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append((similarity))
                docDistancesDict[temp[0] + 1] = temp_list
                myNeighborsDict[temp[0]+1] = temp_list2


def calculateNumNeighborsWithLSHS_JSim(sig):
    docDistancesDict.clear()
    SignatureMatrix = np.transpose(sig)
    start_time = time.time()
    for pair in pairs:
        temp = pairs[pair]
        if temp[0] == temp[1]:
            similarity = MyJacSimWithSets(SignatureMatrix[temp[0]], SignatureMatrix[temp[1]])

            if temp[0]+1 in docDistancesDict.keys():
                docDistancesDict[temp[0] + 1].append(1 - similarity)
                myNeighborsDict[temp[0] + 1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append(similarity)
                docDistancesDict[temp[0] + 1] = temp_list
                myNeighborsDict[temp[0]+1] = temp_list2

    print('===============================================')
    print('METHOD: JACCARD SIMILARITY WITH DOUBLE FOR-LOOP')
    print('-----------------------------------------------')
    print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
    print('===============================================')

    start_time = time.time()

    for pair in pairs:
        temp = pairs[pair]
        if temp[0] == temp[1]:
            similarity = MyJacSimWithOrderedList(SignatureMatrix[temp[0]], SignatureMatrix[temp[1]])

            if temp[0]+1 in docDistancesDict.keys():
                docDistancesDict[temp[0] + 1].append(1 - similarity)
                myNeighborsDict[temp[0] + 1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append(similarity)
                docDistancesDict[temp[0] + 1] = temp_list
                myNeighborsDict[temp[0]+1] = temp_list2

    print('===============================================')
    print('METHOD: JACCARD SIMILARITY WITH ORDERED LISTS')
    print('-----------------------------------------------')
    print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
    print('===============================================')


def calculateAvgSimLSH(numDocuments):

    sorted_neighbors = {k: v for k, v in sorted(myNeighborsDict.items(), key=lambda item: item[1])}
    print('mynumneighbors: ', sorted_neighbors)
    for distance in sorted_neighbors:
        temp_list = sorted_neighbors[distance]
        AvgSimList.append(sum(temp_list)/len(temp_list))

    AvgSim = (1 / numDocuments) * sum(AvgSimList)
    return AvgSim