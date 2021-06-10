from os import read


with open('Problem2\positive.txt', 'r') as p:
    positive = p.read()
    p.close()

with open('Problem2\\negative.txt', 'r') as n:
    negative = n.read()
    n.close()

def getPositive():
    return positive.split(',  ')

def getNegative():
    return negative.split(',    ')