import geopy
import gmplot
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# location of each Hub

class location:
    def __init__(self, latitude, longitude, color):
        self.latitude  = latitude
        self.longitude = longitude
        self.color     = color

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

#deliveryhub
citylink = location(3.0319924887507144, 101.37344116244806,  "green")
poslaju  = location(3.112924170027219 , 101.63982650389863, "orange")
gdex     = location(3.265154613796736 , 101.68024844550233,   "blue")
JT       = location(2.9441205329488325, 101.7901521759029 ,    "red")
dhl      = location(3.2127230893650065, 101.57467295692778, "yellow")

#customer
c1 = customer("Rawang",     3.3615395462207878,101.56318183511695,"Bukit Jeluton",3.1000170516638885,101.53071480907951)
c2 = customer("Subang Jaya",3.049398375759954, 101.58546611160301,"Puncak Alam",  3.227994355250716, 101.42730357605375)
c3 = customer("Ampang",     3.141855957281073, 101.76158583424586,"Cyberjaya",    2.9188704151716256,101.65251821655471)

#deliverhub location(use for gmplot scatter)
deliveryhub = zip(*[
    (citylink.latitude,citylink.longitude),
    (poslaju.latitude,poslaju.longitude),
    (gdex.latitude,gdex.longitude),
    (JT.latitude,JT.longitude),
    (dhl.latitude,dhl.longitude)
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

apikey = ''
gmap = gmplot.GoogleMapPlotter(3.128753803910095, 101.59555418169249,11,apikey)


#Q1 1)
gmap.scatter(*deliveryhub, color=[citylink.color, poslaju.color, gdex.color, JT.color, dhl.color],marker=True)
gmap.draw('map.html')

#Q1 2)

print(c1.distance)
print(c2.distance)
print(c3.distance)

# from geopy.distance import geodesic
# newport_ri = (41.49008, -71.312796)
# cleveland_oh = (41.499498, -81.695391)
# print(geodesic(newport_ri, cleveland_oh).miles)

