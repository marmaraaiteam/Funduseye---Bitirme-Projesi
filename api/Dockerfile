# Resmi Python görüntüsünü kullanıyoruz, versiyon 3.9
FROM python:3.9-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereksinimler dosyasını kopyala ve gerekli paketleri yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyasını kopyala
COPY . .

# Model dosyasını kopyala (Eğer model dosyası bu dizinde ise)
# COPY path/to/CLAHE_ODIR-ORJ-512_inception_v3.h5 .

# Uygulama başlatma komutu
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]
