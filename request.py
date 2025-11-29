import requests

# 👇 SEU LINK DA AZURE (Com a rota /api/predict)
url = 'https://ml-flask-g8cje0b8d5bjhwg6.eastus2-01.azurewebsites.net/api/predict'

# Dados de teste (Um carro de luxo para ver se o valor vem alto)
dados_teste = {
    'ano': 2023,
    'km': 15000,
    'motor': 2.0,
    'marca': 3  # 3 = Luxo
}

print(f"Enviando dados para a Azure: {dados_teste}")
print("Aguardando resposta...")

try:
    # Faz o pedido POST para a nuvem
    r = requests.post(url, json=dados_teste)
    
    if r.status_code == 200:
        print(f"✅ SUCESSO! A Azure respondeu: {r.json()}")
    else:
        print(f"❌ ERRO: Código {r.status_code}")
        print(r.text)
        
except Exception as e:
    print(f"Erro na conexão: {e}")