import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# --- 1. Geração de Dados Simulados ---
np.random.seed(42)
n_samples = 1500 # Aumentamos a base para ficar mais inteligente

data = {
    'ano': np.random.randint(2015, 2025, n_samples),
    'km': np.random.randint(5000, 160000, n_samples),
    'motor': np.random.choice([1.0, 1.4, 1.6, 2.0, 2.5], n_samples),
    # NOVO CAMPO: 1=Popular, 2=Intermediário, 3=Luxo
    'marca': np.random.choice([1, 2, 3], n_samples)
}
df = pd.DataFrame(data)

# Função para dar lógica aos preços (O computador vai "aprender" isso aqui)
def calcular_preco(row):
    preco_base = 50000
    
    # Motor potente adiciona valor
    adicional_motor = row['motor'] * 15000
    
    # Marca de Luxo multiplica o valor
    # Se marca=1 (Popular) -> multiplica por 1.0
    # Se marca=2 (Intermed) -> multiplica por 1.4
    # Se marca=3 (Luxo)     -> multiplica por 2.0
    fator_marca = 1 + ((row['marca'] - 1) * 0.5)
    
    # Depreciação (Idade e KM tiram valor)
    idade = 2025 - row['ano']
    desconto_idade = idade * 2500
    desconto_km = row['km'] * 0.08
    
    valor = (preco_base + adicional_motor) * fator_marca - desconto_idade - desconto_km
    return max(valor, 15000) # Ninguém vende carro por menos de 15k aqui

df['preco'] = df.apply(calcular_preco, axis=1)

# --- 2. Treinamento ---
# Agora treinamos com 4 colunas!
X = df[['ano', 'km', 'motor', 'marca']]
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Validação
score = r2_score(y_test, modelo.predict(X_test))
print(f"Modelo Treinado! Precisão (R²): {score:.2f}")

# --- 3. Salvar ---
# Só precisamos salvar o modelo. Não precisa de 'names.pkl' para regressão.
pickle.dump(modelo, open('model.pkl', 'wb'))
print("Arquivo 'model.pkl' gerado com sucesso!")