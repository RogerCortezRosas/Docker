from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
#from modelo import model


app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Verificar que el archivo sea una imagen JPG o PNG
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Solo se permiten imágenes JPG o PNG")
    
    try:
        # Leer el archivo en memoria
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        #obj_model = model(image)
        #prediction = obj_model.prediction()
        
        return JSONResponse(content={"filename": file.filename, "format": image.format, "size": image.size})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

#ejecutar 
#uvicorn main:app --reload
#main: Es el nombre del archivo (sin la extensión .py).

#app: Es el nombre de la variable que contiene la instancia de FastAPI en tu archivo main.py.