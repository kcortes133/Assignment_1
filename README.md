# Gene Subnetwork Visualization

## DESCRIPTION:
Input is two tab-delimited files named 'Input.gmt' and 'STRING.txt'. Input.gmt is a tab-delimited file formatted as
Broad Institute’s Gene Matrix Transformed (GMT). STRING.txt is a version of the STRING database of known and
predicted protein-protein interactions. Each line in the string file represents an edge in the network between the
protein genes formatted protein'\t'protein'\t'weight'\n' where weight is the strength of their functional similarity.
Output is the subnetwork of these two files output as a (Simple Interaction Format)SIF tab-delimited text file. The
output network is all the genes from the Input GMT file using the STRING file to determine edges and weights. The output
file can be loaded into Cytoscape as a network.

## GOAL:

Display the functional network among Fanconi Anemia genes using Cytoscape

## INSTALL:
python 3.9.5

## USAGE:
```python
import operator
from functools import reduce
from main import *


# define input files
stringFile = 'STRING.txt'
fileIn = 'Input.gmt.txt'
# define output file
outFile = 'outSIF.txt'
# get genes from GMT file
genes = readInput(fileIn)
# get interactions from STRING file
interactionsNetwork = makeInteractionNetwork(stringFile)
# make subnetwork of input genes with interactions from STRING file
geneInteractions = makeNetwork(genes, interactionsNetwork)
# write subnetwork to file
makeNetworkSIF(geneInteractions, outFile)

```

## INPUT:
1. Input.gmt
- disjoint gene sets
- tab-delimited file Input.gmt
- First two columns describe row of gene set
- format: (https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats/)
2. STRING.txt
- STRING database of known and predicted protein-protein interactions
- tab-delimited
- each line represents an edge in network between two genes
- weighted by strength of functional similarity

## OUTPUT:
- Simple Interaction File (SIF) Cytoscape format
- Can be read in Cytoscape for network visualization
- format: (https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats/).
