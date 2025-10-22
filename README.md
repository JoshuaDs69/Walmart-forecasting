# 🧠 Walmart Sales Forecasting
Proyecto de predicción de ventas semanales usando modelos de Machine Learning (Random Forest, XGBoost, LightGBM y CatBoost).

## 📊 Dataset
- Fuente: [Kaggle – Walmart Store Sales Forecasting](https://www.kaggle.com/datasets)
- Periodo: 2010–2012
- Variables: Fecha, tienda, ventas semanales, CPI, desempleo, día feriado, etc.

## ⚙️ Modelos y resultados
| Modelo | R² | RMSE |
|---------|-----|-------|
| Random Forest | 0.935 | 144,150 |
| XGBoost | 0.966 | 104,106 |
| LightGBM | **0.9757** | **88,450** |
| CatBoost | 0.963 | 108,724 |

**Conclusión:** LightGBM obtuvo el mejor rendimiento con alta precisión y generalización.

## 📈 Dashboard
Incluye visualización interactiva en Power BI exportada a PDF (`Dashboard_Walmart.pdf`).

## 🧩 Tecnologías
- Python, Scikit-learn, LightGBM, CatBoost, XGBoost  
- Pandas, NumPy, Seaborn, Matplotlib  
- Power BI

## 🧠 Autor
Andrew Joshua Flores Díaz – 2025
📍 Data Science & Machine Learning Enthusiast

