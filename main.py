# Author: Katherina Cortes
# Date: September 9, 2021
# Purpose: Take a tab delimited .gmz file of gene sets, a given tab-delimited STRING file
#   create a sub network of the gene interactions from the input file using the STRING file

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import operator, json
from functools import reduce
import ipycytoscape as cy

#

# assumptions:
#   input is tab delimited
#   first two indices in line should be thrown away
#   gene in 'locus for gene' will be repeated in the list
#   locus number is unimportant for network
#   gene interactions should be examined across and within all gene sets

# limitations:
#   gene interactions only shown if in STRING network
#   only known gene interactions and given genes
def readInput():
    fileIn = 'Input.gmt.txt'
    fI = open(fileIn, 'r')
    genes = fI.read().strip().split('\n')
    genes = [g.split('\t') for g in genes]

    for g in genes:
        del g[0]
        del g[0]

    genes = genes
    genes = reduce(operator.add, genes)

    return genes


# assumptions:
#   input is organized as protien'\t'protien'\t'weight'\n'
#   protien1:protien2:weight is also represented in the list as protien2:protien1:weight

#   limitations:
#   dictionary wouldnt work if the protien:protien interaction was only represented once


def makeInteractionNetwork(stringFile):
    # dictionary of dictionary 1st protien : 2nd protien: weight
    interactions = {}
    with open(stringFile, 'r') as f:
        for w, i in enumerate(f):
            gene1, gene2, weight = i.strip('\n').split('\t')
            if gene1 in interactions:
                interactions[gene1][gene2] = weight
            else:
                interactions[gene1] = {gene2: weight}
    return interactions


def makeNetwork(genes, interactionsNetwork):
    geneInteractions = {}
    genesTemp = list(genes)
    for gene1 in genesTemp:
        # input gene1 check if connected to any other gene
        geneInteractions[gene1] = {}
        for gene2 in genes:
            if gene1 in interactionsNetwork:
                if gene2 in interactionsNetwork[gene1]:
                    if gene2 in geneInteractions:
                        # make sure not to duplicate
                        if gene1 not in geneInteractions[gene2]:
                            geneInteractions[gene1][gene2] = interactionsNetwork[gene1][gene2]
    return geneInteractions


def makeNetworkJSON(geneInteractions, outFile):
    cytoscapeData = {
        'elements': {
            'nodes': [

            ],
            'edges': [

            ]
        }

    }

    for gene in geneInteractions:
        node = {'data': {'id': gene}}
        cytoscapeData['elements']['nodes'].append(node)
        for interaction in geneInteractions[gene]:
            print(interaction)
            weight = geneInteractions[gene][interaction]
            edge = {'data': {'id': weight, 'source': gene, 'target': interaction}}
            cytoscapeData['elements']['edges'].append(edge)
    print(cytoscapeData)

    with open(outFile, 'w') as out:
        json.dump(cytoscapeData, out)

    return


# Assumptions:
#
# Limitations:
#   large gene interaction dictionaries will take a long time to process
#   SIF files dont give weight information beyone naming them with string
#

def makeNetworkSIF(geneInteractions, outF):
    sifFile = open(outF, 'w')
    sifFile.write('Gene1' + '\t' + 'weight' + '\t' + 'Gene2' + '\n')
    countN = 0

    for gene in geneInteractions:
        if not geneInteractions[gene]:
            sifFile.write(gene + '\n')
            countN += 1
        for interaction in geneInteractions[gene]:
            weight = geneInteractions[gene][interaction]
            # how to deal with duplicates

            sifFile.write(gene + '\t' + weight +'\t' + interaction + '\n')
    sifFile.close()
    print(countN)

    return


def main():
    stringFile = 'STRING.txt'
    genes = readInput()
    interactionsNetwork = makeInteractionNetwork(stringFile)
    geneInteractions = makeNetwork(genes, interactionsNetwork)
    makeNetworkSIF(geneInteractions, 'outSIFTest.txt')



# run the main function
main()
