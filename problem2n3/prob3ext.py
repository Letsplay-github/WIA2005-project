


#distance from problem 1
distanceCust1 = [92.53710000000001, 62.9605, 61.164, 122.1507, 45.9347]
distanceCust2 = [62.170300000000005, 55.4486,  76.8486, 105.7941, 47.236]
distanceCust3 = [103.2835, 50.559400000000004, 76.01310000000001, 56.7797, 74.71839999999999]

courier = ["City-Link Express", "Pos Laju", "GDEX", "J&T", "DHL"]
print("")

#dictionary containing courier name and distance
dictCustomer1 = {}
dictCustomer2 = {}
dictCustomer3 = {}

for i in range(0, len(courier)):
    dictCustomer1[distanceCust1[i]] = courier[i]
    dictCustomer2[distanceCust2[i]] = courier[i]
    dictCustomer3[distanceCust3[i]] = courier[i]

#Sort using quick sort
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


quickSort(distanceCust1, 0, len(distanceCust1)-1)
quickSort(distanceCust2, 0, len(distanceCust2)-1)
quickSort(distanceCust3, 0, len(distanceCust3)-1)


#dictionary containing courier name and distance after sorted
rankCust1 = {}
rankCust2 = {}
rankCust3 = {}
for i in range(0, len(distanceCust1)):
    rankCust1[dictCustomer1[distanceCust1[i]]] = distanceCust1[i]
    rankCust2[dictCustomer2[distanceCust2[i]]] = distanceCust2[i]
    rankCust3[dictCustomer3[distanceCust3[i]]] = distanceCust3[i]

print("Possible Routes for customer 1: ")
print(rankCust1)
print("")
print("Possible Routes for customer 2: ")
print(rankCust2)
print("")
print("Possible Routes for customer 3: ")
print(rankCust3)
print("")


