import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
st.set_page_config(layout="wide")

# Refresca cada 3 segundos
st_autorefresh(interval=3000, key="datarefresh")

st.title("🐟 SmartFeedAI - Panel de Simulación")

# Detectar tamaño de pantalla
screen_width = st.get_option("browser.clientWidth")

# Estilo adaptable
is_mobile = screen_width is not None and screen_width < 768

# -------- Fila 1 - SENSORES --------
if is_mobile:
    st.markdown("### 🌊 Entorno Marino")
    salinidad = st.slider("Salinidad del agua (ppt)", 20.0, 40.0, 30.0)
    temperatura_agua = st.slider("Temperatura del agua (°C)", 5.0, 20.0, 12.0)
    oxigeno = st.slider("Nivel de oxígeno (mg/L)", 4.0, 12.0, 8.0)
    ph = st.slider("pH del agua", 6.0, 9.0, 7.5)

    st.markdown("### 🐠 Peces")
    actividad_peces = st.slider("Nivel de actividad (0 = quietos, 10 = muy activos)", 0, 10, 5)
    nivel_estres = st.slider("Nivel de estrés (0 = relajados, 10 = muy estresados)", 0, 10, 3)
    hambre = st.slider("Nivel de hambre (0 = sin hambre, 10 = muy hambrientos)", 0, 10, 6)

else:
    col1, col2 = st.columns(2)

    with col1:
        st.header("🌊 Entorno Marino")
        salinidad = st.slider("Salinidad del agua (ppt)", 20.0, 40.0, 30.0)
        temperatura_agua = st.slider("Temperatura del agua (°C)", 5.0, 20.0, 12.0)
        oxigeno = st.slider("Nivel de oxígeno (mg/L)", 4.0, 12.0, 8.0)
        ph = st.slider("pH del agua", 6.0, 9.0, 7.5)

    with col2:
        st.header("🐠 Peces")
        actividad_peces = st.slider("Nivel de actividad (0 = quietos, 10 = muy activos)", 0, 10, 5)
        nivel_estres = st.slider("Nivel de estrés (0 = relajados, 10 = muy estresados)", 0, 10, 3)
        hambre = st.slider("Nivel de hambre (0 = sin hambre, 10 = muy hambrientos)", 0, 10, 6)

# -------- Fila 2 - Recomendación --------
st.divider()
st.header("🤖 Recomendación Inteligente de Alimentación")

def decidir_alimentacion(actividad, hambre, oxigeno, estres):
    if oxigeno < 5.5:
        return "⚠️", "No alimentar: Bajo nivel de oxígeno en el agua.", "red"
    elif estres > 7:
        return "🚫", "No alimentar: Peces muy estresados.", "orange"
    elif actividad > 6 and hambre > 6:
        return "✅", "¡Alimentar ahora!", "green"
    elif actividad > 4 and hambre > 4:
        return "🟡", "Esperar un poco más o reducir cantidad de alimento.", "yellow"
    else:
        return "❌", "No alimentar por ahora.", "gray"

icono, texto, color = decidir_alimentacion(actividad_peces, hambre, oxigeno, nivel_estres)

st.markdown(f"<div style='padding: 10px; background-color: {color}; color: white; border-radius: 10px; font-size: 20px;'>{icono} {texto}</div>", unsafe_allow_html=True)

# Botón
if "ordenes" not in st.session_state:
    st.session_state.ordenes = []

if icono == "✅":
    if st.button("📤 Enviar orden de alimentación"):
        st.success("✅ Orden enviada correctamente al sistema de alimentación automatizada.")
        st.session_state.ordenes.append({
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Estado": "Alimentación ejecutada"
        })
else:
    st.info("ℹ️ Aún no es momento óptimo para alimentar.")

# Historial
st.subheader("📋 Historial de Recomendaciones")

if "historial" not in st.session_state:
    st.session_state.historial = []

st.session_state.historial.append({
    "Hora": datetime.now().strftime("%H:%M:%S"),
    "Actividad": actividad_peces,
    "Hambre": hambre,
    "Oxígeno": oxigeno,
    "Estrés": nivel_estres,
    "Recomendación": texto
})

st.dataframe(st.session_state.historial, use_container_width=True)

if st.button("🧹 Limpiar historial"):
    st.session_state.historial = []
    st.session_state.ordenes = []
    st.experimental_rerun()

# Historial de órdenes
if st.session_state.ordenes:
    st.subheader("📦 Historial de Órdenes de Alimentación")
    st.dataframe(st.session_state.ordenes, use_container_width=True)