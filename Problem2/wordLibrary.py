from os import read


with open('positive.txt', 'r') as p:
    positive = p.read()
    p.close()

with open('negative.txt', 'r') as n:
    negative = n.read()
    n.close()

def getPositive():
    return positive.split(',  ')

def getNegative():
    return negative.split(',    ')