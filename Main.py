import folium
from folium.map import Marker
import openrouteservice as ors

client = ors.Client(key="5b3ce3597851110001cf6248fa79019d400d45668f1d7c8ae9cfde10")
# m is the map
m = folium.Map(location=[3.128753803910095, 101.59555418169249],zoom_start=11.2)

class deliveryhub:
    def __init__(self, name, latitude, longitude, imgname):
        self.name      = name
        self.latitude  = latitude
        self.longitude = longitude
        popup     = '<img src="./Icon Images/' + imgname + '" alt="">'
        self.marker    = folium.Marker(location=(latitude,longitude),popup=popup,tooltip="click for more information")

# all deliveryhub in one tuple
deliveryhublist=[deliveryhub("City-link Express",
                            3.0319924887507144, 101.37344116244806,"Citylink icon.png"  ),
                deliveryhub("Pos Laju",
                            3.112924170027219 , 101.63982650389863,"Poslaju icon.png"),
                deliveryhub("GDEX",
                            3.265154613796736 , 101.68024844550233,"Gdex icon.png"),
                deliveryhub("J&T",
                            2.9441205329488325, 101.7901521759029,"J&T icon.png"),
                deliveryhub("DHL",
                            3.2127230893650065, 101.57467295692778,"DHL icon.png")]


class customer:
    def __init__(self,num,customercolor,originname, originlat, originlon, destinationname,destinationlat,destinationlon):
        self.num              = num
        self.originname       = originname
        self.originlat        = originlat
        self.originlon        = originlon
        self.destinationname  = destinationname
        self.destinationlat   = destinationlat
        self.destinationlon   = destinationlon
        self.popuporigin      = originname + "(Customer " + num + "'s origin)"
        self.popupdestination = destinationname + "(Customer " + num + "'s destination"
        self.direction        = client.directions(coordinates = [(originlon,originlat),(destinationlon,destinationlat)], profile = 'driving-car', format = 'geojson')
        #distance in between is in kilometers
        self.distanceinbetween= self.direction['features'][0]['properties']['summary']['distance']/1000
        self.routelist        =[]
        # originmarker
        self.originmarker    = folium.Marker(location=(originlat,originlon),popup=self.popuporigin,tooltip="click for more information",icon=folium.Icon(icon="envelope",color=customercolor))
        # destinationmarker
        self.destinationmarker    = folium.Marker(location=(destinationlat,destinationlon),popup=self.popupdestination,tooltip="click for more information",icon=folium.Icon(icon="home",color=customercolor))

    def stopby(self,deliveryhub):

        temp = route((self.originlon,self.originlat),deliveryhub,(self.destinationlon,self.destinationlat))
        routelistlen = len(self.routelist)
        if(routelistlen==0):
            self.routelist.append(temp)
        else:
            for j in range(0,routelistlen):
                if temp.distance < self.routelist[j].distance:
                    self.routelist.insert(j,temp)
                    break
                elif j == routelistlen-1:
                    self.routelist.append(temp)
                    break

    def getshortestroad(self):
        return self.routelist[0].theroute

    def getshortestroaddistance(self):
        return self.routelist[0].distance
        
    
        

customerlist = [customer('1','lightred',"Rawang",3.3615395462207878,101.56318183511695,
                "Bukit Jeluton",3.1000170516638885,101.53071480907951),
                customer('2','purple',"Subang Jaya",3.049398375759954, 101.58546611160301,
                "Puncak Alam",3.227994355250716, 101.42730357605375),
                customer('3','green',"Ampang",3.141855957281073, 101.76158583424586,
                "Cyberjaya",2.9188704151716256,101.65251821655471)]

class route:
    def __init__(self,originlonlat,deliveryhub,destinationlonlat):
        self.deliveryhub    = deliveryhub
        self.coordinates    = [originlonlat,[deliveryhub.longitude,deliveryhub.latitude],destinationlonlat]
        self.theroute       = client.directions(coordinates = self.coordinates, profile = 'driving-car', format = 'geojson')
        self.distance       = self.theroute['features'][0]['properties']['summary']['distance']/1000
        

# distance of origin to destination
for k in customerlist:
    print("Distance between origin(" + k.originname + ") and destination(" + k.destinationname + ") of customer " + k.num + ": " + str(k.distanceinbetween) + "  kilometers")
print()
# create route for the customers

#add all delivery to customer class(customer class will arranged which one is the shortest)
for c in customerlist:
    for d in deliveryhublist:
        c.stopby(d)

#layer group(for each customer)
grp  = [
        folium.FeatureGroup(name='C1 shortest route',control=True),
        folium.FeatureGroup(name='C2 shortest route',control=True),
        folium.FeatureGroup(name='C3 shortest route',control=True),
        ]


for j in range(0,len(customerlist)):
    customerlist[j].originmarker.add_to(grp[j])
    customerlist[j].destinationmarker.add_to(grp[j])
    folium.GeoJson(customerlist[j].getshortestroad(),name='route',tooltip=str(customerlist[j].getshortestroaddistance()) + "kilometers").add_to(grp[j])
    m.add_children(grp[j])


# add marker to map
for i in deliveryhublist:
    i.marker.add_to(m)

# add route to map
for c in customerlist:
    for i in range(0,len(c.routelist),1):
        print("customer " + c.num + " using " + c.routelist[i].deliveryhub.name + "with distance of " + str(c.routelist[i].distance))
    print()

folium.LayerControl().add_to(m)

# testcoordinate = [[customerlist[0].originlon,customerlist[0].originlat],[ 101.68024844550233,3.265154613796736]]
# testdistance = client.directions(coordinates = testcoordinate, profile = 'driving-car', format = 'geojson')
# print(format(testdistance['features'][0]['properties']['segments'][0]['distance']/1000,".3f"))
# folium.GeoJson(route,name='route').add_to(m)


# add map routing.html
m.save('OurMap.html')