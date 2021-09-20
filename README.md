# Subnetwork Visualization

## DESCRIPTION:
Input is two tab-delimited files named 'Input.gmt' and 'STRING.txt'. Input.gmt is a tab-delimited file formatted as
Broad Institute’s Gene Matrix Transformed (GMT). STRING.txt is a version of the STRING database of known and
predicted protein-protein interactions. Each line in the string file represents an edge in the network between the
protein genes formatted protein'\t'protein'\t'weight'\n' where weight is the strength of their functional similarity.
Output is the subnetwork of these two files output as a (Simple Interaction Format)SIF tab-delimited text file. The
output network is all the genes from the Input GMT file using the STRING file to determine edges and weights. The output
file can be loaded into Cytoscape as a network.

## INSTALL:
numpy~=1.21.1
operator
reduce from functools

## USAGE:
python 3.9.5

## INPUT:
1. Input.gmt
- 12 disjoint gene sets
- tab-delimited file Input.gmt
- format: (https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats/)
2. STRING.txt
- STRING database of known and predicted protien-protien interactions
- tab delimited
- each line represents an edge in network btwn two genes
- weighted by strength of functional similarity

## GOAL:

Display the functional network among Fanconi Anemia genes using Cytoscape

## OUTPUT:
- Simple Interaction File (SIF) Cytoscape format
- read in Cytoscape for network visualization
- format: (https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats/).


# WRITEUP:

## Motivating Problem from Domain:
// TODO

## Computational Problem Formulation:
//TODO

## Specific Approach to the Problem (i.e choice of algorithm):
//TODO

## Specific Implementation of Approach:
//TODO




