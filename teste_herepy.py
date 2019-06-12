import herepy

routingApi = herepy.RoutingApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

geocoderApi = herepy.GeocoderApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

#response = routingApi.truck_route([11.0, 12.0], [22.0, 23.0], [herepy.RouteMode.truck, herepy.RouteMode.fastest])
response = geocoderApi.free_form('200 S Mathilda Sunnyvale CA')

print (response)