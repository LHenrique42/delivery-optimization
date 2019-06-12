from geopy.geocoders import Nominatim 
from geopy.distance import geodesic

#Algoritmo que calcula a distancia entre duas ruas
#Calculo feito pelas longitude e latitude

geolocator = Nominatim()

location1 = geolocator.geocode("Joao Bento Silvares Sao Mateus Espirito Santo Brasil") 
print ("Location 1:" , (location1.latitude, location1.longitude))

local1 = (float(location1.latitude), float(location1.longitude))

location2 = geolocator.geocode("Nelson Fundao Sao Mateus Espirito Santo Brasil") 
print ("Location 2:" , (location2.latitude, location2.longitude))

local2 = (float(location2.latitude), float(location2.longitude))

#Calcula a distancia entre as duas cidades em km
print ("Distancia: ", (geodesic(local1, local2).km))

