# 🏠 House Price Prediction App (Streamlit + FastAPI + ML)

An end-to-end Machine Learning web application that predicts house prices based on user input.  
The project uses **Streamlit for frontend UI** and **FastAPI as backend API** serving the ML model.

---

## 🚀 Live Demo

- 🌐 Streamlit App: https://your-streamlit-link  
- ⚡ FastAPI API Docs: https://your-api-link/docs  

---

## 🧠 Project Overview

This project predicts house prices using a trained machine learning model.

The workflow is:

- User enters input in Streamlit UI  
- Streamlit sends request to FastAPI backend  
- FastAPI processes data using ML model  
- Model returns predicted house price  
- Result is displayed in Streamlit UI  

---

## ⚙️ Tech Stack

- Python  
- Streamlit  
- FastAPI  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  
- Uvicorn  

---

## 🏗️ Architecture

Streamlit (Frontend) → FastAPI (Backend) → Machine Learning Model (.pkl)

---

## 📁 Project Structure
backend/
│── app.py # FastAPI backend
│── model.pkl # Trained ML model

frontend/
│── streamlit_app.py # Streamlit UI

requirements.txt
README.md

---

## ▶️ How to Run Locally

### 1. Clone the repository

git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run FastAPI backend

cd backend
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs

### 4. Run Streamlit frontend

cd frontend
streamlit run streamlit_app.py

### 🚀 Deployment

Frontend: Streamlit Cloud
Backend: Render / Railway

### 📊 Features
Real-time house price prediction
REST API using FastAPI
Clean and interactive Streamlit UI
Modular project structure
Easy deployment ready

### 🔮 Future Improvements
Add feature importance explanation
Store prediction history
Improve model accuracy
Add authentication system
Dockerize the project

### 👨‍💻 Author
Name: chauhan keval

GitHub: https://github.com/chauhankeval33
