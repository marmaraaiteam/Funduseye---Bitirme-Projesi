# Funduseye Projesi - Mobil Uygulama

Funduseye, göz hastalıklarının sınıflandırılması için geliştirilmiş bir projedir. Bu belge, projenin mobil uygulama bileşeni hakkında bilgi vermektedir.

## İçindekiler
- [Açıklama](#açıklama)
- [Kullanım](#kullanım)
- [API](#api)
- [Grup Üyeleri](#grup-üyeleri)

## Açıklama
Projenin mobil uygulaması, kullanıcıların göz görüntülerini yükleyerek hastalık tahmini almasını sağlamaktadır. Uygulama, API'ye istek göndererek sonucu kullanıcıya göstermektedir. Uygulama Flutter dilinde yazılmıştır.

## Kullanım
1. Mobil uygulamayı açın.
2. Göz görüntüsünü yükleyin.
3. Tahmin edilen sınıfı ve olasılığı görüntüleyin.

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
