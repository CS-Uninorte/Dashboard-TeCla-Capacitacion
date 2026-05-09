import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

st.set_page_config(
    page_title="Dashboard Demo",
    layout="wide"
)

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2 = st.tabs(["❌ Versión Mala", "✅ Dashboard Bueno"])

# -----------------------------
# Generador de datos
# -----------------------------
def generar_datos():
    return {
        "Temperatura": np.random.randint(20, 40),
        "Humedad": np.random.randint(30, 90),
        "CPU": np.random.randint(10, 100),
        "Usuarios": np.random.randint(0, 500),
        "Hora": datetime.now().strftime("%H:%M:%S")
    }

# =============================
# TAB 1 - VERSION MALA
# =============================
with tab1:

    st.title("❌ Datos Crudos Sin Dashboard")

    st.write("Información en tiempo real sin organización:")

    placeholder = st.empty()

    datos_texto = ""

    for i in range(30):

        datos = generar_datos()

        datos_texto += f"""
        [{datos['Hora']}]
        Temperatura = {datos['Temperatura']}°C
        Humedad = {datos['Humedad']}%
        CPU = {datos['CPU']}%
        Usuarios conectados = {datos['Usuarios']}
        -----------------------------------------
        """

        placeholder.text(datos_texto)

        time.sleep(0.5)

# =============================
# TAB 2 - DASHBOARD BONITO
# =============================
with tab2:

    st.title("✅ Dashboard Inteligente")

    chart_placeholder = st.empty()
    metrics_placeholder = st.empty()

    historial = pd.DataFrame(columns=[
        "Temperatura",
        "Humedad",
        "CPU",
        "Usuarios"
    ])

    for i in range(30):

        datos = generar_datos()

        nuevo = pd.DataFrame([{
            "Temperatura": datos["Temperatura"],
            "Humedad": datos["Humedad"],
            "CPU": datos["CPU"],
            "Usuarios": datos["Usuarios"]
        }])

        historial = pd.concat([historial, nuevo], ignore_index=True)

        # Métricas
        with metrics_placeholder.container():

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("🌡 Temperatura", f"{datos['Temperatura']} °C")
            c2.metric("💧 Humedad", f"{datos['Humedad']} %")
            c3.metric("🖥 CPU", f"{datos['CPU']} %")
            c4.metric("👥 Usuarios", datos["Usuarios"])

        # Gráfica
        with chart_placeholder.container():

            st.line_chart(historial)

        time.sleep(0.5)