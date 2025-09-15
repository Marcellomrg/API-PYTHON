# %%
import pandas as pd
import requests
from io import StringIO

# %%
header = {'User-Agent':'Marcello'}

url_df = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"

resposta_df = requests.get(url_df,headers=header)

dados = resposta_df.text
dados

# %%
data_df = pd.read_html(StringIO(dados))
data_df[1]

# %%

# %%
