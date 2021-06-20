from prob3ext import *
from analyse import sentimentRank

rankCustomer1 = []
rankCustomer2 = []
rankCustomer3 = []


#add element
for i in rankCust1.keys():
    rankCustomer1.append(i)

for i in rankCust2.keys():
    rankCustomer2.append(i)

for i in rankCust3.keys():
    rankCustomer3.append(i)



pointsCust1 = [0 for i in range(len(rankCustomer1))]
pointsCust2 = [0 for i in range(len(rankCustomer2))]
pointsCust3 = [0 for i in range(len(rankCustomer3))]



# adding point to courier based on distance for each customer
for i in range(0, len(rankCustomer1)):
    for j in range(0, len(courier)):

        if i == 0:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[i] += 5
                break
        if i == 1:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[i] += 4
                break
        if i == 2:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[i] += 3
                break
        if i == 3:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[i] += 2
                break
        if i == 4:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[i] += 1
                break

for i in range(0, len(rankCustomer2)):
    for j in range(0, len(courier)):
        if i == 0:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[i] += 5
                break
        if i == 1:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[i] += 4
                break
        if i == 2:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[i] += 3
                break
        if i == 3:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[i] += 2
                break
        if i == 4:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[i] += 1
                break

for i in range(0, len(rankCustomer3)):
    for j in range(0, len(courier)):
        if i == 0:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[i] += 5
                break
        if i == 1:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[i] += 4
                break
        if i == 2:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[i] += 3
                break
        if i == 3:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[i] += 2
                break
        if i == 4:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[i] += 1
                break


print("Sentiment Rank: ")
print(sentimentRank)
print("")

# adding point to courier based on sentiment for each customer
for i in range(0, len(sentimentRank)):
    for j in range(0, len(rankCustomer1)):
        if i == 0:
            if sentimentRank[i] == rankCustomer1[j]:
                pointsCust1[j] *= 2
                break
        if i == 1:
            if sentimentRank[i] == rankCustomer1[j]:
                pointsCust1[j] *= 4
                break
        if i == 2:
            if sentimentRank[i] == rankCustomer1[j]:
                pointsCust1[j] *= 6
                break
        if i == 3:
            if sentimentRank[i] == rankCustomer1[j]:
                pointsCust1[j] *= 8
                break
        if i == 4:
            if sentimentRank[i] == rankCustomer1[j]:
                pointsCust1[j] *= 10
                break

    for j in range(0, len(rankCustomer2)):
        if i == 0:
            if sentimentRank[i] == rankCustomer2[j]:
                pointsCust2[j] *= 2
                break
        if i == 1:
            if sentimentRank[i] == rankCustomer2[j]:
                pointsCust2[j] *= 4
                break
        if i == 2:
            if sentimentRank[i] == rankCustomer2[j]:
                pointsCust2[j] *= 6
                break
        if i == 3:
            if sentimentRank[i] == rankCustomer2[j]:
                pointsCust2[j] *= 8
                break
        if i == 4:
            if sentimentRank[i] == rankCustomer2[j]:
                pointsCust2[j] *= 10
                break

    for j in range(0, len(rankCustomer3)):
        if i == 0:
            if sentimentRank[i] == rankCustomer3[j]:
                pointsCust3[j] *= 2
                break
        if i == 1:
            if sentimentRank[i] == rankCustomer3[j]:
                pointsCust3[j] *= 4
                break
        if i == 2:
            if sentimentRank[i] == rankCustomer3[j]:
                pointsCust3[j] *= 6
                break
        if i == 3:
            if sentimentRank[i] == rankCustomer3[j]:
                pointsCust3[j] *= 8
                break
        if i == 4:
            if sentimentRank[i] == rankCustomer3[j]:
                pointsCust3[j] *= 10
                break

print("Points before sorting: ")
print("Customer 1: ",pointsCust1)
print("Customer 2: ",pointsCust2)
print("Customer 3: ",pointsCust3)

dictFinalCust1 = {}
dictFinalCust2 = {}
dictFinalCust3 = {}

for i in range(len(rankCustomer1)):
    dictFinalCust1[pointsCust1[i]] = rankCustomer1[i]

for i in range(len(rankCustomer2)):
    dictFinalCust2[pointsCust2[i]] = rankCustomer2[i]

for i in range(len(rankCustomer3)):
    dictFinalCust3[pointsCust3[i]] = rankCustomer3[i]

quickSort(pointsCust1, 0, len(pointsCust1)-1)
quickSort(pointsCust2, 0, len(pointsCust2)-1)
quickSort(pointsCust3, 0, len(pointsCust3)-1)

print("")
print("Points  after sorting: ")
print("Customer 1: ",pointsCust1)
print("Customer 2: ",pointsCust2)
print("Customer 3: ",pointsCust3)

print("")
print("Recommended Courier from Customer 1 based on rank: ")
rank = 1
for i in range(len(pointsCust1)-1, -1, -1):
    print(rank,"-",dictFinalCust1[pointsCust1[i]])
    rank+=1

print("")
print("Recommended Courier from Customer 2 based on rank: ")
rank = 1
for i in range(len(pointsCust2)-1, -1, -1):
    print(rank,"-",dictFinalCust2[pointsCust2[i]])
    rank+=1

print("")
print("Recommended Courier from Customer 3 based on rank: ")
rank = 1
for i in range(len(pointsCust3)-1, -1, -1):
    print(rank,"-",dictFinalCust3[pointsCust3[i]])
    rank+=1











