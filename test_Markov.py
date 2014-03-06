# test_Markov.py

from Markov import *


def makeWordModel(filename):
    infile = open(filename)
    model = Markov()
    for line in infile:
        words = line.split()
        for w in words:
            model.add(w)
    infile.close()
    #Add a sentinel at the end of the text
    model.add(None)
    model.reset()
    return model


def generateWordChain(markov, n):
    #generates up to n words of output from a model
    words = []
    for i in range(n):
        nxt = markov.randomNext()
        if nxt is None:
            break
        words.append(nxt)
    return " ".join(words)


a = makeWordModel("loveletter.txt")

print(generateWordChain(a, 100))