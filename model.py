import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

np.random.seed(42)
n_samples = 2500

data = {
    'ano': np.random.randint(2015, 2025, n_samples),
    'km': np.random.randint(1000, 150000, n_samples),
    'motor': np.random.choice([1.0, 1.4, 1.6, 2.0, 2.5], n_samples),
    'marca': np.random.choice([1, 2, 3], n_samples)
}
df = pd.DataFrame(data)

def calcular_preco(row):
    preco_base = 58000 
    
    adicional_motor = row['motor'] * 22000 
    
    fator_marca = 1 + ((row['marca'] - 1) * 0.55)
    
    idade = 2025 - row['ano']
    
    desconto_idade = idade * 2800  
    
    desconto_km = row['km'] * 0.11 
    
    valor = (preco_base + adicional_motor) * fator_marca - desconto_idade - desconto_km
    
    return max(valor, 20000)

df['preco'] = df.apply(calcular_preco, axis=1)

X = df[['ano', 'km', 'motor', 'marca']]
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

score = r2_score(y_test, modelo.predict(X_test))
print(f"Modelo 'Tabela Fipe 2025' Treinado! Precisão (R²): {score:.2f}")

pickle.dump(modelo, open('model.pkl', 'wb'))
print("Arquivo 'model.pkl' atualizado!")