import mlflow

mlflow.register_model(
    "runs:/a6b1bee0f8d746f5a9d3264d98714ed7/model",
    "Walmart_Sales_Forecast_Model"
)
