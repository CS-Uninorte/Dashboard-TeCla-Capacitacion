import streamlit as st
import time

from data.generator import generar_datos


def mostrar_version_mala():

    st.title("❌ Datos Crudos")

    st.write(
        "Esta vista muestra muchos datos sin organización visual."
    )
    
    placeholder = st.empty()

    texto = ""

    for _ in range(30):

        datos = generar_datos()

        texto += f"""
        [{datos['Hora']}]
        Temperatura = {datos['Temperatura']}°C
        Humedad = {datos['Humedad']}%
        CPU = {datos['CPU']}%
        Usuarios = {datos['Usuarios']}
        -----------------------------
        """

        placeholder.text(texto)
        time.sleep(0.5)