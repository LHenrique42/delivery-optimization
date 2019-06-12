import herepy

routingApi = herepy.RoutingApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

geocoderApi = herepy.GeocoderApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

#response2 = routingApi.truck_route([11.0, 12.0], [22.0, 23.0], [herepy.RouteMode.truck, herepy.RouteMode.fastest])

#response = geocoderApi.free_form('407 Rua Nelson Fundao Fatima Sao Mateus Espirito Santo Brasil')

#response = geocoderApi.street_intersection('Joao Bento Silvares Sao Mateus Espirito Santo Brasil', 'Nelson Fundao Sao Mateus Espirito Santo Brasil')

response = routingApi.car_route([- 18.7176197, -39.8435499],[-18.7164558, -39.844873], [herepy.RouteMode.car, herepy.RouteMode.fastest])

print (response)