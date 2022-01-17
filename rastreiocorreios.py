#ConsultaCEP

#importa as bibliotecas
import requests

# cabeçalho decorado
print('###'*25)
print('                 RASTREIO DE ENCOMENDAS 1.1')
print('###'*25)

#pega o cep
codigo_rastreio = input('Digite o código de rastreio para a consulta: ')

#faz a conexão com a API da ViaCep
request = requests.get('https://proxyapp.correios.com.br/v1/sro-rastro/{}'.format(codigo_rastreio))
resp_consulta = (request.json())
#print(resp_consulta)

#Verifica se o CEP existe e retorna seus dados.
continua = 's'
#while continua == 'S':
#if 'sro-020' in resp_consulta['objetos'][0]['mensagem'][0]:
    #print(dadosendereco)

listaeventos = []
listaeventos2 = []
i = 0
try:
    while i < len(resp_consulta['objetos'][0]['eventos'][0]):
        listaeventos.append(resp_consulta['objetos'][0]['eventos'][i])
        i += 1
    #print(listaeventos)

    controle = 0
    for c in listaeventos:
        listaeventos2.append(listaeventos[controle])
        controle += 1

    controle = 0
    print('=-='*25)
    print('=== PESQUISANDO ENCOMENDA NÚMERO {} ==='.format(codigo_rastreio))
    for x in range(len(listaeventos2)):
        print('|| Data: {}'.format(listaeventos2[x]['dtHrCriado']))
        print('|| Situação: [{}] - {}'.format(listaeventos2[x]['codigo'],listaeventos2[x]['descricao']))
        print('=-=' * 25)
        x += 1
except:
    print('Objeto não localizado ou código inválido. Verifique o código e se ele foi postado e tente novamente!')

