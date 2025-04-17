import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import random

# Estilos personalizados
st.set_page_config(page_title="Dashboard Alimentador", layout="wide", initial_sidebar_state="expanded")

# CSS personalizado
st.markdown("""
    <style>
        body {
            background-color: #111;
            color: white;
        }
        .reportview-container {
            background: #111;
        }
        header {
            background-color: #111;
        }
        footer {
            visibility: hidden;
        }
        .footer:after {
            content:'Desarrollado por Miguel 🐟 | Proyecto ESP32 + Dashboard';
            visibility: visible;
            display: block;
            position: relative;
            padding: 10px;
            text-align: center;
            color: #888;
        }
        .logo {
            position: absolute;
            top: 10px;
            left: 10px;
        }
    </style>
    <div class="logo">
        <img src="https://i.imgur.com/7b6nbHR.png" width="100"/>
    </div>
    <div class="footer"></div>
""", unsafe_allow_html=True)

# Título principal
st.title("📊 Alimentador Automático de Peces")

# Simulación de datos
def generate_data():
    now = datetime.now().strftime("%H:%M:%S")
    temp = round(random.uniform(8, 15), 2)
    actividad = round(random.uniform(0.2, 0.9), 2)
    turbidez = round(random.uniform(0.1, 0.8), 2)
    return now, temp, actividad, turbidez

times = []
temps = []
actividades = []
turbideces = []

for _ in range(30):
    t, temp, act, turb = generate_data()
    times.append(t)
    temps.append(temp)
    actividades.append(act)
    turbideces.append(turb)

df = pd.DataFrame({
    "Hora": times,
    "Temperatura (°C)": temps,
    "Actividad (hambre)": actividades,
    "Turbidez": turbideces
})

# Visualización
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡️ Temperatura del Agua")
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(x=df["Hora"], y=df["Temperatura (°C)"], mode="lines+markers", name="Temp"))
    fig_temp.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    st.subheader("🐟 Nivel de Actividad / Hambre")
    fig_act = go.Figure()
    fig_act.add_trace(go.Scatter(x=df["Hora"], y=df["Actividad (hambre)"], mode="lines+markers", name="Actividad"))
    fig_act.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(fig_act, use_container_width=True)

st.subheader("🌊 Nivel de Turbidez del Agua")
fig_turb = go.Figure()
fig_turb.add_trace(go.Scatter(x=df["Hora"], y=df["Turbidez"], mode="lines+markers", name="Turbidez"))
fig_turb.update_layout(template="plotly_dark", height=300)
st.plotly_chart(fig_turb, use_container_width=True)

# Footer (ya agregado por CSS arriba)
