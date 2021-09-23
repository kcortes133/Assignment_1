from main import *


# check empty file
# check super small file

def testEmptyFile():
    stringFile = 'STRING.txt'
    fileIn = 'empty.txt'
    # define output file
    outFile = 'outEmptySIF.txt'
    # get genes from GMT file
    genes = readInput(fileIn)
    # get interactions from STRING file
    interactionsNetwork = makeInteractionNetwork(stringFile)
    # make subnetwork of input genes with interactions from STRING file
    geneInteractions = makeNetwork(genes, interactionsNetwork)
    print(geneInteractions)
    # write subnetwork to file
    makeNetworkSIF(geneInteractions, outFile)

    return

def testSmallInput():
    stringFile = 'STRING.txt'
    fileIn = 'testInput.gmt.txt'
    # define output file
    outFile = 'outTestSIF.txt'
    # get genes from GMT file
    genes = readInput(fileIn)
    # get interactions from STRING file
    interactionsNetwork = makeInteractionNetwork(stringFile)
    # make subnetwork of input genes with interactions from STRING file
    geneInteractions = makeNetwork(genes, interactionsNetwork)
    print(geneInteractions)
    # write subnetwork to file
    makeNetworkSIF(geneInteractions, outFile)

    return

testEmptyFile()
testSmallInput()