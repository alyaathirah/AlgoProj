#Question1.1
#Plot hub
import gmplot
#hub
lat=[3.0319924887507144,3.112924170027219,3.265154613796736,2.9441205329488325,3.2127230893650065]
lang=[101.37344116244806,101.63982650389863,101.68024844550233,101.7901521759029,101.57467295692778]
#returns map object
Hub = gmplot.GoogleMapPlotter(3.0319924887507144,101.37344116244806,15)
#plots the points on the map
Hub.scatter(lat,lang,'red',size=50,marker=True)
Hub.marker(3.2127230893650065, 101.57467295692778, title="Delivery Hub DHL")
Hub.marker(3.112924170027219, 101.63982650389863, title="Delivery Hub Pos Laju")
Hub.marker(3.0319924887507144, 101.37344116244806, title="Delivery Hub City-link Express")
Hub.marker(3.265154613796736, 101.68024844550233, title="Delivery Hub GDEX")
Hub.marker(2.9441205329488325,101.7901521759029 , title="Delivery Hub J&T")
Hub.apikey = "***"
Hub.draw('map.html')

#Question1.2
#Distance
# Importing the geodesic module from the library
from geopy.distance import geodesic

# Loading the lat-long data for customer origin n destination
Rawang = (3.3615395462207878, 101.56318183511695)
BukitJelutong = (3.1000170516638885, 101.53071480907951)
SubangJaya = (3.049398375759954, 101.58546611160301)
PuncakAlam = (3.227994355250716, 101.42730357605375)
Ampang = (3.141855957281073, 101.76158583424586)
Cyberjaya = (2.9188704151716256, 101.65251821655471)
Cyberjaya1 = (lat[0],lang[0])
Company = ["City-link Express", "Pos Laju\t", "GDEX\t\t","J&T\t\t","DHL\t\t"]
Cust1 = [] 
Cust2 = [] 
Cust3 = [] 

#Print the distance in origin-destination
print("Customer 1\nOrigin: Rawang \nDestination: Bukit Jelutong \nDistance:",round(geodesic(Rawang,BukitJelutong).km,2),"km")
print("\nCustomer 2\nOrigin: Subang Jaya \nDestination: Puncak Alam \nDistance:",round(geodesic(SubangJaya, PuncakAlam).km,2),"km")
print("\nCustomer 3\nOrigin: Ampang \nDestination: Cyberjaya \nDistance:",round(geodesic(Ampang, Cyberjaya).km,2),"km\n")


# Print the distance calculated in km
distance=0
Courier=0
for j in range(3):
    print("Customer ",j+1)
    print("Courier Company\t\tDistance(km)")
    for i in range(5):
        Courier = (lat[i],lang[i])
        if j==0:
            distance=geodesic(Rawang,Courier,BukitJelutong).km
            Cust1.append(round(distance,2))
        elif j==1:
            distance=geodesic(SubangJaya,Courier, PuncakAlam).km
            Cust2.append(round(distance,2))
        else:
            distance=geodesic(Ampang,Courier, Cyberjaya).km
            Cust3.append(round(distance,2))
        print(Company[i],"\t",round(distance,2))
    print("\n")

#Question1.3
#Shortestpath
def shellSort(array, n,arr):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            temp1 = arr[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                arr[j] = arr[j - interval]
                j -= interval

            array[j] = temp
            arr[j] = temp1
        interval //= 2

CourierCompany = ["City-link Express", "Pos Laju", "GDEX","J&T","DHL"]
CourierCompany1 = ["City-link Express", "Pos Laju", "GDEX","J&T","DHL"]
CourierCompany2 = ["City-link Express", "Pos Laju", "GDEX","J&T","DHL"]

size = len(CourierCompany)
shortest=0
comp=''

for j in range(3):
    print("Customer ",j+1,"\n")
    print("Sorted Path in Ascending Order (km):")
    if j==0:
            shellSort(Cust1, size, CourierCompany)
            print(*CourierCompany, sep=' , ')
            print(*Cust1, sep=' , ')
            comp=CourierCompany[0]
            shortest=Cust1[0]
    elif j==1:
            shellSort(Cust2, size, CourierCompany1)
            print(*CourierCompany1, sep=' , ')
            print(*Cust2, sep=' , ')
            comp=CourierCompany1[0]
            shortest=Cust2[0]
    else:
            shellSort(Cust3, size, CourierCompany2)
            print(*CourierCompany2, sep=' , ')
            print(*Cust3, sep=' , ')
            comp=CourierCompany2[0]
            shortest=Cust3[0]
    print("\nShortest Courier Company: ",comp,"(",shortest," km)\n")

#Question1.4
#plotCustomer

Hub1 = gmplot.GoogleMapPlotter(3.0319924887507144,101.37344116244806,15)
lat=[3.0319924887507144,3.112924170027219,3.265154613796736,2.9441205329488325,3.2127230893650065]
lang=[101.37344116244806,101.63982650389863,101.68024844550233,101.7901521759029,101.57467295692778]
Hub1.scatter(lat,lang,'red',size=50,marker=True)
lat1=[3.3615395462207878,3.2127230893650065,3.1000170516638885]
lang1=[101.56318183511695,101.57467295692778,101.53071480907951]
Hub1.scatter(lat1,lang1,size=50,marker=True)
lat2=[3.049398375759954,3.2127230893650065,3.227994355250716]
lang2=[101.58546611160301,101.57467295692778,101.42730357605375]
Hub1.scatter(lat2,lang2,size=50,marker=True)
lat3=[3.141855957281073,3.112924170027219,2.9188704151716256]
lang3=[101.76158583424586,101.63982650389863 ,101.65251821655471]
Hub1.scatter(lat3,lang3,size=50,marker=True)
Hub1.marker(3.3615395462207878, 101.56318183511695, title="Origin Rawang",color='cornflowerblue')
Hub1.marker(3.2127230893650065, 101.57467295692778, title="Delivery Hub DHL",color='purple')
Hub1.marker(3.227994355250716, 101.42730357605375, title="Destination Puncak Alam",color='pink')
Hub1.marker(3.049398375759954, 101.58546611160301, title="Origin Subang Jaya",color='cornflowerblue')
Hub1.marker(3.1000170516638885, 101.53071480907951, title="Destination Bukit Jelutong",color='pink')
Hub1.marker(3.141855957281073, 101.76158583424586, title="Origin Ampang",color='cornflowerblue')
Hub1.marker(3.112924170027219, 101.63982650389863, title="Delivery Hub Pos Laju",color='purple')
Hub1.marker(2.9188704151716256, 101.65251821655471, title="Destination Cyberjaya",color='pink')
Hub1.marker(3.0319924887507144, 101.37344116244806, title="Delivery Hub City-link Express")
Hub1.marker(3.265154613796736, 101.68024844550233, title="Delivery Hub GDEX")
Hub1.marker(2.9441205329488325,101.7901521759029 , title="Delivery Hub J&T")

Hub1.plot(lat1,lang1,'blue',edge_widht=2.5)
Hub1.plot(lat2,lang2,'green',edge_widht=2.5)
Hub1.plot(lat3,lang3,'black',edge_widht=2.5)
Hub1.apikey = "***"
Hub1.draw('map1.html')



