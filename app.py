import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Tenta carregar o modelo
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    print("Erro: model.pkl não encontrado.")

@app.route("/")
def home():
    return "API DE CARROS (Versão Final)"

@app.route("/api/predict", methods=["POST"])
def results():
    data = request.get_json(force=True)
    
    # Recebendo os dados
    ano = float(data['ano'])
    km = float(data['km'])
    motor = float(data['motor'])
    marca = float(data['marca'])
    
    features = [np.array([ano, km, motor, marca])]
    prediction = model.predict(features)
    
    
    valor_usa = f"{prediction[0]:,.2f}"
    
    valor_br = valor_usa.replace(',', 'X').replace('.', ',').replace('X', '.')
    
    return jsonify(f"R$ {valor_br}")

if __name__ == "__main__":
    app.run(port=5000, debug=True)