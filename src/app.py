from fastapi import FastAPI
import mlflow
import pandas as pd

app = FastAPI(title="Walmart Forecasting API", description="API para predicciones con el modelo registrado en MLflow")

# Configurar conexión al servidor MLflow
mlflow.set_tracking_uri("http://localhost:5000")

# Cargar el modelo desde el registro
MODEL_NAME = "Walmart_Best_Model"
VERSION = 2
model = mlflow.pyfunc.load_model(model_uri=f"models:/{MODEL_NAME}/{VERSION}")

@app.get("/")
def home():
    return {"mensaje": "API de predicciones Walmart lista 🚀"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediccion": prediction.tolist()}
