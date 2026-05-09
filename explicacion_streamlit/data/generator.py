import numpy as np
from datetime import datetime


def generar_datos():
    return {
        "Temperatura": np.random.randint(20, 40),
        "Humedad": np.random.randint(30, 90),
        "CPU": np.random.randint(10, 100),
        "Usuarios": np.random.randint(0, 500),
        "Hora": datetime.now().strftime("%H:%M:%S")
    }