import random

def geradorNomesAleatorios():

    arq = open('nomes.txt', 'r')
    nomes = arq.readlines()

    listaNomes = [] 
    for linha in nomes:
        listaNomes.append(linha.rstrip())

    arq.close()

    arq = open('sobrenomes.txt', 'r')
    sobrenomes = arq.readlines()

    listaSobrenomes = []

    for linha in sobrenomes:
        listaSobrenomes.append(linha.rstrip())

    
    nomeCompleto = listaNomes[random.randrange(len(listaNomes))] + ' ' + listaSobrenomes[random.randrange(len(listaSobrenomes))]

    print(nomeCompleto)

    return nomeCompleto

def geradorTelefonesAleatorios():

    numero = '99'
    i = 0
    while i < 7:
        numero += str(random.randrange(0, 9))
        i += 1

    print (numero)

    return numero

def geradorEnderecosAleatorios():

    endereco = str(random.randrange(1, 10000)) + ','

    arq = open('enderecos.csv', 'r')
    texto = arq.readlines()

    listaEnderecos = [] 
    for linha in texto:
        listaEnderecos.append(linha.rstrip())

    endereco += listaEnderecos[random.randrange(len(listaEnderecos))]

    print(endereco)

    return endereco
    

def gerarArqEntrada():

    arquivo = open('entrada.csv','w')
    maxPedidos = random.randrange(1, 20)
    i=0
    print(maxPedidos)
    while i<maxPedidos:
        nome = geradorNomesAleatorios()
        telefone = geradorTelefonesAleatorios() 
        endereco = geradorEnderecosAleatorios()
        numId = str(i+1)
        peso = str(random.randrange(1, 200))
        arquivo.write(nome + ',' + telefone + ',' + endereco + ',' + numId + ',' + peso + '\n')
        i+=1

    arquivo.close()

gerarArqEntrada()
    



