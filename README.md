# 🧠 Walmart Sales Forecasting
Predicción de ventas semanales en tiendas Walmart mediante modelos de Machine Learning supervisado, gestionados y desplegados en un entorno reproducible con Docker y MLflow.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/1bd9fa66-2a73-4ec3-88b3-6e6472f73cc8" />


Este proyecto aplica técnicas de regresión y análisis predictivo para estimar las ventas semanales, optimizando la toma de decisiones en la gestión de inventarios y planeamiento operativo.

---

## 📊 Dataset
- **Fuente:** [Kaggle – Walmart Store Sales Forecasting](https://www.kaggle.com/datasets)
- **Periodo:** 2010–2012  
- **Variables principales:** Fecha, Tienda, Ventas Semanales, CPI, Desempleo, Día Feriado, Temperatura, Fuel Price.

---

## ⚙️ Modelos y resultados

| Modelo | R² | RMSE |
|---------|-----|-------|
| Random Forest | 0.935 | 144,150 |
| XGBoost | 0.966 | 104,106 |
| LightGBM | **0.9757** | **88,450** |
| CatBoost | 0.963 | 108,724 |

📈 **Conclusión:**  
El modelo **LightGBM** alcanzó el mejor rendimiento, logrando una predicción precisa con la menor desviación promedio (RMSE).  
Demuestra alta capacidad de generalización y estabilidad frente a los demás modelos.

---

## 📊 Dashboard Power BI
Se incluye una **visualización interactiva en Power BI**, exportada como PDF para análisis de tendencias, comportamiento de ventas y variación por tienda:

<img width="2000" height="1156" alt="image" src="https://github.com/user-attachments/assets/465c26ad-0a11-4b3a-8163-89b90e0b3924" />

---


## 🧰 Tecnologías utilizadas
**Categoría:**	Tecnologías

**Lenguaje:**	Python 3.11

**Machine Learning:**	scikit-learn, LightGBM, XGBoost, CatBoost

**Tracking:**	MLflow

**Base de datos:**	MySQL 8

**Contenedores:**	Docker, Docker Compose

**Visualización:**	Power BI, Matplotlib, Seaborn

**Gestión de código:**	Git + GitHub


---

## 🧠 Autor
Andrew Joshua Flores Díaz – 2025
📍 Data Science & Machine Learning Enthusiast
