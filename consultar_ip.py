# %%
import requests
import json



def MostrarIp():

    url_PegarIP = "https://httpbin.org/ip"
    resposta = requests.get(url_PegarIP)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['origin']

def LocalizarIP():

    url_LocalizarIP = "http://ip-api.com/json/{ip}"
    resposta = requests.get(url_LocalizarIP.format(ip=MostrarIp()))
    if resposta.status_code == 200:
        dados = resposta.json()
        print(json.dumps(dados,ensure_ascii=False,indent=4))



print(MostrarIp())
LocalizarIP()

# %%
