# Dashboard-TeCla-Capacitacion
Archivos de prueba para capacitación en StreamLit.

# Dashboard Demo - Streamlit

Aplicación desarrollada con Python y Streamlit para demostrar la diferencia entre visualizar datos crudos y utilizar dashboards interactivos.

La aplicación contiene dos vistas:

- ❌ **Versión Mala:** datos impresos en tiempo real sin organización.
- ✅ **Dashboard Bueno:** métricas y gráficas visuales en tiempo real.

---

# Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.10 o superior
- GitHub Desktop
- Git

---

# Clonar el repositorio con GitHub Desktop

1. Abrir GitHub Desktop.
2. Ir a:

```text
File > Clone Repository
```

3. Seleccionar el repositorio.
4. Elegir la carpeta donde se guardará.
5. Presionar:

```text
Clone
```

---

# Abrir el proyecto

Después de clonar:

1. En GitHub Desktop seleccionar:

```text
Repository > Open in Visual Studio Code
```

o abrir manualmente la carpeta del proyecto en VS Code.

---

# Crear entorno virtual (virtualenv)

## Instalar virtualenv

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install virtualenv
```

---

## Crear el entorno virtual

### Windows

```bash
python -m virtualenv venv
```

o

```bash
virtualenv venv
```

### Linux / Mac

```bash
python3 -m virtualenv venv
```

---

# Activar entorno virtual

## Windows (PowerShell)

```bash
.\venv\Scripts\activate
```

## Windows (CMD)

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

Cuando el entorno esté activo, verás algo parecido a:

```text
(venv)
```

al inicio de la terminal.

---

# Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

---

# Ejecutar la aplicación

Ejecutar:

```bash
streamlit run nombre_del_archivo_principal.py
```

Luego abrir en el navegador haciendo click en el link generado.




---

# Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- NumPy

---

# Objetivo del proyecto

Mostrar cómo un dashboard puede transformar grandes cantidades de datos difíciles de interpretar en información clara y útil para la toma de decisiones.

