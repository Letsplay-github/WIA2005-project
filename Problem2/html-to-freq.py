# html-to-freq-2.py

import obo
import text_scrape

link = 'https://www.thestar.com.my/news/nation/2020/09/08/pos-malaysias-sendparcel-to-hit-record-breaking-two-million-parcels-monthly'

fullwordlist = text_scrape.extractWord(link)

stopwordlist = obo.listStopwords(fullwordlist, obo.stopwords)
positivewordlist = obo.listPositivewords(fullwordlist, obo.positivewords)
negativewordlist = obo.listNegativewords(fullwordlist, obo.negativewords)
neutralwordlist = obo.listNeutralwords(fullwordlist, obo.stopwords, obo.positivewords, obo.negativewords)

swdictionary = obo.wordListToFreqDict(stopwordlist)
pwdictionary = obo.wordListToFreqDict(positivewordlist)
negwdictionary = obo.wordListToFreqDict(negativewordlist)
neuwdictionary = obo.wordListToFreqDict(neutralwordlist)

sortedswdict = obo.sortFreqDict(swdictionary)
sortedpwdict = obo.sortFreqDict(pwdictionary)
sortednegwdict = obo.sortFreqDict(negwdictionary)
sortedneuwdict = obo.sortFreqDict(neuwdictionary)

print("Stopwords")
for s in sortedswdict: print(str(s))

print("Positivewords")
for s in sortedpwdict: print(str(s))

print("Negativewords")
for s in sortednegwdict: print(str(s))

print("Neutralwords")
for s in sortedneuwdict: print(str(s))