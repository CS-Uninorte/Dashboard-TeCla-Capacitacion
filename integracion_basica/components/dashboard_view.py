import streamlit as st
import pandas as pd
import time

from data.generator import generar_datos


def mostrar_dashboard():

    st.title("✅ Dashboard")

    st.write(
        "La misma información presentada de forma visual."
    )
    chart_placeholder = st.empty()
    metrics_placeholder = st.empty()

    historial = pd.DataFrame(columns=[
        "Temperatura",
        "Humedad",
        "CPU",
        "Usuarios"
    ])
    
    for _ in range(30):

        datos = generar_datos()

        nuevo = pd.DataFrame([{
            "Temperatura": datos["Temperatura"],
            "Humedad": datos["Humedad"],
            "CPU": datos["CPU"],
            "Usuarios": datos["Usuarios"]
        }])

        historial = pd.concat([
            historial,
            nuevo
        ], ignore_index=True)
        
        with metrics_placeholder.container():

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "🌡 Temperatura",
                f"{datos['Temperatura']} °C"
            )

            c2.metric(
                "💧 Humedad",
                f"{datos['Humedad']} %"
            )

            c3.metric(
                "🖥 CPU",
                f"{datos['CPU']} %"
            )
            c4.metric(
                "👥 Usuarios",
                datos["Usuarios"]
            )

        with chart_placeholder.container():
            st.line_chart(historial)

        time.sleep(0.5)