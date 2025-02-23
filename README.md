# closest-neighbor
Playing around with some big data algorithms and techniques.
In this project, I will attemp to find the closest neighbor of each node in the dataset using signature similarities and the HSM algorithm.

## Datasets used: Bags-of-words text collection
For each text dataset in the collection: 
* D is the number of documents, 
* W is the number of words in the vocabulary, and 
* N is the total number of words

## The routines
###  MyReadDataRoutine
This routine processes the raw data into a list of frozensets. The W varriable is stored for later use siince we will need it later for the production of the permutation.
``` Python
list1 = frozenset(['apple','banana','milk'])
list2 = frozenset(['bread','apple'])
list3 = frozenset(['milk','flour','oranges','diapers'])

t_keys = [list1,list2,list3]
dictOfFrozensets = {t_keys[i]: i+1 for i in range(len(t_keys))}
```

###   MyJacSimWithSets and MyJacSimWithOrderedList
How Jaccard Similarity metric measures the similarity between two sets of data.

![image](https://github.com/user-attachments/assets/de60fc48-3134-4604-9ad7-cf60367eaba8)

``` Python
s1 = set(L1)
s2 = set(L2)
# the number of members shared between both sets
inters = len(s1.intersection(s2))
# the total number of members in both sets
un = len(s1.union(s2))

print("Intersection: {}".format(inters))
print("Union: {}".format(un))
print("Jaccard Similarity: {}".format(inters/un))
```

Both of these routines calculate the Jaccard Similarity with two different methods. MyJacSimWithSets uses a simple for-loop while calculates the similarity with sorted lists.

###  MySigSim
###  MyMinHash
This routine creates a 0/1 registry named wordlist. To create the registry, NumPy python library was used 
