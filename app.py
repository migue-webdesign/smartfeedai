import streamlit as st
import random
import time

# Simulación de sensores
def leer_sensor_oxigeno():
    return round(random.uniform(4.0, 9.0), 2)

def leer_sensor_temperatura():
    return round(random.uniform(8.0, 18.0), 2)

def leer_movimiento_peces():
    return round(random.uniform(0, 10), 2)

def leer_tamano_promedio():
    return round(random.uniform(1.0, 4.5), 1)

st.set_page_config(page_title="SmartFeedAI", layout="wide")

st.title("🐟 SmartFeedAI - Prototipo de alimentación inteligente")

# Lectura simulada
oxigeno = leer_sensor_oxigeno()
temperatura = leer_sensor_temperatura()
movimiento = leer_movimiento_peces()
tamano = leer_tamano_promedio()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Oxígeno (mg/L)", oxigeno)
with col2:
    st.metric("Temperatura (°C)", temperatura)
with col3:
    st.metric("Movimiento", movimiento)
with col4:
    st.metric("Tamaño promedio (kg)", tamano)

# Lógica de decisión
alimentar = False
razon = ""

if oxigeno < 6:
    razon = "Oxígeno insuficiente"
elif temperatura < 10 or temperatura > 16:
    razon = "Temperatura no óptima"
elif movimiento < 4:
    razon = "Bajo movimiento (poca actividad)"
else:
    alimentar = True

st.subheader("📊 Decisión del sistema")

if alimentar:
    st.success("✅ Condiciones óptimas. Alimentando a los peces...")
    st.balloons()
else:
    st.warning(f"⛔ No se recomienda alimentar. Razón: {razon}")

if st.button("Forzar alimentación"):
    st.info("⚠️ Alimentación manual activada.")

# Pie de página
st.caption("Versión demo - Datos simulados - Proyecto SmartFeedAI - by Prido")
