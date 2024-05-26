from fastapi import FastAPI, File, UploadFile, HTTPException
import numpy as np
from io import BytesIO
from PIL import Image, UnidentifiedImageError
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS yapılandırması
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("CLAHE_ODIR-ORJ-512_inception_v3.h5")

# Sınıf isimleri
class_names = [
    'Age related Macular Degeneration', 'Cataract', 'Diabetes', 'Glaucoma',
    'Hypertension', 'Normal', 'Others', 'Pathological Myopia'
]

@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}

def read_file_as_image(data) -> np.ndarray:
    try:
        image = Image.open(BytesIO(data))
        return np.array(image)
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image format")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image processing error: {str(e)}")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()

    # Dosya tipini kontrol et
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Dosya boyutunu kontrol et (örneğin, 5MB'den büyük dosyaları reddet)
    max_file_size = 5 * 1024 * 1024  # 5MB
    if len(image_data) > max_file_size:
        raise HTTPException(status_code=400, detail="File size exceeds limit")

    try:
        image = read_file_as_image(image_data)
    except HTTPException as e:
        return e

    # Görüntüyü modelin beklediği boyuta getirme
    image = tf.image.resize(image, (299, 299))  # InceptionV3 için 299x299 olmalı
    # Görüntüyü normalize etme
    image = tf.cast(image, tf.float32) / 255.0
    # Batch haline getirme
    img_batch = np.expand_dims(image, 0)

    # Model üzerinde tahmin yapma
    predictions = MODEL.predict(img_batch)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
