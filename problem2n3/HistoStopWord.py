#Histogram Question 6(stop word count)
import matplotlib.pyplot as plt
import pandas as pd
import csv
from frequency import deletedSW

with open(r'StopWordFreq.csv','w',encoding='UTF8',newline='') as updte:
    writer = csv.writer(updte)
    header = ['SWFreq']
    data = ['1','2','3','4','5']
    writer.writerow(header)
    for x in range (len(deletedSW)):
        while deletedSW[x]!= 0:
            writer.writerow(data[x])
            deletedSW[x]-=1
        x+=1

plt.style.use('fivethirtyeight')
data = pd.read_csv('StopWordFreq.csv')
Freq = data['SWFreq']
bins = [1,2,3,4,5,6]

plt.hist(Freq, bins, ec="black")

plt.title('Stop Word Frequency for every courier')
plt.xlabel('Courier ID')
plt.ylabel('Word Frequency')
plt.tight_layout()
plt.show()
