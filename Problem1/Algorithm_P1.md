# Problem 1

Customer who needs to make a delivery needs to know which courier company can does it 
fast (assuming that the shorter the distance, the quicker is the delivery). The application will analyse five 
(5) local courier companies which have their delivery hubs located in various locations in West Malaysia. 
The details of the courier companies and their delivery hubs are given

### 1. Get and mark locations of all hub locations given 


```python
import pandas as pd
import gmplot
from IPython.display import IFrame
API_key = '****'

deliveryHub = pd.read_csv('AlgorithmDataCourier.csv')
deliveryHub['Latitude'][0]
#print(deliveryHub)
DHlat = deliveryHub['Latitude']
DHlong = deliveryHub['Longitude']

hubPoint =  gmplot.GoogleMapPlotter(DHlat[1],DHlong[1],10)
hubPoint.scatter(DHlat,DHlong,'red',size=50,marker=True)
hubPoint.marker(DHlat[0], DHlong[0], title="City-link Express, Port Klang")
hubPoint.marker(DHlat[1], DHlong[1], title="Pos Laju, Petaling Jaya")
hubPoint.marker(DHlat[2], DHlong[2], title="GDEX, Batu Caves")
hubPoint.marker(DHlat[3], DHlong[3], title="J&T, Kajang")
hubPoint.marker(DHlat[4], DHlong[4], title="DHL, Sungai Buloh")

hubPoint.apikey = API_key
hubPoint.draw('map.html')
IFrame(src='map.html', width=800, height=600)
```





<iframe
    width="800"
    height="600"
    src="map.html"
    frameborder="0"
    allowfullscreen
></iframe>




### 2. Get the distances between origin and destination of the customers parcel details.


```python
import googlemaps
gmaps = googlemaps.Client(key=API_key)

custDelivery_Data = pd.read_csv('AlgorithmDataCustomer.csv')

distanceOriDes = []
origin_Lat = custDelivery_Data['Latitude-Origin']
origin_Long = custDelivery_Data['Longitude-Origin']
dest_Lat = custDelivery_Data['Latitude-Destination']
dest_Long = custDelivery_Data['Longitude-Destination']

origin = (origin_Lat, origin_Long)
destination = (dest_Lat, dest_Long)

for i in range(len(custDelivery_Data['Latitude-Origin'])):
    origin = (origin_Lat[i], origin_Long[i])
    destination = (dest_Lat[i], dest_Long[i])
    distance = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
    distanceOriDes.append(distance/1000)
    
custDelivery_Data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Customer</th>
      <th>Origin</th>
      <th>Latitude-Origin</th>
      <th>Longitude-Origin</th>
      <th>Destination</th>
      <th>Latitude-Destination</th>
      <th>Longitude-Destination</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Customer 1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Customer 2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Customer 3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
    </tr>
  </tbody>
</table>
</div>




```python
custDelivery_Data["Distance"] = distanceOriDes
custDelivery_Data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Customer</th>
      <th>Origin</th>
      <th>Latitude-Origin</th>
      <th>Longitude-Origin</th>
      <th>Destination</th>
      <th>Latitude-Destination</th>
      <th>Longitude-Destination</th>
      <th>Distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Customer 1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>41.591</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Customer 2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>38.456</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Customer 3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>35.958</td>
    </tr>
  </tbody>
</table>
</div>



### 3. Assuming that all deliveries must go through their delivery hub. For example, a delivery from Kuala Lumpur (origin) will go through Pos Laju Hub in Petaling Jaya to Putrajaya (destination). Suggest the least distance that the parcel has to travel for each customer using every courier company. 

#### a. Calculating total distance between Origin - Delivery Hub - Destination


```python
fullData = pd.read_csv('AlgorithmDataFull.csv')

totalDistanceList = []
distance1List = []
distance2List = []

origin_Lat = fullData['Latitude-Origin']
origin_Long = fullData['Longitude-Origin']
dh_Lat = fullData['Latitude-DH']
dh_Long = fullData['Longitude-DH']
dest_Lat = fullData['Latitude-Destination']
dest_Long = fullData['Longitude-Destination']

origin = (origin_Lat, origin_Long)
del_hub = (dh_Lat, dh_Long)
destination = (dest_Lat, dest_Long)

for i in range(len(fullData['Latitude-Origin'])):
    origin = (origin_Lat[i], origin_Long[i])
    del_hub = (dh_Lat[i], dh_Long[i])
    destination = (dest_Lat[i], dest_Long[i])
    
    #calculate distance
    distance1 = gmaps.distance_matrix(origin, del_hub, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
    distance2 = gmaps.distance_matrix(del_hub, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
    total_distance = distance1 + distance2
    
    distance1List.append(distance1/1000)
    distance2List.append(distance2/1000)
    totalDistanceList.append(total_distance/1000)
    
fullData["Distance1 (Km)"] = distance1List
fullData["Distance2 (Km)"] = distance2List
fullData["Total Distance (Km)"] = totalDistanceList
fullData.to_csv('AlgoCalculated_Distances.csv', sep=',', index=None, header= ['Cust','Origin','Latitude-Origin','Longitude-Origin','Delivery Hub','Latitude-DH','Longitude-DH','Destination','Latitude-Destination','Longitude-Destination','Distance1 (Km)','Distance2 (Km)','Total Distance (Km)'])
calc_distance = pd.read_csv('AlgoCalculated_Distances.csv')
calc_distance
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cust</th>
      <th>Origin</th>
      <th>Latitude-Origin</th>
      <th>Longitude-Origin</th>
      <th>Delivery Hub</th>
      <th>Latitude-DH</th>
      <th>Longitude-DH</th>
      <th>Destination</th>
      <th>Latitude-Destination</th>
      <th>Longitude-Destination</th>
      <th>Distance1 (Km)</th>
      <th>Distance2 (Km)</th>
      <th>Total Distance (Km)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Port Klang</td>
      <td>3.031992</td>
      <td>101.373441</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>70.218</td>
      <td>28.814</td>
      <td>99.032</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Petaling Jaya</td>
      <td>3.112924</td>
      <td>101.639826</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>42.783</td>
      <td>20.457</td>
      <td>63.240</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Batu Caves</td>
      <td>3.265155</td>
      <td>101.680248</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>24.754</td>
      <td>36.345</td>
      <td>61.099</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Kajang</td>
      <td>2.944121</td>
      <td>101.790152</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>75.744</td>
      <td>49.207</td>
      <td>124.951</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Rawang</td>
      <td>3.361540</td>
      <td>101.563182</td>
      <td>Sungai Buloh</td>
      <td>3.212723</td>
      <td>101.574673</td>
      <td>Bukit Jelutong</td>
      <td>3.100017</td>
      <td>101.530715</td>
      <td>26.780</td>
      <td>27.174</td>
      <td>53.954</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Port Klang</td>
      <td>3.031992</td>
      <td>101.373441</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>39.679</td>
      <td>30.570</td>
      <td>70.249</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Petaling Jaya</td>
      <td>3.112924</td>
      <td>101.639826</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>14.021</td>
      <td>41.995</td>
      <td>56.016</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Batu Caves</td>
      <td>3.265155</td>
      <td>101.680248</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>35.918</td>
      <td>41.104</td>
      <td>77.022</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Kajang</td>
      <td>2.944121</td>
      <td>101.790152</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>35.215</td>
      <td>70.745</td>
      <td>105.960</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>Subang Jaya</td>
      <td>3.049398</td>
      <td>101.585466</td>
      <td>Sungai Buloh</td>
      <td>3.212723</td>
      <td>101.574673</td>
      <td>Puncak Alam</td>
      <td>3.227994</td>
      <td>101.427304</td>
      <td>24.145</td>
      <td>23.378</td>
      <td>47.523</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Port Klang</td>
      <td>3.031992</td>
      <td>101.373441</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>55.724</td>
      <td>56.052</td>
      <td>111.776</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Petaling Jaya</td>
      <td>3.112924</td>
      <td>101.639826</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>19.224</td>
      <td>34.331</td>
      <td>53.555</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Batu Caves</td>
      <td>3.265155</td>
      <td>101.680248</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>23.705</td>
      <td>48.727</td>
      <td>72.432</td>
    </tr>
    <tr>
      <th>13</th>
      <td>3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Kajang</td>
      <td>2.944121</td>
      <td>101.790152</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>27.763</td>
      <td>24.629</td>
      <td>52.392</td>
    </tr>
    <tr>
      <th>14</th>
      <td>3</td>
      <td>Ampang</td>
      <td>3.141856</td>
      <td>101.761586</td>
      <td>Sungai Buloh</td>
      <td>3.212723</td>
      <td>101.574673</td>
      <td>Cyberjaya</td>
      <td>2.918870</td>
      <td>101.652518</td>
      <td>30.961</td>
      <td>52.556</td>
      <td>83.517</td>
    </tr>
  </tbody>
</table>
</div>



#### b. Sort the distance to find the shortest path


```python
# shell sort

def shellSort(array, n, arr):

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
        
#initialize
customers = calc_distance['Cust']   
total_distances = calc_distance['Total Distance (Km)']
del_hub = calc_distance['Delivery Hub']
size = len(total_distances)

#initialize sorted hub
customer1 = []
hub1 = []
customer2 = []
hub2 = []
customer3 = []
hub3 = []

for i in range(size):
    if customers[i] == 1:
        customer1.append(total_distances[i])
        hub1.append(del_hub[i])
    elif customers[i] == 2:
        customer2.append(total_distances[i])
        hub2.append(del_hub[i])
    elif customers[i] == 3:
        customer3.append(total_distances[i])
        hub3.append(del_hub[i])

#sort
shellSort(customer1, len(customer1), hub1)
shellSort(customer2, len(customer2), hub2)
shellSort(customer3, len(customer3), hub3)

#display
couriers1 = []
couriers2 = []
couriers3 = []

def deliveryHub(hub, couriers):
    for delivery_hub in hub:
        if delivery_hub == 'Port Klang':
            couriers.append('City-link Express')
        elif delivery_hub == 'Petaling Jaya ':
            couriers.append('Pos Laju')
        elif delivery_hub == 'Batu Caves':
            couriers.append('GDEX')
        elif delivery_hub == 'Kajang':
            couriers.append('J&T')
        elif delivery_hub == 'Sungai Buloh':
            couriers.append('DHL')

deliveryHub(hub1, couriers1)
deliveryHub(hub2, couriers2)
deliveryHub(hub3, couriers3)

print('Customer 1: Distance and Delivery Hub')
print(customer1)
print(hub1)
print(couriers1)
print("The Courier Company with the shortest distance is", couriers1[0], "(", customer1[0], "km )")

print('\nCustomer 2: Distance and Delivery Hub')
print(customer2)
print(hub2)
print(couriers2)
print("The Courier Company with the shortest distance is", couriers2[0], "(", customer2[0], "km )")

print('\nCustomer 3: Distance and Delivery Hub')
print(customer3)
print(hub3)
print(couriers3)
print("The Courier Company with the shortest distance is", couriers3[0], "(", customer3[0], "km )")
```

    Customer 1: Distance and Delivery Hub
    [53.954, 61.099, 63.24, 99.032, 124.951]
    ['Sungai Buloh', 'Batu Caves', 'Petaling Jaya ', 'Port Klang', 'Kajang']
    ['DHL', 'GDEX', 'Pos Laju', 'City-link Express', 'J&T']
    The Courier Company with the shortest distance is DHL ( 53.954 km )
    
    Customer 2: Distance and Delivery Hub
    [47.523, 56.016, 70.249, 77.022, 105.96]
    ['Sungai Buloh', 'Petaling Jaya ', 'Port Klang', 'Batu Caves', 'Kajang']
    ['DHL', 'Pos Laju', 'City-link Express', 'GDEX', 'J&T']
    The Courier Company with the shortest distance is DHL ( 47.523 km )
    
    Customer 3: Distance and Delivery Hub
    [52.392, 53.555, 72.432, 83.517, 111.776]
    ['Kajang', 'Petaling Jaya ', 'Batu Caves', 'Sungai Buloh', 'Port Klang']
    ['J&T', 'Pos Laju', 'GDEX', 'DHL', 'City-link Express']
    The Courier Company with the shortest distance is J&T ( 52.392 km )
    

#### Store shortest path


```python
pathLat1 = []
pathLong1 = []
pathLat2 = []
pathLong2 = []
pathLat3 = []
pathLong3 = []
delHub = fullData['Delivery Hub']


def findCoordinate(courier, pathLat, pathLong):
    for i in range(len(courier)):
        if courier[0] == 'DHL':
            for j in range(len(delHub)):
                if delHub[j] == 'Sungai Buloh':
                    pathLat.append(dh_Lat[j])
                    pathLong.append(dh_Long[j])
                    break
            break
        elif courier[0] == 'J&T':
            for j in range(len(delHub)):
                if delHub[j] == 'Kajang':
                    pathLat.append(dh_Lat[j])
                    pathLong.append(dh_Long[j])
                    break
            break
        elif courier[0] == 'Pos Laju':
            for j in range(len(delHub)):
                if delHub[j] == 'Petaling Jaya ':
                    pathLat.append(dh_Lat[j])
                    pathLong.append(dh_Long[j])
                    break
            break
        elif courier[0] == 'GDEX':
            for j in range(len(delHub)):
                if delHub[j] == 'Batu Caves':
                    pathLat.append(dh_Lat[j])
                    pathLong.append(dh_Long[j])
                    break
            break
        elif courier[0] == 'City-link Express':
            for j in range(len(delHub)):
                if delHub[j] == 'Port Klang':
                    pathLat.append(dh_Lat[j])
                    pathLong.append(dh_Long[j])
                    break
            break
    
    

pathLat1.append(origin_Lat[0])
pathLong1.append(origin_Long[0])
pathLat2.append(origin_Lat[5])
pathLong2.append(origin_Long[5])
pathLat3.append(origin_Lat[10])
pathLong3.append(origin_Long[10])    

findCoordinate(couriers1, pathLat1, pathLong1)
findCoordinate(couriers2, pathLat2, pathLong2)
findCoordinate(couriers3, pathLat3, pathLong3)

pathLat1.append(dest_Lat[0])
pathLong1.append(dest_Long[0])
pathLat2.append(dest_Lat[5])
pathLong2.append(dest_Long[5])
pathLat3.append(dest_Lat[10])
pathLong3.append(dest_Long[10])

```

### 4. Plot line between the shortest destinations before and after 


```python
location = gmplot.GoogleMapPlotter(DHlat[1],DHlong[1],10)
location.scatter(DHlat, DHlong, 'red', size=50, marker=True)
location.scatter(origin_Lat, origin_Long, 'blue', size=50, marker=True)
location.scatter(dest_Lat, dest_Long, 'black', size=50, marker=True)

location.plot(pathLat1,pathLong1,'blue',edge_widht=3.5)
location.plot(pathLat2,pathLong2,'green',edge_widht=3.5)
location.plot(pathLat3,pathLong3,'black',edge_widht=3.5)

#marker for customer origin
location.marker(pathLat1[0], pathLong1[0], title="Customer 1 Origin")
location.marker(pathLat2[0], pathLong2[0], title="Customer 2 Origin")
location.marker(pathLat3[0], pathLong3[0], title="Customer 3 Origin")

#marker for ustomer destination
location.marker(pathLat1[2], pathLong1[2], title="Customer 1 Destination")
location.marker(pathLat1[2], pathLong1[2], title="Customer 2 Destination")
location.marker(pathLat1[2], pathLong1[2], title="Customer 3 Destination")

#marker for hub
location.marker(DHlat[0], DHlong[0], title="City-link Express, Port Klang")
location.marker(DHlat[1], DHlong[1], title="Pos Laju, Petaling Jaya")
location.marker(DHlat[2], DHlong[2], title="GDEX, Batu Caves")
location.marker(DHlat[3], DHlong[3], title="J&T, Kajang")
location.marker(DHlat[4], DHlong[4], title="DHL, Sungai Buloh")

location.apikey = API_key
location.draw('map1.html')
IFrame(src='map1.html', width=800, height=600)

```





<iframe
    width="800"
    height="600"
    src="map1.html"
    frameborder="0"
    allowfullscreen
></iframe>



