import streamlit as st
from PIL import Image
import requests

# URL de la API FastAPI
API_URL = "http://0.0.0.0:8000/upload/"

# Título de la aplicación
st.title("Que imagen es real?")

# Cargar la imagen
uploaded_file = st.file_uploader("Selecciona una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Abrir la imagen con PIL
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Define la ruta donde se almacenará el archivo
    file_path = f"model/imagenes/{uploaded_file.name}"
    
    #Guardar la imagen
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Llamar a api upload para predecir la imagen

    if st.button("Subir Imagen"):
        response = requests.post(API_URL,files=file_path)


    if response.status_code == 200:
            st.success(f"✅ {response.json()['mensaje']}")
    else:
            st.error("❌ Error al subir la imagen")
