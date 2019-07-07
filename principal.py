import herepy
import json

class Pedido:

    def __init__(self, nome, telefone, endereco, idCarga, pesoCarga, turno):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.idCarga = idCarga
        self.pesoCarga = pesoCarga
        self.entregue = False 
        self.turno = turno
    
    def imprimirPedido(self):
        print('Cliente: ' + self.nome + '\nTelefone: ' + self.telefone + '\nEndereco: ' + self.endereco + '\nId Carga: ' + self.idCarga + '\nPeso Carga: ' + self.pesoCarga + '\nTurno: ' + self.turno + '\n\n')
    
    def conteudoPedido(self):
        return 'Cliente: ' + self.nome + '\nTelefone: ' + self.telefone + '\nEndereco: ' + self.endereco + '\nId Carga: ' + self.idCarga + '\nPeso Carga: ' + self.pesoCarga + '\nTurno: ' + self.turno + '\n\n'
    
    def comparaTurno(self, turno):
        if self.turno == turno:
            return True
        else:
            return False

#funcao que le um arquivo de entrada com todos os pedidos e retonar um vetor do tipo Pedido contendo todos os pedidos  
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
        endereco = tmp [2] + ' ' + tmp[3] + ' ' + tmp[4] + ' ' + tmp[5] + ' ' + tmp[6]
        id = tmp[7]
        peso = tmp[8]
        turno = tmp[9]
    
        pedido = Pedido(nome, telefone, endereco, id, peso, turno.rstrip())
        vetorPedidos.append(pedido)
        #pedido.imprimirPedido()
    arq.close()

    return vetorPedidos

#Funcao que calcula a distancia entre duas ruas
#Leva em consideracao que o transporte esta sendo feito por caminhao
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

    print(endereco1 + " - " + endereco2)
    print("Distancia em metros")
    print (data['response']['route'][0]['summary']['distance'])
    print("Tempo em segundos")
    print (data['response']['route'][0]['summary']['travelTime'])

    #retorna a distancia e o tempo
    return data['response']['route'][0]['summary']['distance'], data['response']['route'][0]['summary']['travelTime']



def  proxEndereco(ponto1, vetorPedidos, roteiroEntrega, turno):

    menor = 100000000000000
    posMenor = 0
    tempoEntrega = -1

    for ponto2 in vetorPedidos:
        if turno == ponto2.turno:
            distancia, tempo = calculoDistancias(ponto1, ponto2.endereco)
            if menor > distancia:
                menor = distancia
                tempoEntrega = tempo
                posMenor = vetorPedidos.index(ponto2)

    if tempoEntrega != -1:
        ponto2 = vetorPedidos[posMenor]

        #Adiciona ao roteiro o pedido com a posicao mais proxima a atual 
        ponto2.entregue = True
        roteiroEntrega.append(ponto2)

        #remove o pedido do vetor pois ele ja esta no roteito "foi entrgue"
        del(vetorPedidos[posMenor])
    else:
        ponto1 = ponto2
    return ponto2, tempoEntrega



def salvarRoteiro(roteiroEntrega, turno, opcaoEscrita):

    arquivo = open('Roteiro_Entrega.txt', opcaoEscrita)
    i = 1
    arquivo.write(turno + ': \n\n')
    for local in roteiroEntrega:
        arquivo.write('Entrega ' + str(i) + ': \n')
        arquivo.write(local.conteudoPedido())
        i+=1

    arquivo.close()

    
def principal():

    listaEntregas = leituraPedido('entrada.csv')
    roteiroEntrega = []

    pesoMaxCaminhao = 5000
    pesoPreenchido = 0
    tempoViagem = 0
    tempoTurno = 0
    i = 0

    for pedido in listaEntregas:
        pedido.imprimirPedido()


    #Posicao do local que fica o deposito
    deposito = "R. Sao Mateus, Sao Mateus - ES, 29938-015"
    pontoAtual, tempoViagem = proxEndereco(deposito, listaEntregas, roteiroEntrega, 'manha')
    if  tempoViagem != -1:
        pesoPreenchido += int(pontoAtual.pesoCarga)
        # O tempo para fazer a entraga leva em media 30 minutos = 1800 segundos
        tempoTurno = tempoTurno + tempoViagem + 1800
        print(tempoTurno)

    ##############  Turno da Manha ####################

    #chamar esse funcao ate todos os pedidos tenham sido atendidos
    #Quando o tempoViagem for igual a -1 significa que nao tem mais entregas nesse turno
    # O turno da manha tem uma duracao de 3.5 horas = 126000 segundos

    while i<len(listaEntregas) and pesoMaxCaminhao >= pesoPreenchido and tempoTurno < 126000:
        pontoAtual, tempoViagem = proxEndereco(pontoAtual.endereco, listaEntregas, roteiroEntrega, "manha")
        if  tempoViagem != -1:
            pesoPreenchido += int(pontoAtual.pesoCarga)
            # O tempo para fazer a entraga leva em media 30 minutos = 1800 segundos
            tempoTurno = tempoTurno + tempoViagem + 1800
        else:
            i+=1
        
    salvarRoteiro(roteiroEntrega, 'Turno da Manha', 'w')
    
    #inicializando variaveis novamente
    tempoTurno = 0
    tempoViagem = 0
    i=0
    roteiroEntrega = []

        ##############  Turno da Tarde ####################

    #chamar esse funcao ate todos os pedidos tenham sido atendidos
    #Quando o tempoViagem for igual a -1 significa que nao tem mais entregas nesse turno
    # O turno da tarde tem uma duracao de 4.5 horas = 162000 segundos

    while i<len(listaEntregas) and pesoMaxCaminhao >= pesoPreenchido and tempoTurno < 162000:
        pontoAtual, tempoViagem = proxEndereco(pontoAtual.endereco, listaEntregas, roteiroEntrega, "tarde")
        if  tempoViagem != -1:
            pesoPreenchido += int(pontoAtual.pesoCarga)
            # O tempo para fazer a entraga leva em media 30 minutos = 1800 segundos
            tempoTurno = tempoTurno + tempoViagem + 1800
        else:
            i+=1
        
    salvarRoteiro(roteiroEntrega, 'Turno da Tarde', 'a')


    if listaEntregas != [] and pesoMaxCaminhao >= pesoPreenchido:
        salvarRoteiro(listaEntregas, 'Nao Foi Possivel Fazer a Entraga', 'a')
      
        


principal()
