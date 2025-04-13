import streamlit as st
import random
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="SmartFeedAI", layout="wide")

st.title("🐟 SmartFeedAI - Prototipo de alimentación inteligente")
st.caption("Versión interactiva - Datos simulados")

# Refrescar cada 3 segundos
st_autorefresh(interval=3000, key="datarefresh")

# ========= Iniciar sesión de estado ==========
if "historial" not in st.session_state:
    st.session_state.historial = []

# ========= Simulación dinámica ==========
# Simulamos variación aleatoria en sensores cada 3 segundos
def simular_sensor(valor, min_val, max_val, variacion=0.5):
    return max(min_val, min(max_val, valor + random.uniform(-variacion, variacion)))

# Valores base
oxigeno = simular_sensor(7.0, 3.0, 10.0)
temperatura = simular_sensor(13.0, 6.0, 20.0)
movimiento = simular_sensor(5.0, 0.0, 10.0)

# Agregar al historial
st.session_state.historial.append({
    "Oxígeno": oxigeno,
    "Temperatura": temperatura,
    "Actividad": movimiento
})
# Limitar a 20 lecturas
st.session_state.historial = st.session_state.historial[-20:]

# ========== 🌊 Sección: Entorno Marino ==========
st.subheader("🌊 Entorno Marino")

col1, col2 = st.columns(2)
with col1:
    salinidad = st.slider("Salinidad (PSU)", 20.0, 40.0, 33.0, step=0.1)
    ph = st.slider("pH del agua", 6.0, 9.0, 7.5, step=0.1)

with col2:
    st.metric("Oxígeno disuelto (mg/L)", round(oxigeno, 2))
    st.metric("Temperatura del agua (°C)", round(temperatura, 2))

# ========== 🐟 Estado de los Peces ==========
st.subheader("🐟 Estado de los Peces")

col3, col4 = st.columns(2)

with col3:
    tamano = st.slider("Tamaño promedio (kg)", 0.5, 5.0, 2.0, step=0.1)
    estres = st.slider("Nivel de estrés (0 = relajado, 10 = muy estresado)", 0.0, 10.0, 3.0, step=0.1)

with col4:
    st.metric("Actividad de los peces", round(movimiento, 2))

# ========== 📊 Decisión del sistema ==========

st.subheader("📊 Decisión del sistema")

alimentar = False
razon = ""

if oxigeno < 6:
    razon = "Oxígeno insuficiente"
elif temperatura < 10 or temperatura > 16:
    razon = "Temperatura fuera del rango ideal"
elif salinidad < 28 or salinidad > 36:
    razon = "Salinidad fuera del rango óptimo"
elif ph < 7.0 or ph > 8.2:
    razon = "pH inadecuado"
elif movimiento < 4:
    razon = "Poca actividad, no tienen hambre"
elif estres > 6:
    razon = "Nivel de estrés alto, evitar alimentación"
else:
    alimentar = True

if alimentar:
    st.success("✅ Condiciones óptimas. Alimentando automáticamente a los peces.")
    st.balloons()
else:
    st.warning(f"⛔ No se recomienda alimentar ahora. Razón: {razon}")

# Alimentación manual
if st.button("🔘 Forzar alimentación manual"):
    st.info("⚠️ Alimentación manual activada.")

# ========== 📈 Historial de sensores ==========
st.subheader("📈 Historial en tiempo real")

df = pd.DataFrame(st.session_state.historial)
st.line_chart(df)