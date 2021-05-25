import json 
import requests
import urllib
file= open("C:/mat4/dests.txt", encoding="utf8")
file= file.read()
file= file.splitlines()
apiKey= ""
parms = dict()
information = dict()
MaxDistance = dict()
biggest= 0
biggest1= 0
biggest2= 0
nameOfCity = "null"
nameOfCity1 = "null"
nameOfCity2 = "null"
for line in file:
     Serviceurl ='https://maps.googleapis.com/maps/api/distancematrix/json?'
     parms['origins']='תל אביב'
     parms['destinations'] = line
     parms['key'] = apiKey
     url = Serviceurl + urllib.parse.urlencode(parms)
     response= requests.get(url)
     response= response.json()
     Dist= response['rows'][0]['elements'][0]['distance']['text']
     duration = response['rows'][0]['elements'][0]['duration']['text']
     address=line
     url1="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,apiKey)
     response1 = requests.get(url1).json() 
     location = response1['results'][0]['geometry']['location']
     information[line]= dict()
     information[line]["distance"]= Dist
     information[line]["duration"]= duration
     information[line]["location"]= location
     print("the data of " + line)
     print("the distance is: " +Dist)
     print("the duration is: " + duration)
     print("the location is: "+ str(location))
     print("")
     MaxDistance[line]= Dist
for x in file :
    if MaxDistance[x] > str(biggest):
        biggest1 = biggest
        biggest = MaxDistance[x]
        nameOfCity1= nameOfCity
        nameOfCity = x
    if MaxDistance[x]>str(biggest1)and MaxDistance[x]<str(biggest):
        biggest2 = biggest1
        biggest1 = MaxDistance[x]
        nameOfCity2= nameOfCity1
        nameOfCity1 = x
    if MaxDistance[x]>str(biggest2) and MaxDistance[x]<str(biggest1):
        biggest2 = MaxDistance[x]
        nameOfCity2 = x
print(nameOfCity , nameOfCity1, nameOfCity2)