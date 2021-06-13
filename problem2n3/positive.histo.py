import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('CountPN.csv')
#cid = data['Courier_id']
pwc = data['Positive_word']

bins = [1,2,3,4,5,6]

#plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwards)
plt.hist(pwc, bins, ec="black")

plt.title('Positive Words Count by Courier ID')
plt.xlabel('Courier ID')
plt.ylabel('Positive Words Count')

plt.tight_layout()

plt.show()
