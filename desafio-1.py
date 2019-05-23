'''
Criptografia de Júlio César
Segundo o Wikipedia, criptografia ou criptologia (em grego: kryptós, “escondido”, e gráphein, “escrita”) é o estudo e prática de princípios e técnicas para comunicação segura na presença de terceiros, chamados “adversários”. Mas geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. Muitos aspectos em segurança da informação, como confidencialidade, integridade de dados, autenticação e não-repúdio são centrais à criptografia moderna. Aplicações de criptografia incluem comércio eletrônico, cartões de pagamento baseados em chip, moedas digitais, senhas de computadores e comunicações militares. Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:

Normal: a ligeira raposa marrom saltou sobre o cachorro cansado

Cifrado: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr

Regras
As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia.
No nosso caso os números e pontos serão mantidos, ou seja:
Normal: 1a.a

Cifrado: 1d.d

'''
# importando as libs
import json
import requests 
from hashlib import sha1

URL = "https://api.codenation.dev/v1/challenge/dev-ps" # global variable
TOKEN = "02275c9759b07c64af03e4e8cbe52d5fc8a68847"

# atualiza o arquivo json
def atualizar_json(data):
    with open('answer.json', 'w') as outfile:  
        json.dump(data, outfile)
    return

def decifrar():
    # param Token
    PARAMS = {'token' : TOKEN}

    # enviando get request e salvando o response como um objeto response
    r = requests.get(url = URL + "/generate-data", params = PARAMS) 
    
    # pegando data em json format 
    data = r.json() 

    numero_casas = data['numero_casas']
    cifrado = data['cifrado'].lower()

    alfabeto = 'abcdefghijklmnopqrstuvwxyz' # alfabeto auxiliar

    i = 0 # index da letra criptografada
    decifrado = '' # mensagem decifrada

    for c in cifrado:
        if c in alfabeto:
            i = alfabeto.index(c) - numero_casas
            decifrado += alfabeto[i]
        else:
            decifrado += c

    data['decifrado'] = decifrado

    # atualiza o arquivo json
    atualizar_json(data)

    resumo_criptografico = sha1(data['decifrado'].encode('utf-8'))
    data['resumo_criptografico'] = resumo_criptografico.hexdigest()
    atualizar_json(data)
    return 

def submeter():
    # param Token
    PARAMS = {'token' : TOKEN}
    response = requests.post(URL + "/submit-solution", files={"answer":open("answer.json", "rb")}, params = PARAMS)
    return 

decifrar()
submeter()



