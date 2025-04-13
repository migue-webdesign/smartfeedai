import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Refresca automáticamente cada 3 segundos
st_autorefresh(interval=3000, key="datarefresh")

st.title("🐟 SmartFeedAI - Panel de Simulación")

st.markdown("Simulador de sensores para alimentar salmones de forma inteligente.")

# --- ENTORNO MARINO ---
st.header("🌊 Entorno Marino")

salinidad = st.slider("Salinidad del agua (ppt)", 20.0, 40.0, 30.0)
temperatura_agua = st.slider("Temperatura del agua (°C)", 5.0, 20.0, 12.0)
oxigeno = st.slider("Nivel de oxígeno (mg/L)", 4.0, 12.0, 8.0)
ph = st.slider("pH del agua", 6.0, 9.0, 7.5)

# --- PECES ---
st.header("🐠 Peces")

actividad_peces = st.slider("Nivel de actividad (0 = quietos, 10 = muy activos)", 0, 10, 5)
nivel_estres = st.slider("Nivel de estrés (0 = relajados, 10 = muy estresados)", 0, 10, 3)
hambre = st.slider("Nivel de hambre (0 = sin hambre, 10 = muy hambrientos)", 0, 10, 6)

# --- LÓGICA DE DECISIÓN ---
st.header("🤖 Recomendación Inteligente de Alimentación")

def decidir_alimentacion(actividad, hambre, oxigeno, estres):
    if oxigeno < 5.5:
        return "⚠️ No alimentar: Bajo nivel de oxígeno en el agua."
    elif estres > 7:
        return "🚫 No alimentar: Peces muy estresados."
    elif actividad > 6 and hambre > 6:
        return "✅ Recomendación: ¡Alimentar ahora!"
    elif actividad > 4 and hambre > 4:
        return "🟡 Esperar un poco más o reducir cantidad de alimento."
    else:
        return "❌ No alimentar por ahora."

recomendacion = decidir_alimentacion(actividad_peces, hambre, oxigeno, nivel_estres)
st.subheader(recomendacion)