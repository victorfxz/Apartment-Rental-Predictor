import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os

mlflow.set_tracking_uri("http://127.0.0.1:5000")

def load_dataset(file_path):
    data = pd.read_csv(file_path)
    features = ['rooms', 'size', 'latitude', 'longitude']
    target = 'price'
    return data[features], data[target]

def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    return model, scaler

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/sao-paulo-properties.csv")
    X, y = load_dataset(file_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mlflow.start_run() as run:
        model, scaler = train_model(X_train, y_train)
        
        mlflow.sklearn.log_model(model, "model")
        scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
        with open(scaler_path, "wb") as f:
            pickle.dump(scaler, f)
        mlflow.log_artifact(scaler_path)
        
        mlflow.log_params({
            "model_type": "LinearRegression",
            "scaler": "StandardScaler"
        })

    print(f"Model trained and logged to MLflow with run_id: {run.info.run_id}")
