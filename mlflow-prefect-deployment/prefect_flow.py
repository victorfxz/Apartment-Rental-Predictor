from prefect import flow, task
from scripts.train import train_model, load_dataset
from sklearn.model_selection import train_test_split
import os

@task
def load_and_split_data():
    file_path = os.path.join(os.path.dirname(__file__), "data/sao-paulo-properties.csv")
    X, y = load_dataset(file_path)
    return train_test_split(X, y, test_size=0.2, random_state=42)

@task
def train(X_train, y_train):
    return train_model(X_train, y_train)

@flow(name="apartment-price-prediction")
def house_price_prediction_flow():
    X_train, X_test, y_train, y_test = load_and_split_data()
    model, scaler = train(X_train, y_train)
    return model, scaler

if __name__ == "__main__":
    house_price_prediction_flow()



