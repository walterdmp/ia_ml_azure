import requests

# Testando localmente
url = 'http://127.0.0.1:5000/api/predict'

# Exemplo: BMW (Marca 3), Ano 2022, Motor 2.0
dados = {
    'ano': 2022,
    'km': 30000,
    'motor': 1.0,
    'marca': 1  # <--- Testando a nova variável LUXO
}

r = requests.post(url, json=dados)
print("Valor previsto:", r.json())