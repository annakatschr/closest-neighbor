def MyReadDataRoutine(filename, numDocuments):
    fp = open(filename, 'r')

    counter = 1
    list_of_frozens = []
    words = []
    next(fp)
    W = next(fp)
    next(fp)

    for line in fp:
        line = line.split()

        if counter == numDocuments + 1:
            break

        if counter == int(line[0]):
            words.append(line[1])
            continue
        else:
            current_frozen = frozenset(words)
            list_of_frozens.append(current_frozen)
            words.clear()  # clear the words out of the list for the previous document
            words.append(line[1])  # we get a new document
            counter += 1

    fp.close()
    return list_of_frozens, W


def getDictionary(frozens):
    dictOfFrozensets = {frozens[i]: i + 1 for i in range(len(frozens))}
    print('\nDictionary of frozensets as keys: ', dictOfFrozensets)

