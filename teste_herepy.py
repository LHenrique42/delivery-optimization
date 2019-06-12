import herepy
import json

class Cliente:
    nome = ""
    telefone = 0
    endereco = ''
    idCarga = 0
    pesoCarga = 0.0 

    def __init__(self, nome, telefone, endereco, idCarga, pesoCarga):
        self.nome = nome
        self.endereco = endereco
        self.idCarga = idCarga
        self.pesoCarga = pesoCarga


testeCliente = Cliente("Mariana", 999999999, '407 Rua Nelson Fundao Fatima Sao Mateus Espirito Santo Brasil', 1, 10.2)

print(testeCliente.nome)

routingApi = herepy.RoutingApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

geocoderApi = herepy.GeocoderApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

#response2 = routingApi.truck_route([11.0, 12.0], [22.0, 23.0], [herepy.RouteMode.truck, herepy.RouteMode.fastest])


minhaCasa = geocoderApi.free_form('407 Rua Nelson Fundao Fatima Sao Mateus Espirito Santo Brasil')
data = json.loads(str(minhaCasa))

pontoLatitude= data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
print("pontoLatitude:", pontoLatitude)

pontoLongitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
print("pontoLongitude:", pontoLongitude)

matEnderecos  = []
linha = []

linha.append(float(pontoLatitude))
linha.append(float(pontoLongitude))

matEnderecos.append(linha)

print(matEnderecos)


#print(json.dumps(data, indent=4, sort_keys=True))

#response = geocoderApi.street_intersection('Joao Bento Silvares Sao Mateus Espirito Santo Brasil', 'Nelson Fundao Sao Mateus Espirito Santo Brasil')

response = routingApi.truck_route(matEnderecos[0],[-18.7164558, -39.844873], [herepy.RouteMode.car, herepy.RouteMode.fastest])
#print (response)

data = json.loads(str(response))
#print(json.dumps(data, indent=4, sort_keys=True))
print("Distancia em metros")
print (data['response']['route'][0]['summary']['distance'])
print("Tempo em segundos")
print (data['response']['route'][0]['summary']['travelTime'])