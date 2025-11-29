import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Carrega o modelo de CARROS que acabamos de criar
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    print("Erro: model.pkl não encontrado. Rode o model.py primeiro.")

@app.route("/")
def home():
    return "API DE CARROS (Versão 2.0 - Com Marcas)"

@app.route("/api/predict", methods=["POST"])
def results():
    data = request.get_json(force=True)
    
    # Pegando os 4 dados enviados pelo Frontend
    # Convertendo para float para garantir que o cálculo funcione
    ano = float(data['ano'])
    km = float(data['km'])
    motor = float(data['motor'])
    marca = float(data['marca']) # 1, 2 ou 3
    
    # Cria o array na MESMA ORDEM que foi treinado no model.py
    features = [np.array([ano, km, motor, marca])]
    
    # Faz a previsão
    prediction = model.predict(features)
    
    # Formata para R$ bonito
    resultado_formatado = f"R$ {prediction[0]:,.2f}"
    
    return jsonify(resultado_formatado)

if __name__ == "__main__":
    app.run(port=5000, debug=True)