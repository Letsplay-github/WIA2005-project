import gmplot
import requests
import json
import pprint as pp

# Create the map plotter:
apikey = 'AIzaSyDftFL1A_AZexMNgnrR-pv_ho9Ho6kVgLM' 

latHub = [3.0319924887507144, 3.112924170027219, 3.265154613796736, 2.9441205329488325, 3.2127230893650065]
longHub = [101.37344116244806, 101.63982650389863, 101.68024844550233, 101.7901521759029, 101.57467295692778]

# Mark the hub locations
colour = ["red", "blue", "green", "brown", "yellow"]
gmap = gmplot.GoogleMapPlotter(latHub[0], longHub[0], 14, apikey=apikey)
for i in range(0, len(latHub)):
    gmap.marker(latHub[i], longHub[i], color=colour[i])

# Draw the map to an HTML file:
gmap.draw('map.html')

latOrigin = [3.3615395462207878, 3.049398375759954, 3.141855957281073]
longOrigin = [101.56318183511695, 101.58546611160301, 101.76158583424586]

latDestination = [3.1000170516638885, 3.227994355250716, 2.9188704151716256]
longDestination = [101.53071480907951, 101.42730357605375, 101.65251821655471]

distanceOriDes = []
url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="
url2 = "&destinations="
url3 = "&key="
comma = ","

# Q2 Find the distance between origin and destination
for i in range(0, len(latOrigin)):
    originLat = str(latOrigin[i])
    originLong = str(longOrigin[i])
    desLat = str(latDestination[i])
    desLong = str(longDestination[i])
    urlFull = url1 + originLat + comma + originLong + url2 + desLat + comma + desLong + url3 + apikey
    req = requests.get(urlFull).json()
    dis = req["rows"][0]["elements"][0]["distance"]["value"]
    distanceOriDes.append(dis)

print("The distance between customer from origin and destination:")
for i in range(0, len(distanceOriDes)):
    print("Customer",i+1,":", distanceOriDes[i])
print("")

# Find the distance origin - hub - destination for each customer
distanceCust1 = []
distanceCust2 = []
distanceCust3 = []
for i in range(0, len(latOrigin)):
    for j in range(0, len(latHub)):
        originLat = str(latOrigin[i])
        originLong = str(longOrigin[i])
        desLat = str(latHub[j])
        desLong = str(longHub[j])
        urlFull = url1 + originLat + comma + originLong + url2 + desLat + comma + desLong + url3 + apikey
        req1 = requests.get(urlFull).json()
        dis1 = req1["rows"][0]["elements"][0]["distance"]["value"]
        originLat = str(latHub[j])
        originLong = str(longHub[j])
        desLat = str(latDestination[i])
        desLong = str(longDestination[i])
        urlFull = url1 + originLat + comma + originLong + url2 + desLat + comma + desLong + url3 + apikey
        req2 = requests.get(urlFull).json()
        dis2 = req2["rows"][0]["elements"][0]["distance"]["value"]
        distance = dis1 + dis2
        if i == 0:
            distanceCust1.append(distance)
        if i == 1:
            distanceCust2.append(distance)
        if i == 2:
            distanceCust3.append(distance)

courier = ["City-Link Express", "Pos Laju", "GDEX", "J&T", "DHL"]
print(courier)

dictCust1 = {}
dictCust2 = {}
dictCust3 = {}

for i in range(0, len(courier)):
    dictCust1[distanceCust1[i]] = courier[i]
    dictCust2[distanceCust2[i]] = courier[i]
    dictCust3[distanceCust3[i]] = courier[i]

print("Customer 1:")
print(dictCust1)
print("")
print("Customer 2:")
print(dictCust2)
print("")
print("Customer 3:")
print(dictCust3)
print("")

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

quickSort(distanceCust1, 0, len(distanceCust1)-1)
quickSort(distanceCust2, 0, len(distanceCust2)-1)
quickSort(distanceCust3, 0, len(distanceCust3)-1)

print("The sorted distance for each courier for each customer")
print(distanceCust1)
print(distanceCust2)
print(distanceCust3)
print("")
rankCust1 = {}
rankCust2 = {}
rankCust3 = {}
for i in range(0, len(distanceCust1)):
    rankCust1[dictCust1[distanceCust1[i]]] = distanceCust1[i]
    rankCust2[dictCust2[distanceCust2[i]]] = distanceCust2[i]
    rankCust3[dictCust3[distanceCust3[i]]] = distanceCust3[i]

print("Customer 1 Possible Routes: ")
print(rankCust1)
print("")
print("Customer 2 Possible Routes: ")
print(rankCust2)
print("")
print("Customer 3 Possible Routes: ")
print(rankCust3)
print("")

print("Courier with the shortest distance(Customer 1):", dictCust1[distanceCust1[0]], "with",  distanceCust1[0])
print("Courier with the shortest distance(Customer 2):", dictCust2[distanceCust2[0]], "with",  distanceCust2[0])
print("Courier with the shortest distance(Customer 3):", dictCust3[distanceCust3[0]], "with",  distanceCust3[0])

index1 = courier.index(dictCust1[distanceCust1[0]])
index2 = courier.index(dictCust2[distanceCust2[0]])
index3 = courier.index(dictCust3[distanceCust3[0]])

gmapCust1 = gmplot.GoogleMapPlotter(latOrigin[0], longOrigin[0], 14, apikey=apikey)
for i in range(0, len(latHub)):
        gmapCust1.directions(
            (latOrigin[0],longOrigin[0]),
            (latDestination[0],longDestination[0]),
            waypoints = [(latOrigin[0],longOrigin[0]),(latHub[i],longHub[i]),(latDestination[0],longDestination[0])]
        )
        
        if i == index1:
            gmapCust1.marker(latHub[i],longHub[i], color="purple")
        
        else:
            gmapCust1.marker(latHub[i],longHub[i], color=colour[i])

gmapCust1.draw("Customer1.html")

gmapCust2 = gmplot.GoogleMapPlotter(latOrigin[1], longOrigin[1], 14, apikey=apikey)
for i in range(0, len(latHub)):
        gmapCust2.directions(
            (latOrigin[1],longOrigin[1]),
            (latDestination[1],longDestination[1]),
            waypoints = [(latOrigin[1],longOrigin[1]),(latHub[i],longHub[i]),(latDestination[1],longDestination[1])]
        )
        
        if i == index2:
            gmapCust2.marker(latHub[i],longHub[i], color="purple")
        
        else:
            gmapCust2.marker(latHub[i],longHub[i], color=colour[i])

gmapCust2.draw("Customer2.html")

gmapCust3 = gmplot.GoogleMapPlotter(latOrigin[2], longOrigin[2], 14, apikey=apikey)
for i in range(0, len(latHub)):
        gmapCust3.directions(
            (latOrigin[2],longOrigin[2]),
            (latDestination[2],longDestination[2]),
            waypoints = [(latOrigin[2],longOrigin[2]),(latHub[i],longHub[i]),(latDestination[2],longDestination[2])]
        )
        
        if i == index3:
            gmapCust3.marker(latHub[i],longHub[i], color="purple")
        
        else:
            gmapCust3.marker(latHub[i],longHub[i], color=colour[i])

gmapCust3.draw("Customer3.html")

# gmap1 = gmplot.GoogleMapPlotter(latOrigin[0], longOrigin[0], 14, apikey=apikey)
# colour = ["red", "blue", "green"]
# for i in range(0, len(latOrigin)):
#     gmap1.directions(
#         (latOrigin[i],longOrigin[i]),
#         (latDestination[i],longDestination[i]),
#         waypoints = [(latOrigin[i],longOrigin[i]),(latHub[indexHub[i]],longHub[indexHub[i]]),(latDestination[i],longDestination[i])]
#     )

#     gmap1.marker(latHub[indexHub[i]],longHub[indexHub[i]], color=colour[i])

# gmap1.draw('plotline.html')

# gmap1.directions