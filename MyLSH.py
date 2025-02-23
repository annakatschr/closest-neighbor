import math
import numpy as np
import random


def create_random_hash_function(p=2**33-355, m=2**32-1):
    a = random.randint(1,p-1)
    b = random.randint(0, p-1)
    return lambda x: 1 + (((a * x + b) % p) % m)
"""
sig = np.array([[ 124,  236,   14,  467,  230, 1673,  977,  684,  133,  394],
        [1069,  221,  2,   80,  586,  479, 3531,  277,  846,  757],
        [1546,  700,  296,  379,  106,   63, 3297,   53,  189, 1206],
        [1107,  282,  19,   61, 1009,   19,  750, 1604,  160,  366],
        [1108,   16,  477,  377,  323, 1472,  551,  897, 2346, 2429]])
"""
def myLSH(sig, rowsPerBands, numPermutations):
    sigMatrix = np.transpose(sig)
    numBands = math.floor(numPermutations/rowsPerBands)
    hashLSH = create_random_hash_function()

    for currentBand in range(numBands):
        LSHdicts = dict()
        if currentBand == numBands:
            break
        for docID in range(len(sigMatrix)):
            rowBandVector = []
            for row in range(rowsPerBands):
                rowBandVector.append(sigMatrix[docID][currentBand*rowsPerBands])

            rowBandVector = tuple(rowBandVector)
            hashedVector = hash(rowBandVector)
            LSHdicts[docID+1] = hashedVector

        # check the rows in the specific band for similarity
        for docid1 in LSHdicts:
            for docid2 in LSHdicts:
                #if docid1 == docid2:
                #    continue
                if LSHdicts[docid1] == LSHdicts[docid2]:
                    # hash them to the same bucket
                    LSHdicts[docid1] = hashLSH(LSHdicts[docid1])
                    LSHdicts[docid2] = hashLSH(LSHdicts[docid2])
        print('The buckets: ')
        print(LSHdicts)
        return LSHdicts


def sortLSHDict(LSHdict):
    sortedDict = {k: v for k, v in sorted(LSHdict.items(), key=lambda item: item[1])}
    return sortedDict


#print(sig)
#myLSH(sig, 2, 10)
