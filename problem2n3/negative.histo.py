import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('CountNPN.csv')
#cid = data['Courier_id']
nwc = data['Negative_word']

bins = [1,2,3,4,5,6]

#plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwards)
plt.hist(nwc, bins, ec="black")

plt.title('Negative Words Count by Courier ID')
plt.xlabel('Courier ID')
plt.ylabel('Negative Words Count')

plt.tight_layout()

plt.show()
