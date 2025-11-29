import requests

url = 'https://ml-flask-g8cje0b8d5bjhwg6.eastus2-01.azurewebsites.net/api/predict'

dados_teste = {
    'ano': 2023,
    'km': 15000,
    'motor': 2.0,
    'marca': 3 
}

print(f"Enviando dados para a Azure: {dados_teste}")
print("Aguardando resposta...")

try:
    r = requests.post(url, json=dados_teste)
    
    if r.status_code == 200:
        print(f"✅ SUCESSO! A Azure respondeu: {r.json()}")
    else:
        print(f"❌ ERRO: Código {r.status_code}")
        print(r.text)
        
except Exception as e:
    print(f"Erro na conexão: {e}")