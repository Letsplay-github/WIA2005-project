from mark import *
from analyse import sentimentRank

rankCustomer1 = []
rankCustomer2 = []
rankCustomer3 = []

for i in rankCust1.keys():
    rankCustomer1.append(i)

for i in rankCust2.keys():
    rankCustomer2.append(i)

for i in rankCust3.keys():
    rankCustomer3.append(i)

pointsCust1 = [0 for i in range(len(rankCustomer1))]
pointsCust2 = [0 for i in range(len(rankCustomer2))]
pointsCust3 = [0 for i in range(len(rankCustomer3))]

for i in range(0, len(rankCustomer1)):
    for j in range(0, len(courier)):
        if i == 0:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[j] += 5
                break
        if i == 1:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[j] += 4
                break
        if i == 2:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[j] += 3
                break
        if i == 3:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[j] += 2
                break
        if i == 4:
            if rankCustomer1[i] == courier[j]:
                pointsCust1[j] += 1
                break

for i in range(0, len(rankCustomer2)):
    for j in range(0, len(courier)):
        if i == 0:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[j] += 5
                break
        if i == 1:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[j] += 4
                break
        if i == 2:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[j] += 3
                break
        if i == 3:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[j] += 2
                break
        if i == 4:
            if rankCustomer2[i] == courier[j]:
                pointsCust2[j] += 1
                break

for i in range(0, len(rankCustomer3)):
    for j in range(0, len(courier)):
        if i == 0:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[j] += 5
                break
        if i == 1:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[j] += 4
                break
        if i == 2:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[j] += 3
                break
        if i == 3:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[j] += 2
                break
        if i == 4:
            if rankCustomer3[i] == courier[j]:
                pointsCust3[j] += 1
                break

print(sentimentRank)

for i in range(0, len(sentimentRank)):
    for j in range(0, len(courier)):
        if i == 0:
            if sentimentRank[i] == courier[j]:
                pointsCust1[j] += 1
                pointsCust2[j] += 1
                pointsCust3[j] += 1
                break
        if i == 1:
            if sentimentRank[i] == courier[j]:
                pointsCust1[j] += 3.5
                pointsCust2[j] += 3.5
                pointsCust3[j] += 3.5
                break
        if i == 2:
            if sentimentRank[i] == courier[j]:
                pointsCust1[j] += 6
                pointsCust2[j] += 6
                pointsCust3[j] += 6
                break
        if i == 3:
            if sentimentRank[i] == courier[j]:
                pointsCust1[j] += 8.5
                pointsCust2[j] += 8.5
                pointsCust3[j] += 8.5
                break
        if i == 4:
            if sentimentRank[i] == courier[j]:
                pointsCust1[j] += 12
                pointsCust2[j] += 12
                pointsCust3[j] += 12
                break

print("Points for every courier for each customer before sorting: ")
print("Customer 1: ",pointsCust1)
print("Customer 2: ",pointsCust2)
print("Customer 3: ",pointsCust3)

dictFinalCust1 = {}
dictFinalCust2 = {}
dictFinalCust3 = {}

for i in range(len(courier)):
    dictFinalCust1[pointsCust1[i]] = courier[i]
    dictFinalCust2[pointsCust2[i]] = courier[i]
    dictFinalCust3[pointsCust3[i]] = courier[i]

print(dictFinalCust1)

quickSort(pointsCust1, 0, len(pointsCust1)-1)
quickSort(pointsCust2, 0, len(pointsCust2)-1)
quickSort(pointsCust3, 0, len(pointsCust3)-1)

print("")
print("Points for every courier for each customer after sorting: ")
print("Customer 1: ",pointsCust1)
print("Customer 2: ",pointsCust2)
print("Customer 3: ",pointsCust3)

print("")
print("Preferred Courier for Customer 1 based on rank: ")
rank = 1
for i in range(len(pointsCust1)-1, -1, -1):
    print(rank,"-",dictFinalCust1[pointsCust1[i]])
    rank+=1

print("")
print("Preferred Courier for Customer 2 based on rank: ")
rank = 1
for i in range(len(pointsCust2)-1, -1, -1):
    print(rank,"-",dictFinalCust2[pointsCust2[i]])
    rank+=1

print("")
print("Preferred Courier for Customer 3 based on rank: ")
rank = 1
for i in range(len(pointsCust3)-1, -1, -1):
    print(rank,"-",dictFinalCust3[pointsCust3[i]])
    rank+=1











