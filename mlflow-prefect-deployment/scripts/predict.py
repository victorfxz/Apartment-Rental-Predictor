from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pickle
import os
import pandas as pd
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Configuração do MLflow
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
RUN_ID = "1f967d6e31bd444a83565e54ebe62563"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
model = mlflow.sklearn.load_model(f'runs:/{RUN_ID}/model')

# Carregar o scaler
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

# Configuração do PostgreSQL
DB_HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'postgres'
DB_PASSWORD = '3099'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def log_metrics_to_db(request_count, request_latency):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO prediction_metrics (request_count, request_latency, timestamp)
        VALUES (%s, %s, %s);
    """, (request_count, request_latency, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

def preprocess(features):
    return scaler.transform(pd.DataFrame([features]))

def predict(features):
    processed_features = preprocess(features)
    return model.predict(processed_features)[0]

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    start_time = datetime.now()
    try:
        features = [data['rooms'], data['size'], data['latitude'], data['longitude']]
        prediction = predict(features)
        request_latency = (datetime.now() - start_time).total_seconds()
        log_metrics_to_db(1, request_latency)
        return jsonify({'predicted_price': float(prediction)})
    except (KeyError, TypeError) as e:
        return jsonify({'error': f'Invalid input data: {str(e)}'}), 400

if __name__ == "__main__":
    # Inicialização do banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_metrics (
            id SERIAL PRIMARY KEY,
            request_count INTEGER,
            request_latency FLOAT,
            timestamp TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
    app.run(debug=True, host='0.0.0.0', port=9696)
