import time
import numpy as np
from MySigSim import mySigSim
from MyJaccardSim import MyJacSimWithSets
from MyJaccardSim import MyJacSimWithOrderedList

AvgSimList = []
docDistancesDict = dict()
myNeighborsDict = dict()

# raw violence method
# using the SigSimilarity
def calculateNumNeighborsWithSIGSIM(SignatureMatrix, numDocuments, numPermutations):

    for doc1 in range(numDocuments):
        for doc2 in range(numDocuments):
            if doc1 == doc2:
                continue

            similarity = mySigSim(SignatureMatrix, doc1, doc2, numPermutations)
            if doc1+1 in docDistancesDict.keys():
                docDistancesDict[doc1 + 1].append(1 - similarity)
                myNeighborsDict[doc1+1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append(similarity)
                docDistancesDict[doc1 + 1] = temp_list
                myNeighborsDict[doc1+1] = temp_list2


    sorted_distances1 = {k: v for k, v in sorted(docDistancesDict.items(), key=lambda item: item[1])}
    print('Sorted dict by values: ', sorted_distances1)
    docDistancesDict.clear()


# raw violence method
# using the Jaccard Similarity
def calculateNumNeighborsWithJSIM(SignatureMatrix, numDocuments, numPermutations):

    SignatureMatrix = np.transpose(SignatureMatrix)

    for doc1 in range(numDocuments):
        for doc2 in range(numDocuments):
            if doc1 == doc2:
                continue
            similarity = MyJacSimWithSets(SignatureMatrix[doc1], SignatureMatrix[doc2])
            if doc1+1 in docDistancesDict.keys():
                docDistancesDict[doc1 + 1].append(1 - similarity)
                myNeighborsDict[doc1+1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append(similarity)
                docDistancesDict[doc1 + 1] = temp_list
                myNeighborsDict[doc1+1] = temp_list2

    sorted_distances2 = {k: v for k, v in sorted(docDistancesDict.items(), key=lambda item: item[1])}
    print('Sorted dict by values: ', sorted_distances2)

    # ---------------------------------------------------------------------------------
    docDistancesDict.clear()
    jsim2_time = 0
    for doc1 in range(numDocuments):
        for doc2 in range(numDocuments):
            if doc1 == doc2:
                continue

            similarity = MyJacSimWithOrderedList(SignatureMatrix[doc1], SignatureMatrix[doc2])
            if doc1+1 in docDistancesDict.keys():
                docDistancesDict[doc1 + 1].append(1 - similarity)
                myNeighborsDict[doc1+1].append(similarity)
            else:
                temp_list = []
                temp_list2 = []
                temp_list.append(1 - similarity)
                temp_list2.append(similarity)
                docDistancesDict[doc1 + 1] = temp_list
                myNeighborsDict[doc1+1] = temp_list2
    """
    print('===============================================')
    print('METHOD: JACCARD SIMILARITY WITH ORDERED LISTS')
    print('-----------------------------------------------')
    print("Jaccard Similarity: {}".format(similarity))
    print("EXECUTION TIME = %s seconds" % (time.time() - start_t)
    print('===============================================')
    """
    sorted_distances3 = {k: v for k, v in sorted(docDistancesDict.items(), key=lambda item: item[1])}
    print('Sorted dict by values: ', sorted_distances3)


def calculateAvgSim(numDocuments):
    # add the numneighbors paramrters
    # first calculate the average
    sorted_neighbors = {k: v for k, v in sorted(myNeighborsDict.items(), key=lambda item: item[1])}
    print('mynumneighbors: ', sorted_neighbors)
    for distance in sorted_neighbors:
        temp_list = sorted_neighbors[distance]
        AvgSimList.append(sum(temp_list)/len(temp_list))

    AvgSim = (1 / numDocuments) * sum(AvgSimList)
    return AvgSim

