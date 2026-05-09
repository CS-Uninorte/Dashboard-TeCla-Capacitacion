import streamlit as st


def cargar_estilos():

    st.markdown(
        """
        <style>

        .stMetric {
            background-color: #111827;
            padding: 15px;
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )