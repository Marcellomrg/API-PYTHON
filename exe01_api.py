# %%

import requests
import json

url = "https://httpbin.org/get"

resposta = requests.get(url)

conteudo = resposta.json()

print(f'Status code: {resposta.status_code }\n Conteudo:{conteudo}')

# %%
