import mlflow
import mlflow.sklearn
import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt
import os

# 1️⃣ Carga de datos procesados
DATA_PATH = os.path.join("data", "processed", "walmart_sales_clean.csv")
df = pd.read_csv(DATA_PATH)

# Asegúrate de usar el nombre correcto de tu variable objetivo:
TARGET = "Ventas_Semanales"
X = df.drop(columns=[TARGET])
y = df[TARGET]

# 2️⃣ División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3️⃣ Configuración del experimento MLflow
mlflow.set_experiment("Walmart Forecasting")

with mlflow.start_run(run_name="LightGBM_300_005"):
    model = LGBMRegressor(n_estimators=300, learning_rate=0.05, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # 4️⃣ Métricas
    r2 = r2_score(y_test, preds)
    rmse = sqrt(mean_squared_error(y_test, preds))

    # 5️⃣ Logging
    mlflow.log_param("data_version", os.path.basename(DATA_PATH))
    mlflow.log_param("n_estimators", 300)
    mlflow.log_param("learning_rate", 0.05)
    mlflow.log_metric("R2", r2)
    mlflow.log_metric("RMSE", rmse)

    # Guarda el modelo y su firma
    mlflow.sklearn.log_model(
        sk_model=model,
        name="model",
        input_example=X_test.iloc[:1]
    )

print(f"✅ Run registrado en MLflow | R²={r2:.4f} | RMSE={rmse:.2f}")
