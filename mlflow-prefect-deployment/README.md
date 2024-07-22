# README

This project includes a set of scripts for training, predicting, and testing machine learning models using MLflow and Prefect to predict apartment rental prices in the city of São Paulo, Brazil. The following sections describe how to run each script and the purpose of each command.

## Setup

Before running any scripts, make sure you have installed all the required dependencies. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## MLflow Server

To start the MLflow server, run the following command:

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0
```

This command starts the MLflow server with a SQLite database as the backend store and sets the default artifact root to the `mlruns` directory. The server listens on all interfaces (`0.0.0.0`).

## Training

To train the machine learning model, run the following command:

```bash
python scripts/train.py
```

This script trains the model and logs the metrics, parameters, and artifacts to the MLflow server.

## Prediction

To make predictions using the trained model, run the following command:

```bash
python scripts/predict.py
```

This script loads the trained model from the MLflow server and makes predictions on new data.

## Prefect Server

To start the Prefect server, run the following command:

```bash
prefect server start
```

This command starts the Prefect server, which is used to orchestrate and schedule the machine learning workflows.

## Prefect Flow

To run the Prefect flow, run the following command:

```bash
python prefect_flow.py
```

This script defines a Prefect flow that includes the training and prediction steps. The flow can be scheduled and monitored using the Prefect server.

## Testing Prediction

To test the prediction script, run the following command:

```bash
python scripts/test_predict.py
```
