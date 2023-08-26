import requests

def analisar_proposta(campos):
    url = "https://loan-processor.digitalsys.com.br/api/analise-credito/"
    payload = campos
    response = requests.post(url, json=payload)
    data = response.json()
    return data['status']
