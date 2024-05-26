# Funduseye Projesi - API

Funduseye, göz hastalıklarının sınıflandırılması için geliştirilmiş bir projedir. Bu belge, projenin API bileşeni hakkında bilgi vermektedir.

## İçindekiler
- [Açıklama](#açıklama)
- [Kullanım](#kullanım)
- [Endpoint](#endpoint)
- [Grup Üyeleri](#grup-üyeleri)

## Açıklama
Proje, göz hastalıklarını tahmin etmek için bir API kullanmaktadır. Bu API, FastAPI framework'ü kullanılarak geliştirilmiş ve Hugging Face üzerinden sunulmaktadır. API, eğitilmiş TensorFlow modelini kullanarak görüntü sınıflandırması yapmaktadır.

## Kullanım
API'yi kullanmak için bir POST isteği yapmanız gerekmektedir. İstek, tahmin edilecek göz görüntüsünü içermelidir. Aşağıda örnek bir kullanım verilmiştir:

### Örnek İstek
```http
POST /predict HTTP/1.1
Host: https://huggingface.co/spaces/Bitirme/odirapi
Content-Type: multipart/form-data

Content-Disposition: form-data; name="file"; filename="göz_resmi.jpg"
Content-Type: image/jpeg

[Dosya İçeriği]
```

### Örnek Cevap
```json
{
  "class": "Glaucoma",
  "confidence": 0.85
}
```

## Endpoint
- API linki: [https://huggingface.co/spaces/Bitirme/odirapi](https://huggingface.co/spaces/Bitirme/odirapi)

## Grup Üyeleri
- Yaren Can
- Kübra Buzlu
- Hüseyin Taşkın
