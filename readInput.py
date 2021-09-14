# assumptions:
#   input is tab delimited
#   first two indices in line should be thrown away
#   gene in 'locus for gene' will be repeated in the list
#   locus number is unimportant for network
#   gene interactions should be examined across and within all gene sets

# limitations:
#   gene interactions only shown if in STRING network
#   only known gene interactions and given genes
import operator
from functools import reduce

import numpy as np

fileIn = 'Input.gmt.txt'
fI = open(fileIn, 'r')
genes = fI.read().strip().split('\n')
genes = [g.split('\t') for g in genes]

for g in genes:
    del g[0]
    del g[0]

genes = reduce(operator.add, genes)
print(genes)
