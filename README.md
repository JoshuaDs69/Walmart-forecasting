# 🧠 Walmart Sales Forecasting
Predicción de ventas semanales en tiendas **Walmart** utilizando modelos de *Machine Learning* supervisado.

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

📄 `Dashboard_Walmart.pdf`

---

## 🧩 Tecnologías utilizadas
- **Lenguaje:** Python  
- **Librerías ML:** Scikit-learn, LightGBM, CatBoost, XGBoost  
- **Procesamiento:** Pandas, NumPy  
- **Visualización:** Seaborn, Matplotlib, Power BI  

---

## 🚀 Ejecución del proyecto

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/walmart-forecasting.git

# Entrar a la carpeta del proyecto
cd walmart-forecasting

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el notebook
jupyter notebook Walmart_proyect.ipynb

<<<<<<< HEAD
=======
## 🧠 Autor
Andrew Joshua Flores Díaz – 2025
📍 Data Science & Machine Learning Enthusiast

>>>>>>> 12af02c8fa748cd303acaaf0915ec93c98c1954b
