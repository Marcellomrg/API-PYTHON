
# %%
import requests
import json 
cep = input("Digite o CEP: ").strip()

def buscacep(cep):

    if not cep.isdigit() and len(cep)==8:
         print("CEP INVALIDO")
         return

    try:

        url = "https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url.format(cep=cep))
        


    except requests.exceptions.RequestException as e:
        print(f'Erro na requisicao: {e}')

    if resposta.status_code == 200:
        dados = resposta.json()

    with open("ceps.json",mode='w') as open_file:
        json.dump(dados,open_file,ensure_ascii=False,indent=4)


buscacep(cep)

# %%
