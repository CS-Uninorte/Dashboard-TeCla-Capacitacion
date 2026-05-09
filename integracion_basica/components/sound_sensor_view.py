import streamlit as st
import pandas as pd
import serial
import time


def mostrar_sensor_sonido():

    st.title("🎤 Sensor MAX4466 en Tiempo Real")

    st.write(
        """
        Esta vista muestra datos enviados desde Arduino
        utilizando comunicación serial.
        """
    )

    # Selección del puerto
    puerto = st.text_input(
        "Puerto COM",
        value="COM3"
    )

    iniciar = st.button("Conectar Sensor")

    if iniciar:

        try:
            # Conexión serial
            arduino = serial.Serial(
                puerto,
                9600,
                timeout=1
            )

            # Esperar inicialización
            time.sleep(2)

            st.success("Arduino conectado correctamente")

            # Placeholders
            metric_placeholder = st.empty()
            chart_placeholder = st.empty()
            raw_placeholder = st.empty()

            # DataFrame para gráfica
            historial = pd.DataFrame(
                columns=["Amplitud"]
            )

            while True:

                # Leer línea serial
                linea = arduino.readline().decode().strip()

                # Ignorar encabezado
                if (
                    linea
                    and "LecturaCruda" not in linea
                    and "," in linea
                ):

                    try:

                        lecturaCruda, valorMin, valorMax, amplitud = map(
                            int,
                            linea.split(",")
                        )

                        # Nuevo dato
                        nuevo = pd.DataFrame([{
                            "Amplitud": amplitud
                        }])

                        historial = pd.concat(
                            [historial, nuevo],
                            ignore_index=True
                        )

                        # Limitar historial
                        historial = historial.tail(100)

                        # =====================
                        # MÉTRICAS
                        # =====================

                        with metric_placeholder.container():

                            c1, c2, c3, c4 = st.columns(4)

                            c1.metric(
                                "🎵 Amplitud",
                                amplitud
                            )

                            c2.metric(
                                "📈 Máximo",
                                valorMax
                            )

                            c3.metric(
                                "📉 Mínimo",
                                valorMin
                            )

                            c4.metric(
                                "🔊 Lectura",
                                lecturaCruda
                            )

                        # =====================
                        # GRÁFICA
                        # =====================

                        with chart_placeholder.container():

                            st.line_chart(
                                historial,
                                height=400
                            )

                        # =====================
                        # DATOS CRUDOS
                        # =====================

                        raw_placeholder.code(
                            f"""
Lectura Cruda : {lecturaCruda}
Valor Mínimo : {valorMin}
Valor Máximo : {valorMax}
Amplitud     : {amplitud}
                            """,
                            language="text"
                        )

                    except:
                        pass

        except Exception as e:
            st.error(f"Error de conexión: {e}")