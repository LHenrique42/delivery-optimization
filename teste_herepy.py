import herepy
import json

class Pedido:

    def __init__(self, nome, telefone, endereco, idCarga, pesoCarga):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.idCarga = idCarga
        self.pesoCarga = pesoCarga
        self.entregue = False 
    
    def imprimirPedido(self):
        print(self.nome + ' ' + self.telefone + ' ' + self.endereco + ' ' + self.idCarga + ' ' + self.pesoCarga)

#função que lê um arquivo de entrada com todos os pedidos e retonar um vetor do tipo Pedido contendo todos os pedidos  
def leituraPedido(nomeArquivo):

    arq = open(nomeArquivo, 'r')
    texto = arq.readlines()

    vetorPedidos = []
    
    for linha in texto:
        tmp = []
        for x in linha.split(','):
            tmp.append(x)
        nome = tmp[0]
        telefone = tmp[1]
        endereco = tmp [2] + ' ' + tmp[3] + ' ' + tmp[4] + ' ' + tmp[5]
        id = tmp[6]
        peso = tmp[7]
    
        pedido = Pedido(nome, telefone, endereco,id,peso)
        vetorPedidos.append(pedido)
        #pedido.imprimirPedido()
    arq.close()

    return vetorPedidos



def calculoDistancias(endereco1, endereco2):

    routingApi = herepy.RoutingApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

    geocoderApi = herepy.GeocoderApi('o6i9v6u7AQdyeVTbJwWw', 'kp3lhUcL0KmT-gODan27iw')

    #response2 = routingApi.truck_route([11.0, 12.0], [22.0, 23.0], [herepy.RouteMode.truck, herepy.RouteMode.fastest])

    #####      Endereco 1     #####

    localizacaoCompleta = geocoderApi.free_form(endereco1)
    data = json.loads(str(localizacaoCompleta))

    pontoLatitude= data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    #print("pontoLatitude:", pontoLatitude)

    pontoLongitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    #print("pontoLongitude:", pontoLongitude)

    posicaoEndereco1 = []

    posicaoEndereco1.append(float(pontoLatitude))
    posicaoEndereco1.append(float(pontoLongitude))

    #Imprimir JSON
    #print(json.dumps(data, indent=4, sort_keys=True)) 
    #response = geocoderApi.street_intersection('Joao Bento Silvares Sao Mateus Espirito Santo Brasil', 'Nelson Fundao Sao Mateus Espirito Santo Brasil')

    
    #####      Endereco 2     #####

    localizacaoCompleta = geocoderApi.free_form(endereco2)
    data = json.loads(str(localizacaoCompleta))

    pontoLatitude= data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    #print("pontoLatitude:", pontoLatitude)

    pontoLongitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    #print("pontoLongitude:", pontoLongitude)

    posicaoEndereco2 = []

    posicaoEndereco2.append(float(pontoLatitude))
    posicaoEndereco2.append(float(pontoLongitude))


    #####      Calcula distancia entre os dois enderecos     #####
    response = routingApi.truck_route(posicaoEndereco1, posicaoEndereco2, [herepy.RouteMode.car, herepy.RouteMode.fastest])
    #print (response)

    data = json.loads(str(response))
    #print(json.dumps(data, indent=4, sort_keys=True))
    print("Distancia em metros")
    print (data['response']['route'][0]['summary']['distance'])
    print("Tempo em segundos")
    print (data['response']['route'][0]['summary']['travelTime'])



def principal():

    lista = leituraPedido('ArquivoEntrada.csv')
    calculoDistancias(lista[0].endereco, lista[1].endereco)



principal()