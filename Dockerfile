FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt mlflow pymysql
COPY . .
EXPOSE 5000
CMD ["mlflow", "server", "--backend-store-uri", "mysql+pymysql://root:admin@mysql-mlflow/mlflow_db", "--default-artifact-root", "./mlruns", "--host", "0.0.0.0", "--port", "5000"]
