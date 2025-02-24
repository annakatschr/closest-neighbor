# closest-neighbor
In this project, I have implemented the LSH and MinHash algorithms and compared their quality and execution times where the objective is to calculate the nearest neighbors of a document X included in a 
collection of documents.
The assessment of similarity of the other documents from document X will be done in two main ways:
* The Jaccard-Similarity 𝐽𝑎𝑐𝑆𝑖𝑚(𝑋, 𝑌) metric of document X, where Y are the rest of the documents in the dataset.
* The signature similarity 𝑆𝑖𝑔𝑆𝑖𝑚(𝑋, 𝑌) of document X, where Y are the rest of the documents in the dataset.
  
## Datasets used: Bags-of-words text collection
The nodes in these datasets represent documents. We want to find the similarity between these documents.
For each text dataset in the collection: 
* D is the number of documents, 
* W is the number of words in the vocabulary, and 
* N is the total number of words

## The "Signature Generation" routines
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
The Jaccard similarity is a measure of how similar two sets are, defined as the ratio of the intersection of the sets to the union of the sets:
![image](https://github.com/user-attachments/assets/de60fc48-3134-4604-9ad7-cf60367eaba8)

Both of these routines calculate the Jaccard Similarity with two different methods. **MyJacSimWithSets** uses a simple for-loop while **MyJacSimWithOrderedLis**t calculates the Jaccard similarity with ordered lists, making for more efficient execution times.

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

###  MySigSim
This routine calculates the signature similarity between two documents. This is done by comparing the lines of the Signature Matrix of each document and dividing their union with the number of permutations.

###  MyMinHash
This routine implements a MinHash Algorith. Min Hash uses hash functions to generate a "signature" for each set. Each hash function provides a compressed, unique representation of the set.
Bellow is the hash algorith used in this project.
``` Python
def create_random_hash_function(p=2**33-355, m=2**32-1):
    a = random.randint(1,p-1)
    b = random.randint(0, p-1)
    return lambda x: 1 + (((a * x + b) % p) % m)
```
The signature matrix is created with dimentions K(number of permutations) x N (number of documents)

## The "Calculation of closest neighbor per document" routines
* Brute-Force Method
  * calculateNumNeighborsWithSIGSIM, calculateNumNeighborsWithJSIM and 
    calculateAvgSim.
* LSH Method
  * myLSH, calculateNumNeighborsWithLSHS_SigSim and
    calculateNumNeighborsWithLSHS_JSim

### Execution times for each algorith used

| Seconds       | Brute-Force           | LSH                   |
|---------------|-----------------------|-----------------------|
| Jaccard Sim   | 0.0033218860626220703 | 3.0872836112976074    |
| Signature Sim | 0.0006268024444580078 | 0.0006077289581298828 |

## Usage
Execute main.py
![image](https://github.com/user-attachments/assets/1b24c112-0c36-4f0f-8497-999b06c56c27)
![image](https://github.com/user-attachments/assets/7751d586-8dc5-48bf-9473-ca030598707d)


