import streamlit as st

from components.raw_view import mostrar_version_mala
from components.dashboard_view import mostrar_dashboard
from components.sound_sensor_view import mostrar_sensor_sonido
from utils.styles import cargar_estilos

# Configuración principal
st.set_page_config(
    page_title="Dashboard Demo",
    layout="wide"
)

# Cargar estilos
cargar_estilos()

# Tabs
raw_tab, dashboard_tab, sensor_tab = st.tabs([
    "❌ Versión Mala",
    "✅ Dashboard Bueno",
    "🎤 Sensor de Sonido"
])

# Mostrar contenido
with raw_tab:
    mostrar_version_mala()

with dashboard_tab:
    mostrar_dashboard()
    
with sensor_tab:
    mostrar_sensor_sonido()