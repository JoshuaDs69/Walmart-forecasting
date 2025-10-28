import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import warnings, os

warnings.filterwarnings("ignore")

# 1️⃣ Carga de datos
DATA_PATH = os.path.join("data", "processed", "walmart_sales_clean.csv")
df = pd.read_csv(DATA_PATH)
TARGET = "Ventas_Semanales"
X = df.drop(columns=[TARGET])
y = df[TARGET]

# 2️⃣ División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3️⃣ Configura experimento
mlflow.set_experiment("Walmart Forecasting - Boosting Models")

# 4️⃣ Modelos y parámetros
models = {
    "LightGBM_300_005": LGBMRegressor(n_estimators=300, learning_rate=0.05, random_state=42),
    "LightGBM_500_003": LGBMRegressor(n_estimators=500, learning_rate=0.03, max_depth=8, random_state=42),
    "XGBoost_500_03": XGBRegressor(n_estimators=500, learning_rate=0.03, max_depth=6, random_state=42, subsample=0.8),
    "CatBoost_400_05": CatBoostRegressor(iterations=400, learning_rate=0.05, depth=8, verbose=0, random_state=42),
    "RandomForest_300": RandomForestRegressor(n_estimators=300, max_depth=10, random_state=42)
}

# 5️⃣ Entrenamiento y logging en MLflow
for model_name, model in models.items():
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        # Métricas
        r2 = r2_score(y_test, preds)
        rmse = sqrt(mean_squared_error(y_test, preds))

        # Logging de parámetros
        mlflow.log_param("model_name", model_name)
        if hasattr(model, "n_estimators"):
            mlflow.log_param("n_estimators", getattr(model, "n_estimators", None))
        if hasattr(model, "learning_rate"):
            mlflow.log_param("learning_rate", getattr(model, "learning_rate", None))
        if hasattr(model, "max_depth"):
            mlflow.log_param("max_depth", getattr(model, "max_depth", None))

        # Logging de métricas
        mlflow.log_metric("R2", r2)
        mlflow.log_metric("RMSE", rmse)

        # Guardar modelo
        mlflow.sklearn.log_model(
            sk_model=model,
            name=f"{model_name}_model",
            input_example=X_test.iloc[:1]
        )

        print(f"✅ {model_name} | R²={r2:.4f} | RMSE={rmse:.2f}")
