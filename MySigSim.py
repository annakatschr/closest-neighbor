def mySigSim(SignatureMatrix, docID1, docID2, numPermutation):

    similarity_counter = 0
    for row in range(numPermutation):
        if SignatureMatrix[row, docID1-1] == SignatureMatrix[row, docID2-1]:
            similarity_counter += 1

    return similarity_counter/numPermutation



