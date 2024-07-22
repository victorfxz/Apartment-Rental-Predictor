from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Função para carregar e pré-processar o conjunto de dados
def load_dataset(file_path):
    real_estate_data = pd.read_csv(file_path)
    real_estate_data.columns = real_estate_data.columns.str.lower().str.replace(' ', '_')
    features = ['rooms', 'size', 'latitude', 'longitude']
    target = 'price'
    X = real_estate_data[features]
    y = real_estate_data[target]
    return X, y

# Função para treinar o modelo
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Carrega e pré-processa o conjunto de dados
file_path = "data/sao-paulo-properties.csv"
X, y = load_dataset(file_path)

# Divide o conjunto de dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina o modelo
model = train_model(X_train, y_train)

@app.route('/front-end/predict', methods=['GET'])
def home():
    return "API de Previsão de Preços Imobiliários"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        rooms = data['rooms']
        size = data['size']
        latitude = data['latitude']
        longitude = data['longitude']
        
        # Prepara o vetor de recursos
        features = pd.DataFrame([[rooms, size, latitude, longitude]], 
                                columns=['rooms', 'size', 'latitude', 'longitude'])
        
        # Previsão
        prediction = model.predict(features)[0]
        return jsonify({'predicted_price': prediction})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)