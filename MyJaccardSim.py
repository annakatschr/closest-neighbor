
# docID1 and docID2 are frozensets
def getIntersection2loops(docID1, docID2):
    global comparisons, totalTime
    intersectionCounter = 0
    for doc1 in docID1:
        for doc2 in docID2:
            if doc1 == doc2:
                intersectionCounter += 1
            else:
                continue
    return intersectionCounter


def getIntersectionFaster(docID1, docID2):

    pos1 = 0
    pos2 = 0
    intersectionCounter = 0

    docID1 = sorted(docID1)
    docID2 = sorted(docID2)

    lenDoc1 = len(docID1)
    lenDoc2 = len(docID2)

    while pos1 < lenDoc1 and pos2 < lenDoc2:
        if docID1[pos1] == docID2[pos2]:
            intersectionCounter += 1
            pos1 += 1
            pos2 += 1
        else:
            if docID1[pos1] < docID2[pos2]:
                pos1 += 1
            else:
                pos2 += 1

    # print("Intersection: {}".format(intersectionCounter))

    return intersectionCounter


def getUnion(type, docID1, docID2):
    len_of_sets = len(set(docID1)) + len(set(docID2))
    if type == '2loop':
        intersection = getIntersection2loops(docID1, docID2)
        union = len_of_sets - intersection
     #   print("Union: {}".format(union))
        return union
    elif type == 'faster':
        intersection = getIntersectionFaster(docID1, docID2)
        union = len_of_sets - intersection
    #    print("Union: {}".format(union))
        return union


def MyJacSimWithSets(docID1, docID2):
    result = getIntersection2loops(docID1, docID2) / getUnion('2loop', docID1, docID2)
  #  print("Jaccard Similarity: {}".format(result))
    return result


def MyJacSimWithOrderedList(docID1, docID2):
    result = getIntersectionFaster(docID1, docID2) / getUnion('faster', docID1, docID2)
   # print("Jaccard Similarity: {}".format(result))
    return result