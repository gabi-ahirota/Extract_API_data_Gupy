import requests
import json
import os

url = "https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

response = requests.get(url)

if response.status_code == 200:
    
    dados = response.json()
    print(dados)

    diretorio = 'dados_vagas'
    nome_arquivo = os.path.join(diretorio, 'dados_api.json')
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        
    print(f'Dados salvos com sucesso no arquivo {nome_arquivo}')
else:
    print(f"Erro na requisicao: {response.status_code}")

