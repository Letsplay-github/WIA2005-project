#Histogram Question 6(word count)
import matplotlib.pyplot as plt
import pandas as pd
import csv
from frequency import wordcount

with open(r'WordFreq.csv','w',encoding='UTF8',newline='') as updte:
    writer = csv.writer(updte)
    header = ['Freq']
    data = ['1','2','3','4','5']
    writer.writerow(header)
    for x in range (len(wordcount)):
        while wordcount[x]!= 0:
            writer.writerow(data[x])
            wordcount[x]-=1
        x+=1


plt.style.use('fivethirtyeight')


data = pd.read_csv('WordFreq.csv')
Freq = data['Freq']

bins = [1,2,3,4,5,6]

#plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwards)
plt.hist(Freq, bins, ec="black")

plt.title('Word Frequncy for every courier')
plt.xlabel('Courier ID')
plt.ylabel('Word Frequency')
plt.tight_layout()
plt.show()
