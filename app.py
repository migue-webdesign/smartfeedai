import streamlit as st

st.set_page_config(page_title="SmartFeedAI", layout="wide")

st.title("🐟 SmartFeedAI - Prototipo de alimentación inteligente")

st.subheader("🎛️ Simulación de sensores (ajusta los valores manualmente)")

# Sliders para simular los sensores
oxigeno = st.slider("Oxígeno disuelto (mg/L)", min_value=3.0, max_value=10.0, value=7.0, step=0.1)
temperatura = st.slider("Temperatura del agua (°C)", min_value=6.0, max_value=20.0, value=13.0, step=0.1)
movimiento = st.slider("Actividad de los peces (0 = baja, 10 = alta)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
tamano = st.slider("Tamaño promedio (kg)", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

# Métricas visuales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Oxígeno", f"{oxigeno} mg/L")
with col2:
    st.metric("Temp. Agua", f"{temperatura} °C")
with col3:
    st.metric("Actividad", movimiento)
with col4:
    st.metric("Tamaño", f"{tamano} kg")

# Lógica de decisión
alimentar = False
razon = ""

if oxigeno < 6:
    razon = "Oxígeno insuficiente"
elif temperatura < 10 or temperatura > 16:
    razon = "Temperatura fuera del rango ideal"
elif movimiento < 4:
    razon = "Poca actividad, no tienen hambre"
else:
    alimentar = True

st.subheader("📊 Decisión del sistema")

if alimentar:
    st.success("✅ Condiciones óptimas. Alimentando automáticamente a los peces.")
    st.balloons()
else:
    st.warning(f"⛔ No se recomienda alimentar ahora. Razón: {razon}")

if st.button("🔘 Forzar alimentación manual"):
    st.info("⚠️ Alimentación manual activada.")

st.caption("Versión interactiva - Datos simulados - SmartFeedAI - by CreativoChile")
