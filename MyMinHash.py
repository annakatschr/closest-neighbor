import numpy as np
import random


def create_random_hash_function(p=2**33-355, m=2**32-1):
    a = random.randint(1,p-1)
    b = random.randint(0, p-1)
    return lambda x: 1 + (((a * x + b) % p) % m)


def createRandomHash(W): # W is the total number of words in the vocab
    h = create_random_hash_function()
    randomHash = {x: h(x) for x in range(W)}
   # print('RandomHash: ', randomHash)
    myHashKeysOrderedByValues = sorted(randomHash, key=randomHash.get)
    myDict = {myHashKeysOrderedByValues[x]: x for x in range(W)}
    return myDict


# dimension of array W x numofDocument
def myMinHash(documentsList, K, W):  # k is the number of permutations

    # create numpy empty with zeros
    numDocuments = len(documentsList)
    wordlist = np.zeros((W, numDocuments))
    SIG = np.full((K, numDocuments), np.inf)

    for i in range(numDocuments):
        # i is the document id (+1)
        frozen = documentsList[i]  # this is one frozenset
        for x in frozen:
            wordlist[int(x), i] = 1

    for row in range(W):
        for col in range(numDocuments):
            if wordlist[row, col] == 1:
                for i in range(K):
                    hash_table = createRandomHash(W)
                    if hash_table[row] < SIG[i, col]:
                        SIG[i, col] = hash_table[row]

    return SIG
