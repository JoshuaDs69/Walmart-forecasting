import mlflow
import pandas as pd

# Conectar a MLflow
mlflow.set_tracking_uri("http://localhost:5000")

# Cargar el modelo registrado
model = mlflow.pyfunc.load_model("models:/Walmart_Best_Model/2")

# Simular datos de entrada
data = {
    "Tienda": 1,
    "Depto": 5,
    "Semana": 42,
    "Promociones": 1,
    "Temperatura": 25.6,
    "Desempleo": 7.1
}

df = pd.DataFrame([data])
prediction = model.predict(df)
print("Predicción de ventas semanales:", prediction[0])
