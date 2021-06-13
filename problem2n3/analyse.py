from frequency import withoutStop
from mainCountPN import pw, nw

courier = ["City-Link Express", "Pos Laju", "GDEX", "J&T", "DHL"]
total = withoutStop
positive = pw
negative = nw
sentimentPoints = [0 for i in range(len(courier))]

# formula = (P − N) / (P + N + O)
for i in range(0, len(total)):
    sentimentPoints[i] = round((positive[i]-negative[i])/(positive[i]+negative[i]+total[i]), 5) 
print("Sentiment Analysis for every courier")
print(sentimentPoints)
print("")

dictSentiment = {}
for i in range(0, len(courier)):
    dictSentiment[sentimentPoints[i]] = courier[i]
print(dictSentiment)

# Sort using Quick Sort
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quickSort(arr, start, end):
    if start >= end:
        return

    piv = partition(arr, start, end)
    quickSort(arr, start, piv-1)
    quickSort(arr, piv+1, end)

quickSort(sentimentPoints, 0, len(sentimentPoints)-1)

print("")
print("Sorted Sentiment Analysis:")
print(sentimentPoints)
print("")
print("The courier who score highest point for sentiment analysis is", dictSentiment[sentimentPoints[len(sentimentPoints)-1]])

dictSentimentPoints = {}
for i in range(0, len(courier)):
    dictSentimentPoints[dictSentiment[sentimentPoints[i]]] = sentimentPoints[i]
print("Sentiment Analysis Result for Every Courier:")
print(dictSentimentPoints)
print("")
sentimentRank = []
for i in dictSentimentPoints.keys():
    sentimentRank.append(i)

