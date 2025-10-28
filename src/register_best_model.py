import mlflow
from mlflow.tracking import MlflowClient
import pandas as pd

# 1️⃣ Configura el nombre del experimento
EXPERIMENT_NAME = "Walmart Forecasting - Boosting Models"
MODEL_NAME = "Walmart_Best_Model"

# 2️⃣ Obtiene ID del experimento
client = MlflowClient()
experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

if experiment is None:
    raise ValueError(f"❌ No se encontró el experimento '{EXPERIMENT_NAME}'.")

experiment_id = experiment.experiment_id

# 3️⃣ Recupera todos los runs
runs = client.search_runs(
    experiment_ids=[experiment_id],
    order_by=["metrics.R2 DESC"],
    max_results=10
)

# 4️⃣ Selecciona el mejor modelo (mayor R²)
best_run = runs[0]
run_id = best_run.info.run_id
r2 = best_run.data.metrics.get("R2")
rmse = best_run.data.metrics.get("RMSE")
model_name = best_run.data.params.get("model_name")

print(f"\n🏆 Mejor modelo encontrado:")
print(f"   • Nombre: {model_name}")
print(f"   • R² = {r2:.4f}")
print(f"   • RMSE = {rmse:.2f}")
print(f"   • run_id = {run_id}")

# 5️⃣ Registra el modelo en el Model Registry
model_uri = f"runs:/{run_id}/{model_name}_model"
result = mlflow.register_model(model_uri, MODEL_NAME)

print(f"\n✅ Modelo registrado exitosamente:")
print(f"   • Nombre registrado: {MODEL_NAME}")
print(f"   • Versión creada: {result.version}")
print(f"   • URI: {model_uri}")
