import time
import numpy as np

# assumptions:
#   input is organized as protien'\t'protien'\t'weight'\n'
#   protien1:protien2:weight is also represented in the list as protien2:protien1:weight

#   limitations:
#   dictionary wouldnt work if the protien:protien interaction was only represented once


start = time.time()

stringFile = 'STRING.txt'
# dictionary of dictionary 1st protien : 2nd protien: weight
interactions = {}
with open(stringFile, 'r') as f:
    for w, i in enumerate(f):
        gene1, gene2, weight = i.strip('\n').split('\t')
        if gene1 in interactions:
            interactions[gene1][gene2] = weight
        else:
            interactions[gene1] = {gene2: weight}
print(interactions)
total = time.time() - start
print('Done', total)





