import streamlit as st
import requests
from PIL import Image

# Hugging Face API URL
API_URL = "https://bitirme-odirapi.hf.space/predict"

st.title("Göz Hastalığı Tahmini Uygulaması")

uploaded_file = st.file_uploader("Lütfen tahmin edilmesini istediğiniz göz görüntüsünü yükleyin.", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Görüntüyü göster
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Görüntü", use_column_width=True)
    st.write("")
    st.write("Tahmin ediliyor...")

    # Görüntüyü API'ye gönder
    img_bytes = uploaded_file.getvalue()  # Dosyanın tam olarak okunması

    if len(img_bytes) == 0:
        st.error("Yüklenen dosya boş görünüyor. Lütfen geçerli bir dosya yükleyin.")
    else:
        files = {"file": (uploaded_file.name, img_bytes, uploaded_file.type)}

        try:
            response = requests.post(API_URL, files=files)
            response.raise_for_status()
            response_data = response.json()

            if 'class' in response_data and 'confidence' in response_data:
                st.write(f"Tahmin edilen sınıf: {response_data['class']}")
                st.write(f"Güven: {response_data['confidence']:.2f}")
            else:
                st.write("API yanıtı beklenen formatta değil.")
                st.write(response_data)
        except requests.exceptions.RequestException as e:
            st.write("API isteği sırasında bir hata oluştu.")
            st.write(f"Hata Kodu: {response.status_code}")
            st.write(f"Hata Mesajı: {response.text}")
            st.write(e)

