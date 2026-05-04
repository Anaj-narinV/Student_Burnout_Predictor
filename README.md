# Student Burnout Predictor

## Overview
This project is a machine learning-based web application that predicts student burnout levels based on academic performance, study habits, and lifestyle factors. The goal is to identify early signs of burnout and provide data-driven insights for awareness and understanding.

## Live Demo
https://studentburnoutpredictor-ezwhmcuzuu3r7cdftpm5fm.streamlit.app/

## Features
- Predicts student burnout level in real-time  
- Machine learning model-based prediction  
- Interactive web interface  
- Input-based analysis using academic and lifestyle parameters  
- Simple and user-friendly design  

## Tech Stack
- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  

## Project Structure

student-burnout-predictor/
│
├── app.py Main Streamlit application
├── model.pkl Trained machine learning model
├── requirements.txt Required dependencies
├── dataset.csv Dataset used for training (if applicable)
│
├── /assets Images and UI assets (if any)
├── /models Saved ML models (if multiple used)
├── /notebooks Jupyter notebooks for analysis and training
│
└── README.md Project documentation

## Installation and Setup

### 1. Clone the repository

git clone https://github.com/your-username/student-burnout-predictor.git

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the application

streamlit run app.py

## How It Works
1. User enters academic and lifestyle details  
2. Data is processed using a trained machine learning model  
3. The model predicts burnout level (Low, Medium, High)  
4. Results are displayed instantly in the web app  

## Future Improvements
- Improve model accuracy with larger datasets  
- Add personalized recommendations  
- Enhance UI and design  
- Add user history tracking  
- Deploy with authentication system  

## Author
Niranjana V
CSE Student  

---

## License
This project is for educational purposes only.
