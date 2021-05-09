import geopy
import gmplot
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# location of each Hub

class deliveryhub:
    def __init__(self, name, latitude, longitude, color):
        self.name      = name
        self.latitude  = latitude
        self.longitude = longitude
        self.color     = color
        self.latlon    = (self.latitude,self.longitude)

class customer:
    def __init__(self,originname, originlat, originlon,destinationname, destinationlat, destinationlon):
        self.origin          = (originlat,originlon)
        self.originname      = originname
        self.originlat       = originlat
        self.originlon       = originlon
        self.destination     = (destinationlat,destinationlon)
        self.destinationname = destinationname
        self.destinationlat  = destinationlat
        self.destinationlon  = destinationlon
        self.distance        = geodesic(self.origin,self.destination)
    
    def stopby(self,latitude,longitude):
        stopbylocation = (latitude,longitude)
        stopbydistance = geodesic(self.origin,stopbylocation) + geodesic(stopbylocation,self.destination)
        return stopbydistance

#deliveryhub
deliveryhublist = [deliveryhub("City-link Express", 3.0319924887507144, 101.37344116244806, "green" ),
                    deliveryhub("Pos Laju",          3.112924170027219 , 101.63982650389863, "orange"),
                    deliveryhub("GDEX",              3.265154613796736 , 101.68024844550233, "blue"  ),
                    deliveryhub("J&T",               2.9441205329488325, 101.7901521759029 , "red"   ),
                    deliveryhub("DHL",               3.2127230893650065, 101.57467295692778, "yellow")]

#customer
c1 = customer("Rawang",     3.3615395462207878,101.56318183511695,"Bukit Jeluton",3.1000170516638885,101.53071480907951)
c2 = customer("Subang Jaya",3.049398375759954, 101.58546611160301,"Puncak Alam",  3.227994355250716, 101.42730357605375)
c3 = customer("Ampang",     3.141855957281073, 101.76158583424586,"Cyberjaya",    2.9188704151716256,101.65251821655471)

#deliverhub location(use for gmplot scatter)
deliveryhub = zip(*[
    deliveryhublist[0].latlon,
    deliveryhublist[1].latlon,
    deliveryhublist[2].latlon,
    deliveryhublist[3].latlon,
    deliveryhublist[4].latlon
])

geolocator = Nominatim(user_agent="Question1")
# Addresses of delivery hub
# CitylinkExpress = geolocator.reverse("3.0319924887507144, 101.37344116244806")
# PosLaju = geolocator.reverse("3.112924170027219, 101.63982650389863")
# GDEX = geolocator.reverse("3.265154613796736, 101.68024844550233")
# JandT = geolocator.reverse("2.9441205329488325, 101.7901521759029")
# DHL = geolocator.reverse("3.2127230893650065, 101.57467295692778")
# print(CitylinkExpress.address)
# print(PosLaju.address)
# print(GDEX.address)
# print(JandT.address)
# print(DHL.address)

apikey = 'AIzaSyBjsKRkTNzMm-elG3Fu9UywPCt1yS03q0Y'
gmap = gmplot.GoogleMapPlotter(3.128753803910095, 101.59555418169249,11,apikey=apikey)


#Q1 1)

for i in range(len(deliveryhublist)):
    gmap.marker(deliveryhublist[i].latitude,deliveryhublist[i].longitude,color = deliveryhublist[i].color, label = deliveryhublist[i].name)
# gmap.scatter(*deliveryhub, color=[citylink.color, poslaju.color, gdex.color, JT.color, dhl.color],marker=True)
gmap.draw('map.html')

#Q1 2)

print(c1.distance)
print(c2.distance)
print(c3.distance)
print()

#Q1 3)

c1leastdistance = 0
c2leastdistance = 0
c3leastdistance = 0
j = 0

for i in range(len(deliveryhublist)):

    if i == 0:
        c1leastdistance = c1.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
    elif c1leastdistance > c1.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude):
        c1leastdistance = c1.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
        j = i

print("Stop by at is quicker "+ deliveryhublist[j].name + ": "+ str(c1.stopby(deliveryhublist[j].latitude,deliveryhublist[j].longitude)))
j = 0
for i in range(len(deliveryhublist)):

    if i == 0:
        c2leastdistance = c2.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
    elif c2leastdistance > c2.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude):
        c2leastdistance = c2.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
        j = i


print("Stop by at is quicker "+ deliveryhublist[j].name + ": "+ str(c2.stopby(deliveryhublist[j].latitude,deliveryhublist[j].longitude)))

j=0
for i in range(len(deliveryhublist)):

    if i == 0:
        c3leastdistance = c3.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
    elif c3leastdistance > c3.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude):
        c3leastdistance = c3.stopby(deliveryhublist[i].latitude,deliveryhublist[i].longitude)
        j = i

print("Stop by at is quicker "+ deliveryhublist[j].name + ": "+ str(c3.stopby(deliveryhublist[j].latitude,deliveryhublist[j].longitude)))

# Q1 4)

gmap.directions((c1.originlat,c1.originlon),(c1.destinationlat,c1.destinationlon),waypoints=[(c1.originlat,c1.originlon),(deliveryhublist[0].latitude,deliveryhublist[0].longitude),(c1.destinationlat,c1.destinationlon)])
gmap.draw('route.html')