from Preprocessing import MyReadDataRoutine
from MyMinHash import myMinHash
from BruteForceAvgSim import calculateNumNeighborsWithSIGSIM
from BruteForceAvgSim import calculateNumNeighborsWithJSIM
from BruteForceAvgSim import calculateAvgSim
from LSHAvgSim import calculateNumNeighborsWithLSHS_JSim
from LSHAvgSim import calculateNumNeighborsWithLSHS_SigSim
from LSHAvgSim import calculateAvgSimLSH
from LSHAvgSim import getCandidates
from MyJaccardSim import MyJacSimWithSets
from MyJaccardSim import MyJacSimWithOrderedList
from MyLSH import myLSH
import time
import numpy as np

# ADD COMMENTS FOR USAGE HERE
"""
sig = np.array([[ 124,  236,   14,  467,  230, 1673,  977,  684,  133,  394],
        [1069,  221,  2,   80,  586,  479, 3531,  277,  846,  757],
        [1546,  700,  296,  379,  106,   63, 3297,   53,  189, 1206],
        [1107,  282,  19,   61, 1009,   19,  750, 1604,  160,  366],
        [1108,   16,  477,  377,  323, 1472,  551,  897, 2346, 2429]])
"""
def main():
    print('\n====================  ALGORITHMS FOR BIG DATA - FINDING SIMILAR ITEMS ==================== \n')
    print('*** File Menu ***')
    print('1. DATA_1-docword.enron.txt')
    print('2. DATA_2-docword.nips.txt\n')
    filename = input("Enter choose a file name: ")
    numDocuments = int(input("Enter the number of documents you would like to process: "))
    numNeighbors = int(input("Enter the number of neighbors for each documents\n(The number should be a small integer ex. 1, 2, 4): "))
    my_tuple = MyReadDataRoutine(filename, numDocuments)
    documentList = my_tuple[0]
    W = my_tuple[1]

    numPermutations = int(input("Enter the number of permutations for the creation of the Signatures: "))
    print('Please wait until the program processes the file and creates the Signature Matrix...')
    sig = myMinHash(documentList, numPermutations, int(W))
    print(sig)
    while True:
        similarity = input("Would you like to use the Jaccard or the Signature similarity method?(jac/sig): ")
        method = input("Would you like to use BruteForce or the LSH method?(brute/lsh): ")

        if similarity == "jac":
            print('===========================================')
            print('COMPUTATION OF JSIM BEGINS(A,B): ')
            if method == "brute":
                start_time = time.time()
                calculateNumNeighborsWithJSIM(sig, numDocuments, numPermutations)
                avg = calculateAvgSim(numDocuments)
                print('===============================================')
                print('METHOD: JACCARD SIMILARITY AND BRUTE FORCE')
                print('-----------------------------------------------')
                print("Average Similarity: {}".format(avg))
                print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
                print('===============================================')
                break
            elif method == "lsh":
                start_time = time.time()
                rowsPerBand = int(input("Give the rows per band LSH will use: "))
                candidates = myLSH(sig, rowsPerBand, numPermutations)
                getCandidates(candidates)
                calculateNumNeighborsWithLSHS_JSim(sig)
                avg = calculateAvgSimLSH(numDocuments)
                print('===============================================')
                print('METHOD: JACCARD SIMILARITY AND LSH')
                print('-----------------------------------------------')
                print("Average Similarity: {}".format(avg))
                print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
                print('===============================================')
                break

        elif similarity == "sig":
            print('===========================================')
            print('COMPUTATION OF SIGSIM BEGINS(A,B): ')
            if method == "brute":
                start_time = time.time()
                calculateNumNeighborsWithSIGSIM(sig, numDocuments, numPermutations)
                avg = calculateAvgSim(numDocuments)
                print('===============================================')
                print('METHOD: SIGNATURE SIMILARITY AND BRUTE FORCE')
                print('-----------------------------------------------')
                print("Average Similarity: {}".format(avg))
                print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
                print('===============================================')
                break
            elif method == "lsh":
                print('===========================================')
                print('COMPUTATION OF LSH BEGINS: ')
                rowsPerBand = int(input('Enter the number of rows per band: '))
                start_time = time.time()
                candidates = myLSH(sig, rowsPerBand, numPermutations)
                getCandidates(candidates)
                calculateNumNeighborsWithLSHS_SigSim(sig,numPermutations)
                avg = calculateAvgSimLSH(numDocuments)
                print('===============================================')
                print('METHOD: SIGNATURE SIMILARITY AND LSH')
                print('-----------------------------------------------')
                print("Average Similarity: {}".format(avg))
                print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
                print('===============================================')
                break

        else:
            print("You can only choose between jac and sig. Try again.")
            continue

    while True:
        answer = input("Would you like to check a specific pair of documents for similarity?(y/n): ")
        if answer == "y":
            docID1 = int(input("Give the docID1 name: "))
            docID2 = int(input("Give the docID2 name: "))
            # add the execution times for comparison
            start_time = time.time()
            similarity = MyJacSimWithSets(sig[docID1], sig[docID2])
            print('===============================================')
            print('METHOD: JACCARD SIMILARITY WITH DOUBLE FOR-LOOP')
            print('-----------------------------------------------')
            print("Jaccard Similarity: {}".format(similarity))
            print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
            print('===============================================')
            start_time = time.time()
            similarity = MyJacSimWithOrderedList(sig[docID1], sig[docID2])
            print('===============================================')
            print('METHOD: JACCARD SIMILARITY WITH ORDERED LISTS')
            print('-----------------------------------------------')
            print("Jaccard Similarity: {}".format(similarity))
            print("EXECUTION TIME = %s seconds" % (time.time() - start_time))
            print('===============================================')
            break
        elif answer == "n":
            print('Exiting Program...')
            break
        else:
            print("Only 'y' or 'n' are permitted. Try again!")
            continue


main()
