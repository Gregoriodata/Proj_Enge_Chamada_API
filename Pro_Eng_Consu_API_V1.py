import pandas as pd
import json
import requests
from Funcao_Chamada_API import Clima
from Funcao_Chamada_API_Cidade import localizacao


local = localizacao()
dados = local.consulta()
# print(dados)

nomes_minicipios = [municipio['nome']for municipio in dados]

print(nomes_minicipios)


# cidade = f'Curitiba'

# url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&appid=08dcfb72931ed589d85b8d6b3cb63861'

# response = requests.get(url).json()
# # print(response)

# ret = response

# # print(list(ret.items())[0])
# # print(ret)

# #Leitura

# cidade = ret.get('name')
# clima = ret['weather'][0]['main']
# print(cidade, clima)
