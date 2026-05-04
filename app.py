import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Burnout Analyzer", layout="wide")

# -------------------------------
# 🎨 Animated Pastel UI
# -------------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #f6f9fc, #e3f2fd, #fce4ec, #e8f5e9);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.card {
    background: rgba(255,255,255,0.85);
    padding: 18px;
    border-radius: 12px;
    backdrop-filter: blur(6px);
    margin-bottom: 15px;
}

.stButton>button {
    background: #bde0fe;
    color: #1d3557;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

h1 { text-align:center; color:#3a86ff; }

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🧠 Burnout Analyzer")

st.sidebar.markdown("""
### 📌 About
AI-based burnout prediction system.

### ⚙️ Usage
Enter your lifestyle → Analyze → Get insights

### 🎯 Goal
Maintain mental balance
""")

# -------------------------------
# Title
# -------------------------------
st.markdown("<h1>🧠 Student Burnout Dashboard</h1>", unsafe_allow_html=True)
st.info("💡 Balanced lifestyle reduces burnout risk")

# -------------------------------
# Load Model
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "burnout_model.pkl"), "rb"))

# -------------------------------
# Input
# -------------------------------
col1, col2 = st.columns([1,1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📥 Inputs")

    study_hours = st.slider("Study Hours", 0, 12, 6)
    sleep_hours = st.slider("Sleep Hours", 0, 10, 7)
    stress_level = st.slider("Stress Level", 1, 10, 5)
    screen_time = st.slider("Screen Time", 0, 10, 4)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Live Metrics")

    st.metric("Study", study_hours)
    st.metric("Sleep", sleep_hours)
    st.metric("Stress", stress_level)
    st.metric("Screen", screen_time)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🔍 Analyze Burnout"):

    df = pd.DataFrame([[study_hours, sleep_hours, stress_level, screen_time]],
                      columns=['study_hours','sleep_hours','stress_level','screen_time'])

    prediction = model.predict(df)[0]

    # Result
    if prediction == "High":
        st.error("🔴 High Burnout Risk")
    elif prediction == "Medium":
        st.warning("🟠 Moderate Burnout Risk")
    else:
        st.success("🟢 Low Burnout Risk")

    # Score
    risk_score = (stress_level*2 + screen_time + study_hours - sleep_hours)
    risk_score = np.clip(risk_score, 0, 20)

    st.write("### 📈 Burnout Score")
    st.progress(int(risk_score*5))

    # -------------------------------
    # 📊 DASHBOARD CHARTS
    # -------------------------------
    st.markdown("## 📊 Analytics Dashboard")

    col3, col4 = st.columns(2)

    # Bar Chart
    with col3:
        fig1, ax1 = plt.subplots()
        labels = ['Study','Sleep','Stress','Screen']
        values = [study_hours, sleep_hours, stress_level, screen_time]
        ax1.bar(labels, values)
        ax1.set_title("Feature Comparison")
        st.pyplot(fig1)

    # Pie Chart
    with col4:
        fig2, ax2 = plt.subplots()
        ax2.pie(values, labels=labels, autopct='%1.1f%%')
        ax2.set_title("Lifestyle Distribution")
        st.pyplot(fig2)

    # -------------------------------
    # 📈 Trend Simulation
    # -------------------------------
    st.markdown("### 📉 Weekly Burnout Trend (Simulated)")

    trend = np.random.randint(5, 15, size=7)
    st.line_chart(trend)

    # -------------------------------
    # 🧠 Insights
    # -------------------------------
    st.markdown("### 🧠 Insights")

    if sleep_hours < 6:
        st.write("⚠️ Low sleep detected")

    if stress_level > 7:
        st.write("🔥 High stress level")

    if screen_time > 6:
        st.write("📱 High screen usage")

    # -------------------------------
    # 💡 Suggestions
    # -------------------------------
    st.markdown("### 💡 Suggestions")

    suggestions = []

    if sleep_hours < 6:
        suggestions.append("Increase sleep duration")

    if study_hours > 9:
        suggestions.append("Take breaks while studying")

    if stress_level > 7:
        suggestions.append("Practice relaxation techniques")

    if screen_time > 6:
        suggestions.append("Reduce screen exposure")

    if not suggestions:
        suggestions.append("Maintain current lifestyle")

    for s in suggestions:
        st.write("👉", s)

    # -------------------------------
    # 🏆 Summary
    # -------------------------------
    st.success(f"""
    Burnout Level: {prediction}
    Risk Score: {risk_score}/20
    """)

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center;'>🚀 ML Dashboard Project | Burnout Analyzer</p>
""", unsafe_allow_html=True)