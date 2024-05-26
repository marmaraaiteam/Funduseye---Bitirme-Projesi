# Funduseye Projesi - Web Arayüzü

Funduseye, göz hastalıklarının sınıflandırılması için geliştirilmiş bir projedir. Bu belge, projenin web arayüzü bileşeni hakkında bilgi vermektedir.

## İçindekiler
- [Web Arayüzü](#web-arayüzü)
- [API](#api)
- [Grup Üyeleri](#grup-üyeleri)

## Web Arayüzü

### Açıklama
Web arayüzü, kullanıcıların göz görüntülerini yükleyerek tahmin almasını sağlar. API'yi kullanarak tahminleri gerçekleştirir. Web arayüzü için Streamlit kullanılmıştır ve Hugging Face üzerinden sunulmaktadır.

### Kullanım
Web arayüzüne erişmek için aşağıdaki linki kullanabilirsiniz:
- Web arayüzü linki: [https://huggingface.co/spaces/Bitirme/odirmodel](https://huggingface.co/spaces/Bitirme/odirmodel)

Web arayüzü, Hugging Face API'sini kullanmaktadır. Bu API, göz görüntülerini işleyerek hastalık tahmini yapar.

## API

### Açıklama
Proje, göz hastalıklarını tahmin etmek için bir API kullanmaktadır. Bu API, Hugging Face üzerinden sunulmaktadır ve eğitilmiş TensorFlow modelini kullanarak görüntü sınıflandırması yapmaktadır.

### Kullanım
API'yi kullanmak için bir POST isteği yapmanız gerekmektedir. İstek, tahmin edilecek göz görüntüsünü içermelidir.

#### Endpoint
- API linki: [https://huggingface.co/spaces/Bitirme/odirapi](https://huggingface.co/spaces/Bitirme/odirapi)

## Grup Üyeleri
- Yaren Can
- Kübra Buzlu
- Hüseyin Taşkın
