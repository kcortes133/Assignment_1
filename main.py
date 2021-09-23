# Author: Katherina Cortes
# Date: September 9, 2021
# Purpose: Take a tab delimited .gmz file of gene sets, a given tab-delimited STRING file
#   create a sub network of the gene interactions from the input file using the STRING file
#   output a SIR tab-delimited file for input to cytoscape

import operator
from functools import reduce
import numpy as np


# assumptions:
#   input is tab delimited
#   first two indices in line should be thrown away
#   gene in 'locus for gene' will be repeated in the list
#   locus number is unimportant for network
#   gene interactions should be examined across and within all gene sets
#
# limitations:
#   gene interactions only shown if in STRING network
#   only known gene interactions and given genes
#
#   Returns a list of genes.
#   Expects a .txt tab-delimited file as input.
#   First two columns in file rows are discarded
#
#   @param fileIn file with genes to be read in
#   @return genes list of genes to check interactions for
def readInput(fileIn):
    # read in GMT file
    # separate file into list by tabs
    fI = open(fileIn, 'r')
    genes = fI.read().strip().split('\n')
    genes = [g.split('\t') for g in genes]

    # Delete first two columns
    for g in genes:
        del g[0]
        del g[0]

    # condense list of lists into one-dimensional list
    genes = reduce(operator.add, genes)

    return genes


# assumptions:
#   input is organized as protein'\t'protein'\t'weight'\n'
#   protein1:protein2:weight is also represented in the list as protein2:protein1:weight
#
#   limitations:
#   dictionary would not work if the protein:protein interaction was only represented once
#
#   Returns dictionary of protein interactions ordered protein:protein:weight
#   Expects tab-delimited STRING file as input
#
#   @param   stringFile STRING file of protein-protein interactions
#            organized as protein'\t'protein'\t'weight'\n'
#   @returns interactions dict of protein interactions

def makeInteractionNetwork(stringFile):
    # dictionary of dictionary 1st protein : 2nd protein: weight
    interactions = {}
    with open(stringFile, 'r') as f:
        for w, i in enumerate(f):
            gene1, gene2, weight = i.strip('\n').split('\t')
            if gene1 in interactions:
                interactions[gene1][gene2] = weight
            else:
                interactions[gene1] = {gene2: weight}
    return interactions



#   @param   genes list of genes to check interactions for (gotten from readInput(file))
#   @param   interactionsNetwork dict of protein-protein interactions from makeInteractionNetwork(stringFile)
#   @returns geneInteractions dict of gene interactions from input GMT file
def makeNetwork(genes, interactionsNetwork):
    geneInteractions = {}
    for gene1 in genes:
        # input gene1 check if connected to any other gene
        geneInteractions[gene1] = {}
        for gene2 in genes:
            if gene1 in interactionsNetwork:
                if gene2 in interactionsNetwork[gene1]:
                    if gene2 in geneInteractions:
                        # make sure not to duplicate edges
                        if gene1 not in geneInteractions[gene2]:
                            geneInteractions[gene1][gene2] = interactionsNetwork[gene1][gene2]
    return geneInteractions


# Limitations:
#   large gene interaction dictionaries will take a long time to process
#   SIF files dont give weight information beyone naming them with string
#
#   @param   geneInteractions dictionary of gene interactions generated from makeNetwork()
#   @param   outF string file name to write gene interactions dictionary to
#   @returns nothing
def makeNetworkSIF(geneInteractions, outF):
    sifFile = open(outF, 'w')
    sifFile.write('Gene1' + '\t' + 'weight' + '\t' + 'Gene2' + '\n')
    countN = 0

    for gene in geneInteractions:
        # if gene has no interactions write without edges
        if not geneInteractions[gene]:
            sifFile.write(gene + '\n')
            countN += 1
        # otherwise write genes with interactions in same line
        else:
            for interaction in geneInteractions[gene]:
                weight = geneInteractions[gene][interaction]
                sifFile.write(gene + '\t' + weight +'\t' + interaction + '\n')
    sifFile.close()
    return


def main():
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



# run the main function
main()
